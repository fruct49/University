import os
import PySimpleGUI as sg
from pathlib import Path
from PIL import Image
from pdf2docx import Converter
from docx.api import Document

def compress_image(file_path):
    try:
        img = Image.open(file_path)
        img.save(file_path, optimize=True, quality=70)
        return f"Сжатие {file_path} завершено."
    except Exception as e:
        return f"Ошибка при сжатии {file_path}: {e}"

def convert_pdf_to_docx(file_path):
    output_docx = file_path.replace('.pdf', '.docx')
    try:
        converter = Converter(file_path)
        converter.convert(output_docx, start=0, end=None)
        converter.close()
        return f"Конвертация {file_path} в {output_docx} завершена."
    except Exception as e:
        return f"Ошибка при конвертации {file_path}: {e}"

def convert_docx_to_pdf(file_path):
    output_pdf = file_path.replace('.docx', '.pdf')
    try:
        subprocess.run([
            "libreoffice", "--headless", "--convert-to", "pdf", file_path
        ], check=True)
        return f"Конвертация {file_path} в {output_pdf} завершена."
    except subprocess.CalledProcessError as e:
        return f"Ошибка при конвертации {file_path}: {e}"
    except FileNotFoundError:
        return "LibreOffice не установлен. Установите его для использования этой функции."

def process_files(selected_files):
    results = []
    for file_path in selected_files:
        if file_path.endswith('.pdf'):
            results.append(convert_pdf_to_docx(file_path))
        elif file_path.endswith('.docx'):
            results.append(convert_docx_to_pdf(file_path))
        elif file_path.lower().endswith(('png', 'jpg', 'jpeg')):
            results.append(compress_image(file_path))
        else:
            results.append(f"Файл {file_path} не поддерживается для операций.")
    return results

def main():
    sg.theme("LightBlue")

    layout = [
        [sg.Text("Выберите папку:"), sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Text("Файлы в папке:")],
        [sg.Listbox(values=[], size=(60, 20), select_mode=sg.SELECT_MODE_EXTENDED, key="-FILE LIST-")],
        [sg.Button("Обновить"), sg.Button("Выполнить"), sg.Button("Выход")],
        [sg.Output(size=(80, 20))]
    ]

    window = sg.Window("Графический интерфейс приложения", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Выход":
            break

        if event == "Обновить":
            folder = values["-FOLDER-"]
            if os.path.isdir(folder):
                files = os.listdir(folder)
                file_list = [
                    f for f in files
                    if f.lower().endswith(('.pdf', '.docx', '.png', '.jpg', '.jpeg'))
                ]
                window["-FILE LIST-"].update(file_list)
            else:
                sg.popup("Выберите существующую папку.")

        if event == "Выполнить":
            selected_files = values["-FILE LIST-"]
            if not selected_files:
                sg.popup("Выберите файлы для выполнения действий.")
                continue


            folder = values["-FOLDER-"]
            full_paths = [os.path.join(folder, f) for f in selected_files]

            results = process_files(full_paths)
            for result in results:
                print(result)

    window.close()

if __name__ == "__main__":
    main()
