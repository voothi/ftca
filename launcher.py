import sys
import base64
import subprocess
import os

# Путь к вашему браузеру Chrome. Измените, если он у вас в другом месте.
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def main():
    # Проверяем, был ли передан текст в качестве аргумента
    if len(sys.argv) > 1:
        # Берем весь текст из первого аргумента
        original_text = sys.argv[1]
        
        # Кодируем текст в байты UTF-8, затем в Base64
        text_bytes = original_text.encode('utf-8')
        base64_bytes = base64.b64encode(text_bytes)
        base64_string = base64_bytes.decode('utf-8')
        
        # Формируем URL с новым параметром s_b64
        url = f'http://127.0.0.1:5010/?clipboard=true&multiline=true&s_b64={base64_string}'
        
        # Проверяем, существует ли Chrome по указанному пути
        if not os.path.exists(CHROME_PATH):
            print(f"Ошибка: Не удалось найти Chrome по пути: {CHROME_PATH}")
            print("Пожалуйста, исправьте путь в переменной CHROME_PATH в скрипте launcher.py")
            # Даем пользователю время прочитать ошибку
            input("Нажмите Enter для выхода...")
            return

        # Запускаем Chrome с новым URL
        subprocess.run([CHROME_PATH, url])
    else:
        print("Текст для обработки не был передан.")

if __name__ == '__main__':
    main()