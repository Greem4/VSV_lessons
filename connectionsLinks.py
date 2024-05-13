import os
import re

# Укажите корневой путь к вашим урокам
root_path = '/home/greem/yaDisk/VSV_lessons/lessons/'

# Получаем список всех папок в директории 'lessons'
lesson_folders = sorted([d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))], key=lambda x: float('0' + re.sub('[^0-9.]', '', x)))

# Функция для создания Markdown ссылки
def create_markdown_link(target_md_file):
    # Создаем Markdown ссылку
    return f"\n\n[Next Lesson](../{target_md_file})\n"

# Проверяем, существует ли ссылка на следующий урок в файле
def link_exists(md_file_content, target_md_file):
    link = create_markdown_link(target_md_file).strip()
    return link in md_file_content

# Обходим каждую папку и добавляем ссылку на файл в следующей папке
for i, folder in enumerate(lesson_folders[:-1]):  # Последняя папка не имеет следующей, поэтому исключаем ее
    # Получаем список файлов .md в текущей папке
    md_files = [f for f in os.listdir(os.path.join(root_path, folder)) if f.endswith('.md')]
    if md_files:
        # Берем первый .md файл в папке
        current_md_file_path = os.path.join(root_path, folder, md_files[0])
        # Получаем следующую папку и первый .md файл в ней
        next_folder = lesson_folders[i + 1]
        next_md_files = [f for f in os.listdir(os.path.join(root_path, next_folder)) if f.endswith('.md')]
        if next_md_files:
            # Создаем путь к следующему .md файлу
            next_md_file = os.path.join(next_folder, next_md_files[0])
            # Читаем текущий .md файл и проверяем, существует ли уже ссылка
            with open(current_md_file_path, 'r+') as md_file:
                content = md_file.read()
                if not link_exists(content, next_md_file):
                    # Если ссылки нет, добавляем ее в конец файла
                    md_file.write(create_markdown_link(next_md_file))