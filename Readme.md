# 🖼️ Image to Text Converter using Selenium & Google Search

This Python script automates the process of converting an image to text using **Google Search** and **Selenium**. It simulates uploading an image to Google and retrieves the detected text.

## 🚀 Features

* Automates Chrome using Selenium
* Uses Google search to detect text in images (OCR via Google Lens)
* Copies extracted text to your clipboard

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

`requirements.txt` should contain:

```
pyperclip==1.9.0
selenium==4.34.0
webdriver-manager==4.0.2
```

## 🛠️ Usage

1. Activate your virtual environment:

```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Run the script:

```bash
python image_to_text.py
```

3. When prompted, provide the image path. The detected text will be automatically copied to your clipboard.

## 💡 Notes

* Make sure Chrome is installed on your system.
* The script uses `webdriver-manager` to auto-install the correct version of ChromeDriver.