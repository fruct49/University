import re
import csv
import ssl
import urllib.request

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode()

with open('html.txt', mode='w', encoding='utf8') as file:
    file.write(html_content)

#\s* для удаления лишних пробелов
re_algorithm = r'class="org-widget-header__title-link">\s*([^<]+?)\s*</a>.*?' \
               r'org-widget-header__meta--location">\s*([^<]+?)\s*</span>.*?' \
               r'<dt class="spec__index"><span class="spec__index-inner">Телефон</span></dt>.*?' \
               r'<dd class="spec__value">\s*([^<]+?)\s*</dd>.*?' \
               r'<dt class="spec__index"><span class="spec__index-inner">Часы работы</span></dt>.*?' \
               r'<dd class="spec__value">\s*([^<]+?)\s*</dd>'

# Поиск совпадений по регулярному выражению
matches = re.findall(re_algorithm, html_content, re.DOTALL)

cleaned_matches = [(name.strip(), address.strip(), phone.strip(), hours.strip()) for name, address, phone, hours in matches]

# Запись результатов в CSV-файл с разделителем точка с запятой
with open('output.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')  # Указываем разделитель ";"

    writer.writerow(['Наименование', 'Адрес', 'Телефон', 'Часы работы'])
    #строки данных
    writer.writerows(cleaned_matches)