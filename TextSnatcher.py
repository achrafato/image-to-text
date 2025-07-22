from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import random
import tempfile
import os
import pyperclip


first_call = True

def create_stealth_driver():
    """Create a Chrome driver with anti-detection measures"""
    options = Options()
    
    # Basic stealth options
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # User agent spoofing
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    # Disable webdriver detection
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    
    # Use unique user data directory
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={temp_dir}')
    
    # Additional privacy options
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-plugins')
    options.add_argument('--disable-images')  # Faster loading
    options.add_argument('--disable-javascript')  # Optional: disable JS
    
    # Create driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Execute script to remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver, temp_dir



def human_like_delay(min_delay=1, max_delay=3):
    """Add random human-like delays"""
    time.sleep(random.uniform(min_delay, max_delay))




def main(file_path, driver, temp_dir):
    # driver, temp_dir = create_stealth_driver()
    
    try:
        # Navigate to Google Images
        # global first_call

        # if first_call :
        #     driver.get('https://images.google.com/')
        #     human_like_delay(2, 4)
        #     first_call = False
    
        wait = WebDriverWait(driver, 5)
        # Method 1: Try to find camera button with multiple selectors
        camera_selectors = [
            "a[aria-label*='camera']",
            ".nDcEnd",
            "[data-ved*='camera']",
            "a[title*='camera']",
            ".XWrYL"
        ]
        
        camera_clicked = False
        for selector in camera_selectors:
            try:
                camera_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                camera_btn.click()
                camera_clicked = True
                print("Camera button clicked successfully")
                break
            except:
                continue
        
        if not camera_clicked:
            print("Could not find camera button, trying alternative method...")

            # Alternative: Use keyboard shortcut
            from selenium.webdriver.common.keys import Keys
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
        
        human_like_delay(2, 3)
        
        # Try to find upload button with multiple selectors
        upload_selectors = [
            "input[type='file']",
            "input[name='encoded_image']",
            ".DV7the input",
            "[accept*='image'] input"
        ]
        
        upload_clicked = False
        for selector in upload_selectors:
            try:
                upload_btn = driver.find_element(By.CSS_SELECTOR, selector)
                upload_btn.send_keys(file_path)
                upload_clicked = True
                print("Image uploaded successfully")
                break
            except:
                continue
        
        if not upload_clicked:
            print("Could not find upload button")
        
        # Wait for results
        human_like_delay(5, 8)



        # select text
        MAX_RETRIES = 3

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                select_Text = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[3]/div[1]/div/c-wiz/div/div[1]/div[3]/div/div/div/button'))
                )
                select_Text.click()
                break  # ✅ success, break the loop
            except TimeoutException as e:
                print(f"[Attempt {attempt}] Element not found or not clickable.")
                if attempt == MAX_RETRIES:
                    d1_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "XWrYL")))
                    d1_element.click()
                    raise Exception("❌ Failed after 3 retries.")
        # select_Text = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[3]/div[1]/div/c-wiz/div/div[1]/div[3]/div/div/div/button')))
        # select_Text.click()

        human_like_delay(2, 5)
        
        # copy button
        copy_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[3]/div[1]/div/c-wiz/div/div[1]/div[3]/div/div/div[1]/button')))
        copy_btn.click()

        d1_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "XWrYL")))
        d1_element.click()

        human_like_delay(2, 4)




        # # Optional: Extract results
        # try:
        #     results = driver.find_elements(By.CSS_SELECTOR, ".g img")
        #     print(f"Found {len(results)} similar images")
        # except:
        #     pass
            
    except Exception as e:
        print(f"Error: {e}")
    
    # finally:
    #     driver.quit()
    #     # Clean up temp directory
    #     try:
    #         import shutil
    #         shutil.rmtree(temp_dir)
    #     except:
    #         pass


# driver = None
# temp_dir = None

if __name__ == "__main__":
    
    global driver, temp_dir
    folder_path = "/home/sak/Desktop/python_proj/pics"

    driver, temp_dir = create_stealth_driver()
    
    driver.get('https://images.google.com/')
    human_like_delay(2, 4)
    wait = WebDriverWait(driver, 15)

    for filename in sorted(os.listdir(folder_path)):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            main(full_path, driver, temp_dir)
            clipboard_text = pyperclip.paste()

            # Append clipboard content to the file
            with open("output.txt", "a") as file:
                file.write(clipboard_text + "\n\n\n\n\n\n")