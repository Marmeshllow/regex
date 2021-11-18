import re
import csv

pattern = re.compile(r"(\+7|8)?\s?\(?(\d{3})\)?\s*-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s?\(?(доб\.)\s?(\d{4})\)?)?")
sub = r"+7(\2)\3-\4-\5 \7\8"

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

prepare_to_del = []
for num1, el in enumerate(contacts_list):
    double = []
    if num1 not in prepare_to_del:
        num2 = num1 + 1
        for elem in contacts_list[num2:]:
            if el[0] + el[1] == elem[0] + elem[1]:
                double.append(elem)
                num2 += 1
                prepare_to_del.append(num2)
        if len(double) > 0:
            for row in double:
                for num3, call in enumerate(row):
                    if len(el[num3]) < len(call):
                        el[num3] = call

for i in prepare_to_del[::-1]:
    del contacts_list[i]
print(contacts_list)
print(prepare_to_del)

for el in contacts_list:
    result = pattern.sub(sub, el[5])
    el[5] = result
print(contacts_list)

with open("phonebook.csv", "w", newline='') as f:
    dw = csv.writer(f, delimiter=',')
    dw.writerows(contacts_list)
