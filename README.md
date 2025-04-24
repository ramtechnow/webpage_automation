# Automated Project Downloader & Extractor

## 📌 Description
This project automates the process of **navigating a portfolio website, selecting projects, downloading ZIP files from GitHub, extracting them**, and tracking newly added or modified files. It uses **Selenium for automation** and **Tkinter for GUI interaction**, ensuring an effortless workflow.

## ✨ Features
- **Fully Automated Web Navigation** (Selenium-based)
- **ZIP File Download & Extraction** (`D:\test` folder)
- **Automated Dependency Installation** (via `setup.bat`)
- **Real-Time File Tracking** (detects newly added or updated files)

## 🛠 Requirements
- **Python 3.8+**
- **Google Chrome** (latest version)
- **ChromeDriver** (matching your Chrome version)
- **Required Python Packages**:
  - `selenium` (Web Automation)
  - `zipfile` (ZIP Extraction)
  - `tkinter` (Graphical Interface)

## 🚀 Installation Guide
### Step 1: Clone the Repository
```bash
gh repo clone ramtechnow/webpage_automation
cd webpage_automation
```

### Step 2: Install Dependencies (Automated)
Run the batch file to install required pip packages:
```bash
setup.bat
```
OR install manually:
```bash
pip install selenium
```

### Step 3: Setup ChromeDriver
Download the compatible version:
- [ChromeDriver Download](https://sites.google.com/a/chromium.org/chromedriver/)
- Place `chromedriver.exe` in the **same folder** as the script OR ensure it's accessible via PATH.

### Step 4: Run the Automation
Start the automation by running:
```bash
python automated_project_downloader.py
```
- The GUI will appear.
- Click **Start Automation**, and the process will handle everything automatically.
- Once both projects are processed, the label will display `"Process Completed!"`.

### Step 5: Verify Extracted Files
All files will be **automatically extracted** into `D:\test`  
Check the folder to confirm new files.

## 🔄 Project Workflow
1. **Navigate to Portfolio Website** → Opens the page.
2. **Click "Projects"** → Selects projects.
3. **Download ZIP Files** → Navigates to GitHub, clicks `<code>` and downloads ZIP.
4. **Extract Files** → Automatically extracts files into `D:\test`.
5. **Track New Files** → Detects updates.

## 🤝 Contributing
- Fork the repository.
- Submit pull requests.
- Open issues for improvements!

## 📜 License
This project is licensed under the **MIT License**.

## 👤 Author
Created by **Shriram M G**  
Feel free to contact at [https://portfolio-f7afe.web.app/](mailto:ramtechnow@gmail.com).
