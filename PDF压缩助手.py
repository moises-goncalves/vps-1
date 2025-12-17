import os
import subprocess
import shutil


def compress_pdf(input_path: str, output_path: str, target_size_mb: float = 199.0,
                 initial_check_mb: float = 200.0) -> bool:
    """
    压缩PDF文件，如果其大小超过初始检查阈值，则尝试将其压缩到目标大小以下。

    Args:
        input_path (str): 输入PDF文件的路径。
        output_path (str): 压缩后PDF文件的输出路径。
        target_size_mb (float): 目标文件大小（MB）。压缩后的文件大小应小于此值。
        initial_check_mb (float): 初始检查阈值（MB）。只有当文件大小超过此值时才进行压缩。

    Returns:
        bool: 如果成功压缩到目标大小（或文件本身就小于初始检查阈值），则返回True；否则返回False。
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # 获取输入文件大小（MB）
        input_file_size_bytes = os.path.getsize(input_path)
        input_file_size_mb = input_file_size_bytes / (1024 * 1024)
        print(f"原始文件 '{os.path.basename(input_path)}' 大小: {input_file_size_mb:.2f} MB")

        # 如果文件大小未超过初始检查阈值，则直接复制并返回成功
        if input_file_size_mb <= initial_check_mb:
            print(f"文件大小 ({input_file_size_mb:.2f} MB) 未超过 {initial_check_mb:.2f} MB，无需压缩。")
            shutil.copy2(input_path, output_path)  # 复制原文件到目标位置
            return True

        print(f"文件大小超过 {initial_check_mb:.2f} MB，开始尝试压缩...")

        # 定义Ghostscript的压缩设置。/ebook 提供了一个很好的平衡，能显著减小文件大小。
        # 其他选项包括：
        # /screen: 最低质量，文件最小，适合屏幕显示。
        # /printer: 较高质量，适合打印。
        # /prepress: 最高质量，几乎无损，但压缩效果有限。
        # /default: 默认设置，不进行过多压缩。
        gs_compression_setting = "/ebook"

        # Ghostscript 命令构建
        # -sDEVICE=pdfwrite: 指定输出设备为PDF写入器。
        # -dCompatibilityLevel=1.4: 设置PDF兼容性级别。
        # -dPDFSETTINGS={setting}: 应用预定义的PDF设置，用于控制压缩级别。
        # -dNOPAUSE -dQUIET -dBATCH: 以批处理模式运行，不暂停，静默输出。
        # -sOutputFile={output_path}: 指定输出文件路径。
        # {input_path}: 指定输入文件路径。
        command = [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={gs_compression_setting}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path
        ]

        print(f"正在执行 Ghostscript 命令: {' '.join(command)}")
        # 执行Ghostscript命令
        result = subprocess.run(command, capture_output=True, text=True, check=False)

        if result.returncode != 0:
            print(f"Ghostscript 命令执行失败，错误代码: {result.returncode}")
            print(f"STDOUT:\n{result.stdout}")
            print(f"STDERR:\n{result.stderr}")
            # 尝试复制原始文件到输出路径，以防万一
            shutil.copy2(input_path, output_path)
            return False

        # 检查压缩后的文件大小
        if not os.path.exists(output_path):
            print("错误：压缩后文件未生成。")
            return False

        compressed_file_size_bytes = os.path.getsize(output_path)
        compressed_file_size_mb = compressed_file_size_bytes / (1024 * 1024)
        print(f"压缩后文件 '{os.path.basename(output_path)}' 大小: {compressed_file_size_mb:.2f} MB")

        if compressed_file_size_mb < target_size_mb:
            print(f"恭喜！文件已成功压缩到目标大小 {target_size_mb:.2f} MB 以下。")
            return True
        else:
            print(f"警告：文件压缩后仍大于目标大小 {target_size_mb:.2f} MB。可能需要更强的压缩设置或手动优化。")
            return False

    except FileNotFoundError:
        print("错误：未找到 'gs' 命令。请确保您已安装 Ghostscript 并将其添加到系统PATH中。")
        print("您可以在这里下载 Ghostscript: https://www.ghostscript.com/download.html")
        return False
    except Exception as e:
        print(f"在压缩过程中发生未知错误: {e}")
        return False


if __name__ == "__main__":
    # --- 示例用法 ---
    # 在运行此脚本之前，请确保：
    # 1. 您已安装 Ghostscript。您可以在其官方网站下载：https://www.ghostscript.com/download.html
    # 2. Ghostscript 的可执行文件（在Windows上通常是gs.exe）已添加到您的系统PATH环境变量中。
    #    或者，您可以提供Ghostscript可执行文件的完整路径，例如：
    #    command = ["C:\\Program Files\\gs\\gs9.xx\\bin\\gswin64c.exe", ...]

    # 用户提供的输入PDF文件路径
    input_pdf_file = '/Users/apple/Downloads/IMG_8675 2.pdf'

    # 构造输出文件路径，在原文件名的基础上添加 '_compressed' 后缀
    # 确保输出文件与输入文件在同一目录下，并避免覆盖原文件
    file_dir = os.path.dirname(input_pdf_file)
    file_name_without_ext = os.path.splitext(os.path.basename(input_pdf_file))[0]
    output_pdf_file = os.path.join(file_dir, f"{file_name_without_ext}_compressed.pdf")

    print("\n--- 开始PDF压缩示例 ---")

    # 检查输入文件是否存在
    if not os.path.exists(input_pdf_file):
        print(f"错误：指定的输入文件 '{input_pdf_file}' 不存在。")
        print("请检查文件路径是否正确。")
    else:
        success = compress_pdf(input_pdf_file, output_pdf_file, target_size_mb=199.0, initial_check_mb=200.0)
        if success:
            print("\n--- PDF压缩成功完成！ ---")
            print(f"压缩后的文件位于: {os.path.abspath(output_pdf_file)}")
        else:
            print("\n--- PDF压缩操作未能达到预期效果或发生错误。 ---")
            print(f"请检查上述输出，并确保Ghostscript已正确安装并可执行。")
            print(f"如果文件仍过大，可以尝试更强的压缩设置（如在代码中将 /ebook 改为 /screen），但这会降低文档质量。")
