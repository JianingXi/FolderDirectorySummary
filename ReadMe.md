
# Directory Summary Script

This script generates a summary of the contents of a specified directory and saves it to a text file.

这个脚本生成指定目录内容的摘要，并将其保存到文本文件中。

## Features

- Lists all files and directories in the specified directory.
- Saves the summary to a text file.
- 简单易用，只需指定目录路径。

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    克隆仓库：

    ```sh
    git clone https://github.com/yourusername/directory-summary-script.git
    cd directory-summary-script
    ```

2. Install any required Python packages:

    安装所需的Python包：

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Modify the script to specify the directory you want to summarize:

    修改脚本以指定要生成摘要的目录：

    ```python
    folder_path = r'C:\path\to\your\directory'
    ```

2. Run the script:

    运行脚本：

    ```sh
    python get_directory_summary_txt.py
    ```

3. The summary will be saved to `directory_summary.txt` in the specified directory.

    摘要将保存到指定目录中的 `directory_summary.txt` 文件。

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
    directory_path = r'C:\path\to\your\directory'  # 修改为你的目录路径
    summary_file_path = os.path.join(directory_path, 'directory_summary.txt')
    summary = get_directory_summary(directory_path)
    save_summary_to_file(summary, summary_file_path)
    print(f"Directory summary saved to {summary_file_path}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 许可证

这个项目是根据MIT许可证授权的 - 详见[LICENSE](LICENSE)文件。
