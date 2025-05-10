import os
import glob
import pandas as pd

def clean_empty_rows_in_excel(folder_path):
    # 找到文件夹中所有 .xlsx 文件
    pattern = os.path.join(folder_path, '*.xlsx')
    files = glob.glob(pattern)

    for file_path in files:
        print(f'Processing {file_path}...')
        # 读取所有 sheet
        xls = pd.read_excel(file_path, sheet_name=None, dtype=str)

        # 用于保存清理后的各 sheet
        cleaned_sheets = {}

        for sheet_name, df in xls.items():
            # 去除全为空的行
            df_clean = df.dropna(axis=0, how='all')
            # 可选：如果想去除“全为空字符串”的行，可以先将空字符串视为 NaN
            df_clean = df_clean.replace(r'^\s*$', pd.NA, regex=True).dropna(axis=0, how='all')
            cleaned_sheets[sheet_name] = df_clean

        # 将清理后的结果写回到同一个文件（覆盖原文件）
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            for sheet_name, df_clean in cleaned_sheets.items():
                df_clean.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f'  → Done. Empty rows removed.')

if __name__ == '__main__':
    folder = r'C:\Users\xijia\Desktop\summary'
    clean_empty_rows_in_excel(folder)
