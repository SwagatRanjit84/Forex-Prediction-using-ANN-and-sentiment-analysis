from __future__ import print_function
from os.path import join, dirname, abspath


import xlrd
import xlwt
from xlutils.copy import copy



from html.parser import HTMLParser
import urllib.request
import xlrd

from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf # http://pypi.python.org/pypi/xlwt

def import_data():
    fname = join(dirname(dirname(abspath(__file__))), 'backpropagation', 'technicaldata.xls')
    workbook = xlrd.open_workbook(fname)

    sheet = workbook.sheet_by_index(0)
    countdata = sheet.nrows
    return (sheet.cell_value(countdata-1,0))




def update(new_date, low1, open1, high1,close1):
    fname = join(dirname(dirname(abspath(__file__))), 'backpropagation', 'technicaldata.xls')
    rb = xlrd.open_workbook(fname)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(r, 0, new_date)
    sheet.write(r, 1, low1)
    sheet.write(r, 2, open1)
    sheet.write(r, 3, high1)
    sheet.write(r, 4, close1)

    wb.save('C:/Users/Swechya/PycharmProjects/voting/backpropagation/technicaldata.xls')
    rb.release_resources()
    del rb


class HTMLTableParser(HTMLParser):
    def __init__(
            self,
            decode_html_entities=False,
            data_separator=' ',
    ):

        HTMLParser.__init__(self)

        self._parse_html_entities = decode_html_entities
        self._data_separator = data_separator

        self._in_td = False
        self._in_th = False
        self._current_table = []
        self._current_row = []
        self._current_cell = []
        self.tables = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self._in_td = True
        if tag == 'th':
            self._in_th = True

    def handle_data(self, data):
        if self._in_td or self._in_th:
            self._current_cell.append(data.strip())

    def handle_charref(self, name):

        if self._parse_html_entities:
            self.handle_data(self.unescape('&#{};'.format(name)))

    def handle_endtag(self, tag):

        if tag == 'td':
            self._in_td = False
        elif tag == 'th':
            self._in_th = False

        if tag in ['td', 'th']:
            final_cell = self._data_separator.join(self._current_cell).strip()
            self._current_row.append(final_cell)
            self._current_cell = []
        elif tag == 'tr':
            self._current_table.append(self._current_row)
            self._current_row = []
        elif tag == 'table':
            self.tables.append(self._current_table)
            self._current_table = []



store_date = import_data()
print("store_date")
print(store_date)


print ("Extracting the data from investing.com for technical analysis....")

target = 'https://www.investing.com/currencies/usd-npr-historical-data'
req = urllib.request.Request(url=target, data=None, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')
# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
a=p.tables
new_date = a[2][1][0]
print ("Extracted data from investing.com....")
print("Date.........")
print(new_date)


a=p.tables
close = a[2][1][1]
a = close.replace(',', '')
ab = float(a)
close = ab
print("Close USD/NPR.........")
print(close)



a=p.tables
open1 = a[2][1][2]
a = open1.replace(',', '')
ab = float(a)
open1 = ab
print("Open USD/NPR.........")
print(open1)


a=p.tables
high1 = a[2][1][3]
a = high1.replace(',', '')
ab = float(a)
high1 = ab
print("High USD/NPR.........")
print(high1)


a=p.tables
low1 = a[2][1][4]
a = low1.replace(',', '')
ab = float(a)
low1 = ab

print("Low USD/NPR.........")
print(low1)







check = 0
if (store_date == new_date):
    print("Fine. Don't need to extract data..")
else:
    print("Need to extract data and store..")
    update(new_date, low1, open1, high1, close)
    check = 1

class abc:
    def check1(self):
        return new_date













