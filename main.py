import re
from pprint import pprint
import csv
r = r'(\+7|8)?\s?\(?(\d{3})\)?\s*-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s?\(?(доб\.)\s?(\d{4})\)?)?'
sub = r'+7(\2)-\3-\4-\5 \7\8'

with open("data.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

del contacts_list[0]

for el in contacts_list:
    full_name = el[0] + ' ' + el[1] + ' ' + el[2]
    sent_list = re.split(r'\s+', full_name)
    if "" in sent_list and len(sent_list) > 3:
        sent_list.remove("")
    el[0], el[1], el[2] = sent_list[0], sent_list[1], sent_list[2]


for num, el in enumerate(contacts_list):
    double = []
    for elem in contacts_list[num + 1:]:
        if el[0] + el[1] == elem[0] + elem[1]:
            double.append(elem)
    if len(double) > 0:
        pprint(double)






s = '''
делаем энемерате !!!
бахаем вайл от нашего индекса и до конца!!!
если находим мач то апендим в промеж список и удаляем из первичного списка!!!
сравниваем значения из нашей похиции со значениями из промеж списка по длинее??? по нул? по ''? !!!
оставляем то что пизже'''



# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
