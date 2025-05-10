import os
import glob
import pandas as pd

def excel_sheets_to_txt(folder_path, output_txt_path):
    """
    遍历指定文件夹下所有 Excel 文件，将每个文件的所有 sheet 内容拼接到一个大 TXT 文件中。
    """
    # 查找所有 .xlsx 和 .xls 文件
    excel_files = glob.glob(os.path.join(folder_path, '*.xlsx')) + glob.glob(os.path.join(folder_path, '*.xls'))
    with open(output_txt_path, 'w', encoding='utf-8') as out_f:
        for file_path in excel_files:
            file_name = os.path.basename(file_path)
            # 读取所有 sheet
            xls = pd.ExcelFile(file_path, engine='openpyxl')
            for sheet_name in xls.sheet_names:
                # 读取该 sheet 为 DataFrame
                df = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)
                # 写入分隔标题
                out_f.write(f'===== 文件: {file_name} | 工作表: {sheet_name} =====\n')
                # 将 DataFrame 写入 TXT，用制表符分隔
                df.to_csv(out_f, sep='\t', index=False, header=True)
                out_f.write('\n\n')  # 每个 sheet 之间空两行

if __name__ == '__main__':
    folder = r'C:\Users\xijia\Desktop\summary'
    output = r'C:\Users\xijia\Desktop\summary\merged.txt'
    excel_sheets_to_txt(folder, output)
    print(f'已将所有 Excel sheet 内容合并至：{output}')
