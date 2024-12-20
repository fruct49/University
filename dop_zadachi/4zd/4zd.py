import re
import csv
import urllib.request

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
html_content = urllib.request.urlopen(url).read().decode()

pattern = (
    r'class="org-widget-header__title-link">([^<]+)</a>.*?'
    r'org-widget-header__meta--location">([^<]+)</span>.*?'
    r'<dd class="spec__value">([^<]+)</dd>.*?'
    r'<dd class="spec__value">([^<]+)</dd>'
)


matches = re.findall(pattern, html_content, re.DOTALL)

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Наименование', 'Адрес', 'Телефон', 'Часы работы'])
    writer.writerows(matches)
