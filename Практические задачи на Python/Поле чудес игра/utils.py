import os
import random

def load_words(file_path="words.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().splitlines()
            if not words:
                raise ValueError("Файл пустой! Добавьте слова в файл.")
            return words
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except Exception as e:
        raise Exception(f"Произошла ошибка при чтении файла: {e}")

def get_record(file_path="records.txt"):
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            record = file.read()
            return int(record) if record.isdigit() else 0
    except Exception as e:
        print(f"Ошибка при чтении файла рекордов: {e}")
        return 0

def save_record(record, file_path="records.txt"):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(record))
    except Exception as e:
        print(f"Ошибка при записи рекорда: {e}")
