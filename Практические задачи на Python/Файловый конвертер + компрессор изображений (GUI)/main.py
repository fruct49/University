import os
import shutil
from pathlib import Path
from PIL import Image
from pdf2docx import Converter
from docx.api import Document


def display_menu():
    print("\nВыберите действие:")
    print("0. Сменить рабочий каталог")
    print("1. Преобразовать PDF в DOCX")
    print("2. Преобразовать DOCX в PDF")
    print("3. Произвести сжатие изображений")
    print("4. Удалить группу файлов")
    print("5. Выход")


def change_working_directory():
    new_dir = input("Введите путь к новому рабочему каталогу: ")
    if os.path.isdir(new_dir):
        os.chdir(new_dir)
        print(f"Рабочий каталог изменен на: {new_dir}")
    else:
        print("Указанный путь не существует.")


def convert_pdf_to_docx():
    pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]
    if not pdf_files:
        print("PDF-файлы не найдены в текущем каталоге.")
        return

    for pdf_file in pdf_files:
        output_docx = pdf_file.replace('.pdf', '.docx')
        try:
            converter = Converter(pdf_file)
            converter.convert(output_docx, start=0, end=None)
            converter.close()
            print(f"Конвертация {pdf_file} в {output_docx} завершена.")
        except Exception as e:
            print(f"Ошибка при конвертации {pdf_file}: {e}")


def convert_docx_to_pdf():
    docx_files = [f for f in os.listdir() if f.endswith('.docx')]
    if not docx_files:
        print("DOCX-файлы не найдены в текущем каталоге.")
        return

    for docx_file in docx_files:
        output_pdf = docx_file.replace('.docx', '.pdf')
        try:
            # Псевдокод, поскольку docx-to-pdf не реализуется напрямую стандартными библиотеками
            print(f"Конвертация {docx_file} в {output_pdf} завершена. (реализуйте с подходящей библиотекой)")
        except Exception as e:
            print(f"Ошибка при конвертации {docx_file}: {e}")


def compress_images():
    image_files = [f for f in os.listdir() if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    if not image_files:
        print("Изображения не найдены в текущем каталоге.")
        return

    for image_file in image_files:
        try:
            img = Image.open(image_file)
            img.save(image_file, optimize=True, quality=70)
            print(f"Сжатие {image_file} завершено.")
        except Exception as e:
            print(f"Ошибка при сжатии {image_file}: {e}")


def delete_files():
    file_extension = input("Введите расширение файлов для удаления (например, .txt): ")
    files_to_delete = [f for f in os.listdir() if f.endswith(file_extension)]

    if not files_to_delete:
        print(f"Файлы с расширением {file_extension} не найдены.")
        return

    for file in files_to_delete:
        os.remove(file)
        print(f"Файл {file} удален.")


def main():
    print(f"Текущий рабочий каталог: {os.getcwd()}")

    while True:
        display_menu()
        choice = input("Введите номер действия: ")

        if choice == "0":
            change_working_directory()
        elif choice == "1":
            convert_pdf_to_docx()
        elif choice == "2":
            convert_docx_to_pdf()
        elif choice == "3":
            compress_images()
        elif choice == "4":
            delete_files()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
