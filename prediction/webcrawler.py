from __future__ import print_function
from os.path import join, dirname, abspath


from html.parser import HTMLParser
import urllib.request
import xlrd

from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf # http://pypi.python.org/pypi/xlwt

def import_data():
    fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_by_index(0)
    countdata = sheet.nrows
    return (sheet.cell_value(countdata-1,0))




def update(d,g,n,o,u):

    fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
    rb = xlrd.open_workbook(fname)#read garney object
    r_sheet = rb.sheet_by_index(0)#read garney in sheet by index 0
    r = r_sheet.nrows#geting the rows in r_sheet
    wb = copy(rb)#write garney object
    sheet = wb.get_sheet(0)#write garna lai sheet 0 liney
    sheet.write(r+1, 0, d)
    sheet.write(r+1, 1, g)
    sheet.write(r+1, 2, n)
    sheet.write(r+1, 3, o)
    sheet.write(r+1, 4, u)
    print("---------------")
    print(r)

    print(d)

    wb.save('/home/shruti/major project/FOREX/trainingdata.xls')
    print("done saving");
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

print ("Extracting the data from investing.com for fundamental analysis....")

target = 'https://www.investing.com/commodities/gold-historical-data'
req = urllib.request.Request(url=target, data=None, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')#xhtml ma page ko bhahye bhar ko data aunxa
# instantiate the parser and feed it
p = HTMLTableParser()#p is an instance of htmltableparser
p.feed(xhtml)#giving every parsed to p
print("p-----")
print(p)
a=p.tables#page bata tables nikalaney
print("a========")
print(a)
print ("Extracted data from investing.com....")
print("Date.........")
new_date = a[3][1][0]
print(new_date)
print("Gold.......")
print( a[3][1][1])
new_gold = a[3][1][1]
a = new_gold.replace(',', '')
ab = float(a)
new_gold = ab

store_date = import_data()#last date auncha of stored table coz xa bhanney check garnu pardaina feri ..tei dekhaunney ho
print("store_date")
print(store_date)

target = 'https://www.investing.com/currencies/usd-npr-historical-data'
req = urllib.request.Request(url=target, data=None, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')
# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
a=p.tables
print("USD/NPR.......")
print( a[2][1][1])
new_usd = a[2][1][1]
a = new_usd.replace(',', '')
ab = float(a)
new_usd = ab

target = 'https://www.investing.com/commodities/crude-oil-historical-data'
req = urllib.request.Request(url=target, data=None, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')

# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
a=p.tables
print("Oil.......")
print( a[3][1][1])
new_oil = a[3][1][1]
a = float(new_oil)
a = new_oil.replace(',', '')
ab = float(a)
new_oil = ab

target = 'https://www.investing.com/indices/nq-100-historical-data'
req = urllib.request.Request(url=target, data=None, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')

# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
a=p.tables
print("Nasdaq.......")
print( a[2][1][1])
new_nasdaq = a[2][1][1]
a = new_nasdaq.replace(',', '')
ab = float(a)
new_nasdaq = ab



check = 0
if (store_date == new_date):
    print("Fine. Don't need to extract data..")
else:
    print("Need to extract data and store..")
    update(new_date, new_gold, new_nasdaq, new_oil, new_usd)
    check = 1

class abc:
    def check1(self):
        return new_date




















