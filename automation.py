
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import zipfile
import os
from pathlib import Path

extract_to_path = Path("D:/test")

def get_existing_files():
    """Returns a snapshot of files in the extraction folder."""
    file_snapshot = {}
    for file in extract_to_path.glob("*"):
        if file.is_file():
            file_snapshot[file.name] = file.stat().st_mtime
    return file_snapshot

def process_project(driver, project_xpath):
    """Automates the task for a specific project."""
    try:
        # Hover over the project to reveal "View Project" button
        project_element = driver.find_element(By.XPATH, project_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(project_element).perform()
        time.sleep(1)  # Allow time for visibility

        # Click "View Project"
        project_element.click()
        time.sleep(2)

        # Switch to the GitHub tab
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)

        # Click on <>code button
        code_button = driver.find_element(By.XPATH, "//*[@id=':R55ab:']")
        code_button.click()
        time.sleep(1)

        # Click on "Download ZIP" button
        download_button = driver.find_element(By.XPATH, "//*[@id=':re:--label']")
        download_button.click()
        time.sleep(10)  # Wait for the download to complete

        # Detect and extract the ZIP file
        downloads_folder = Path.home() / "Downloads"
        zip_files = list(downloads_folder.glob("*.zip"))
        if zip_files:
            latest_zip = max(zip_files, key=os.path.getctime)
            extract_zip(latest_zip)
        else:
            raise FileNotFoundError("No ZIP file found!")

        # Close the GitHub tab and return to the main portfolio page
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        raise Exception(f"Error while processing project: {e}")

def extract_zip(zip_file_path):
    """Extracts the ZIP file into the target folder."""
    try:
        # Ensure the target folder exists
        extract_to_path.mkdir(parents=True, exist_ok=True)

        # Extract ZIP file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_path)
    except Exception as e:
        raise Exception(f"Extraction failed: {e}")

def run_task():
    """Runs the automation task for both projects."""
    try:
        status_label.config(text="Processing...")
        root.update()

        # Set up Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)

        # Open Portfolio Website
        driver.get("https://portfolio-f7afe.web.app/")
        time.sleep(2)

        # Click "Projects"
        projects_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Projects')]")
        projects_button.click()
        time.sleep(2)

        # Process Project 1
        process_project(driver, "//*[@id='projects']/div[2]/div/div[1]/div/div/a")

        # Return to Portfolio Page
        driver.get("https://portfolio-f7afe.web.app/")
        time.sleep(2)

        # Process Project 2
        process_project(driver, "//*[@id='projects']/div[2]/div/div[2]/div/div/a")

        # Quit the browser
        driver.quit()

        # Update the GUI status
        status_label.config(text="Process Completed!")
        root.update()

    except Exception as e:
        status_label.config(text="An error occurred!")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setting up Tkinter GUI
root = tk.Tk()
root.title("Automated Project Downloader")
root.geometry("500x300")

status_label = tk.Label(root, text="Ready", font=("Helvetica", 12))
status_label.pack(pady=20)

run_button = tk.Button(root, text="Start Automation", font=("Helvetica", 12), command=run_task)
run_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=root.quit)
exit_button.pack(pady=20)

root.mainloop()