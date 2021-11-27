import re
import csv
import collections


class Regex:
    def __init__(self):
        self.contacts_list = []

    def open_data(self, filename):
        with open(filename, encoding="utf-8") as f:
            rows = csv.reader(f, delimiter=",")
            self.contacts_list = list(rows)

    def prepare_data(self):
        for el in self.contacts_list:
            del el[7:]

    def reg_fio(self):
        for el in self.contacts_list:
            full_name = el[0] + ' ' + el[1] + ' ' + el[2]
            sent_list = re.split(r'\s+', full_name)
            if "" in sent_list and len(sent_list) > 3:
                sent_list.remove("")
            el[0], el[1], el[2] = sent_list[0], sent_list[1], sent_list[2]

    def dell_double(self):
        prepare_to_del = []
        for num1, el in enumerate(self.contacts_list):
            double = []
            if num1 not in prepare_to_del:
                num2 = num1 + 1
                for elem in self.contacts_list[num2:]:
                    if el[0] + el[1] == elem[0] + elem[1]:
                        double.append(elem)
                        num2 += 1
                        prepare_to_del.append(num2)
                        if len(double) > 0:
                            for row in double:
                                for num3, call in enumerate(row):
                                    if len(el[num3]) < len(call):
                                        el[num3] = call
        for i in prepare_to_del[:-1]:
            del self.contacts_list[i]

    def reg_phone(self, pattern, sub):
        for el in self.contacts_list:
            result = pattern.sub(sub, el[5])
            el[5] = result

    def save_data(self, final_filename):
        with open(final_filename, "w", newline='') as f:
            dw = csv.writer(f, delimiter=',')
            dw.writerows(self.contacts_list)


if __name__ == '__main__':
    pattern1 = re.compile(r"(\+7|8)?\s?\(?(\d{3})\)?\s*-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s?\(?(доб\.)\s?(\d{4})\)?)?")
    sub1 = r"+7(\2)\3-\4-\5 \7\8"
    a = Regex()
    a.open_data('data.csv')
    a.prepare_data()
    a.reg_fio()
    a.dell_double()
    a.reg_phone(pattern1, sub1)
    a.save_data('phonebook.csv')
