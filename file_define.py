"""

文件相关的类定义

"""
import json

# 导入包 使Record可用

from data_define import Record

# 定义一个抽象类 作为顶层设计 表明哪些功能需要实现
class FileReader:
    # 定义读取文件数据的方法
    def read_data(self) ->list[Record]:
        """将读到的每一项数据转化为record类,将他们封装为list类内返回出去"""
        pass
# 构建具体操作
class TextFileReader(FileReader):

        def __init__(self,path) :
            self.path = path    # 定义成员变量记录文件路径
        # 复写(实现抽象方法) 父类的方法
        def read_data(self) -> list[Record]:
            f = open(self.path,"r",encoding= "UTF-8")# 方法内部使用成员变量要使用self

            record_list :list[Record] = []

            for line in f.readlines():
                # 消除读取到的行的空格和换行符
                line = line.strip()
                data_list = line.split(",")
                record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
                record_list.append(record)
            f.close()
            return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path # 记录变量的数据

    def read_data(self) ->list[Record]:
        f = open(self.path, "r", encoding="UTF-8")  # 方法内部使用成员变量要使用self

        record_list: list[Record] = []

        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)


        f.close()
        return record_list


if __name__ == "__main__":
    # 读取文件
    text_file_reader = TextFileReader("/Users/apple/2011年1月销售数据.txt")

    json_file_reader = JsonFileReader("/Users/apple/2011年2月销售数据JSON.txt")
    # 调用方法
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)

# SQL : 开发人员必备技能 本课程只是简单了解基础语法
# 数据的存储和计算 python语言是对数据进行计算
# 使用图形化工具操作MySQL数据库软件 使用命令行
# 使用 pymysql 操作mySQL
