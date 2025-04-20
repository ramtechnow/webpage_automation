# Automated Project Downloader and Extractor

## Description
This project provides a **fully automated solution** for downloading and extracting ZIP files from a portfolio website. It uses **Selenium WebDriver** for automation and **Python’s Tkinter** module to offer a GUI for user interaction. The extracted files are managed in a specified folder (`D:\test`), ensuring seamless handling and tracking of new and modified files.

## Features
- **Automated Web Navigation**: Uses Selenium to interact with the portfolio website, select projects, and download ZIP files.
- **ZIP File Extraction**: Extracts downloaded ZIP files into the `D:\test` folder.
- **File Update Tracking**: Detects and reports new or modified files in the target folder after extraction.
- **GUI Integration**: Provides a simple Tkinter-based interface for initiating the automation and monitoring progress.
- **Error Handling**: Displays meaningful messages in case of failures.

## Requirements
- Python 3.8+
- **Dependencies**:
  - `selenium`: For web automation
  - `tkinter`: For GUI
  - `zipfile`: To handle ZIP file extraction
- **Browser**:
  - Google Chrome (latest version)
  - ChromeDriver (compatible with your Chrome version)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/project-downloader.git
   cd project-downloader
   ```
2. Install dependencies:
   ```bash
   pip install selenium
   ```
3. Ensure ChromeDriver is installed and added to your PATH:
   - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

## Usage
1. Run the script:
   ```bash
   python automated_project_downloader.py
   ```
2. The GUI will appear. Click **Start Automation** to begin the process.
3. All files will be downloaded and extracted into the `D:\test` folder. The GUI will display a "Process Completed!" message upon completion.

## Project Workflow
1. **Navigate to the Portfolio Website**: Opens the portfolio page.
2. **Click Projects**: Interacts with project links using Selenium.
3. **Download ZIP Files**: Clicks the `<>code` button and downloads ZIP files.
4. **Extract Files**: Unzips files into `D:\test`, ensuring new or modified files are tracked.
5. **Track Updates**: Reports new additions or modifications to extracted files.

## Contributing
Feel free to fork the repository and submit pull requests for enhancements or bug fixes. All contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
Created by **Your Name**. For inquiries, email at [ramtechnow@gmail.com](ramtechnow@gmail.com).
```
