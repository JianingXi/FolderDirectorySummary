import os

def summarize_text_file(file_path, num_lines=5):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='gbk') as file:
            lines = file.readlines()
    summary = ''.join(lines[:num_lines])
    return summary

def summarize_image_file(file_path):
    # For simplicity, we'll just return the file name for image files
    return f"Image file: {file_path}"

def generate_folder_summary(folder_path, num_lines=5):
    folder_summary = []
    for root, dirs, files in os.walk(folder_path):
        folder_summary.append(f"Directory: {root}")
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.endswith(".txt") or filename.endswith(".docx"):
                summary = summarize_text_file(file_path, num_lines)
            elif filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                summary = summarize_image_file(file_path)
            else:
                summary = f"File: {filename} (type not summarized)"
            folder_summary.append(f"  {filename}: {summary}")
    return "\n".join(folder_summary)

# 使用原始字符串
folder_path = r'C:\Users\xijia\Desktop\新建文件夹\材料_1图片版'  # 替换为您的文件夹路径

summary = generate_folder_summary(folder_path)

with open('folder_summary.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(summary)

print("Folder summary has been written to 'folder_summary.txt'")
