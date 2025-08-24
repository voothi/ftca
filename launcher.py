import sys
import base64
import subprocess
import os

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def main():
    if len(sys.argv) > 1:
        original_text = sys.argv[1]
        
        text_bytes = original_text.encode('utf-8')
        base64_bytes = base64.b64encode(text_bytes)
        base64_string = base64_bytes.decode('utf-8')
        
        url = f'http://127.0.0.1:5010/?clipboard=true&multiline=true&s_b64={base64_string}'
        
        if not os.path.exists(CHROME_PATH):
            print(f"Error: Could not find Chrome at path: {CHROME_PATH}")
            print("Please correct the path in the CHROME_PATH variable in the launcher.py script")
            input("Press Enter to exit...")
            return

        subprocess.run([CHROME_PATH, url])
    else:
        print("No text was provided for processing.")

if __name__ == '__main__':
    main()