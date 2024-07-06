
# Directory Summary Script

This script generates a summary of the contents of a specified directory and saves it to a text file.

����ű�����ָ��Ŀ¼���ݵ�ժҪ�������䱣�浽�ı��ļ��С�

## Features

- Lists all files and directories in the specified directory.
- Saves the summary to a text file.
- �����ã�ֻ��ָ��Ŀ¼·����

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ��¡�ֿ⣺

    ```sh
    git clone https://github.com/yourusername/directory-summary-script.git
    cd directory-summary-script
    ```

2. Install any required Python packages:

    ��װ�����Python����

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Modify the script to specify the directory you want to summarize:

    �޸Ľű���ָ��Ҫ����ժҪ��Ŀ¼��

    ```python
    folder_path = r'C:\path\to\your\directory'
    ```

2. Run the script:

    ���нű���

    ```sh
    python get_directory_summary_txt.py
    ```

3. The summary will be saved to `directory_summary.txt` in the specified directory.

    ժҪ�����浽ָ��Ŀ¼�е� `directory_summary.txt` �ļ���

## Code

```python
import os

def get_directory_summary(directory_path):
    summary = []
    for root, dirs, files in os.walk(directory_path):
        summary.append(f"Directory: {root}")
        for dir in dirs:
            summary.append(f"  Subdirectory: {dir}")
        for file in files:
            summary.append(f"  File: {file}")
    return "\n".join(summary)

def save_summary_to_file(summary, file_path):
    with open(file_path, 'w') as file:
        file.write(summary)

if __name__ == "__main__":
    directory_path = r'C:\path\to\your\directory'  # �޸�Ϊ���Ŀ¼·��
    summary_file_path = os.path.join(directory_path, 'directory_summary.txt')
    summary = get_directory_summary(directory_path)
    save_summary_to_file(summary, summary_file_path)
    print(f"Directory summary saved to {summary_file_path}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ���֤

�����Ŀ�Ǹ���MIT���֤��Ȩ�� - ���[LICENSE](LICENSE)�ļ���
