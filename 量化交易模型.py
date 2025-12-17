import ccxt  # 用于与交易所交互
import pandas as pd  # 数据处理
import matplotlib.pyplot as plt  # 绘图
import time  # 时间处理

# 设置Binance期货测试网络的API连接
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',  # 替换为您的API Key
    'secret': 'YOUR_SECRET_KEY',  # 替换为您的Secret Key
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',  # 使用期货市场
    },
    'urls': {
        'api': {
            'public': 'https://testnet.binancefuture.com/fapi/v1',  # 测试网络API
            'private': 'https://testnet.binancefuture.com/fapi/v1',
        }
    }
})

# 设置交易参数
symbol = 'BTC/USDT'  # 交易对
leverage = 100  # 杠杆倍数
timeframe = '1m'  # 1分钟K线
limit = 1000  # 历史数据条数

# 设置杠杆
def set_leverage(symbol, leverage):
    try:
        exchange.fapiPrivate_post_leverage({
            'symbol': symbol.replace('/', ''),  # 如BTCUSDT
            'leverage': leverage
        })
        print(f"成功设置杠杆为 {leverage}x")
    except Exception as e:
        print(f"设置杠杆失败: {e}")

# 获取历史K线数据
def fetch_ohlcv(symbol, timeframe, limit):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# 计算RSI
def calculate_rsi(df, period=14):
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))
    return df

# 生成买卖信号
def generate_signals(df, rsi_overbought=70, rsi_oversold=30):
    df['signal'] = 0  # 0: 无信号
    df['signal'][df['rsi'] < rsi_oversold] = 1  # 买入
    df['signal'][df['rsi'] > rsi_overbought] = -1  # 卖出
    df['position'] = df['signal'].diff()  # 持仓变化
    return df

# 模拟高频交易
def simulate_trading(df, initial_balance=10000):
    balance = initial_balance  # 初始USDT
    position = 0  # 当前持仓（BTC）
    trade_history = []

    for i in range(1, len(df)):
        if df['position'].iloc[i] == 1:  # 买入
            if position == 0:
                buy_price = df['close'].iloc[i]
                position = (balance / buy_price) * leverage  # 杠杆影响持仓量
                balance = 0
                trade_history.append(('buy', df.index[i], buy_price, position))
                print(f"买入价格: {buy_price}, 时间: {df.index[i]}")
        elif df['position'].iloc[i] == -1:  # 卖出
            if position > 0:
                sell_price = df['close'].iloc[i]
                balance = (position * sell_price) / leverage  # 杠杆影响收益
                position = 0
                trade_history.append(('sell', df.index[i], sell_price, balance))
                print(f"卖出价格: {sell_price}, 时间: {df.index[i]}")

    # 计算最终余额
    if position > 0:
        balance = (position * df['close'].iloc[-1]) / leverage
    return balance, trade_history

# 绘制交易结果
def plot_results(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='收盘价')
    plt.scatter(df[df['position'] == 1].index, df[df['position'] == 1]['close'], marker='^', color='g', label='买入')
    plt.scatter(df[df['position'] == -1].index, df[df['position'] == -1]['close'], marker='v', color='r', label='卖出')
    plt.title(f'{symbol} RSI策略（杠杆 {leverage}x）')
    plt.legend()
    plt.show()

# 主函数
def main():
    set_leverage(symbol, leverage)  # 设置杠杆
    df = fetch_ohlcv(symbol, timeframe, limit)
    df = calculate_rsi(df)
    df = generate_signals(df)
    final_balance, trade_history = simulate_trading(df)
    print(f"最终余额: {final_balance} USDT")
    plot_results(df)

if __name__ == "__main__":
    main()