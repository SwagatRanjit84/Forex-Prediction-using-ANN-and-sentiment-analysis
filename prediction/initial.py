from __future__ import print_function
from os.path import join, dirname, abspath

import xlrd
import sqlite3
# import matplotlib
# matplotlib.use('Agg')
# from matplotlib import pyplot as plt

conn = sqlite3.connect('datas32.db')
c123 = conn.cursor()

def create_table():
    c123.execute('CREATE TABLE IF NOT EXISTS datas1(date TEXT, gold REAL,nasdaq REAL,oil REAL,usdnpr REAL,predicted REAL)')


def read_db():
    c123.execute("SELECT * FROM datas1")
    data = c123.fetchall()
    print ("yehi ho data")
    print (data)

def read_all():
    global date12345
    date12345 = []

    m=[]
    fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_by_index(0)
    ee = sheet.nrows-1
    for i in range(1,ee):
        m.append(sheet.cell_value(i, 4))
        date12345.append(sheet.cell_value(i, 0))
    return m



def abc():
    global final_data
    final_data=[]
    fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_by_index(0)
    ee = sheet.nrows-1
    final_data.append( sheet.cell_value(ee, 0))
    final_data.append( sheet.cell_value(ee, 1))
    final_data.append(sheet.cell_value(ee, 2))
    final_data.append(sheet.cell_value(ee, 3))
    final_data.append(sheet.cell_value(ee, 4))
    return final_data

def dynamic_datastore(datas,output,count):
    # i = 1
    j = 1
    for j in range(count):
        c123.execute("INSERT INTO datas1 (date, gold,nasdaq ,oil, usdnpr,predicted) VALUES (?,?,?,?,?,?)", (datas[j][0], datas[j][1],
                                                                                     datas[j][2],datas[j][3],datas[j][4],output[j]))

        # c.execute("INSERT INTO datas1 (date, gold,nasdaq ,usdnpr) VALUES (?,?,?,?)", ('12 may',23.1,221.2,435.3))
        #

    conn.commit()


def import_data():
    global past_data
    past_data = []
    global target
    target = []
    fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
    workbook = xlrd.open_workbook(fname)

    sheet = workbook.sheet_by_index(0)
    list_data = []
    j = 1
    while j < 2000:
        i = 0
        m = []
        while i < 5:
            temp = sheet.cell_value(j+1,i)
            m.append(sheet.cell_value(j,i))

            # print sheet.cell_value(j,i)
            i = i + 1

        j = j + 1
        past_data.append(m)
        list_data.append(m)
        target.append(temp)
    # print list_data
    return list_data



def import_target():
    global counttt
    global target123

    target123 = []
    fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
    workbook = xlrd.open_workbook(fname)
    sheet = workbook.sheet_by_index(0)
    list_data123 = []
    counttt = sheet.nrows
    j = 2000
    while j < counttt-1:
        i = 1
        m = []

        while i < 5:
            temp = sheet.cell_value(j + 1, i)
            m.append(sheet.cell_value(j, i))
            i = i + 1
        j = j + 1
        list_data123.append(m)
        target123.append(temp)

    j = 2000
    while j < 2210:
        i = 0
        m = []

        while i < 5:
            temp = sheet.cell_value(j + 1, i)
            m.append(sheet.cell_value(j, i))
            i = i + 1
        j = j + 1
        past_data.append(m)

    return list_data123

class calcu_pre:
    def __init__(self):
        pass

    min_max = []

    #maximum and minmium
    def min_max1(self,data):
        gold = []
        nasdaq = []
        oil = []
        usdnpr = []
        global min_max

        for i in range(0,len(data)):
            gold.append(data[i][0])
            nasdaq.append(data[i][1])
            oil.append(data[i][2])
            usdnpr.append(data[i][3])
        # min_max.append([min(gold),max(gold)],[min(nasdaq),max(nasdaq)],[min(oil),max(oil)],[min(usdnpr),max(usdnpr)])
        min_max = ([min(gold), max(gold)], [min(nasdaq), max(nasdaq)], [min(oil), max(oil)],[min(usdnpr), max(usdnpr)])
        return min_max


    def min_max_target(self,data):
        min_max_target = []

        for i in range(0,len(data)):
            min_max_target.append(data[i])
            # min_max.append([min(gold),max(gold)],[min(nasdaq),max(nasdaq)],[min(oil),max(oil)],[min(usdnpr),max(usdnpr)])
        min_max = ([min(min_max_target), max(min_max_target)])
        return min_max



    #moving average
    def average(self,data):
        list1=[]
        for j in range(0,len(data)-5):
            avg_gold = 0.0
            avg_nasdaq = 0.0
            avg_oil = 0.0
            avg_usdnpr = 0.0
            m = []
            count = 0
            for i in range(j, j+5):
                avg_gold = (avg_gold + (data[i][1] * (count + 1)))
                avg_nasdaq = (avg_nasdaq + (data[i][2] * (count + 1)))
                avg_oil = (avg_oil + (data[i][3] * (count + 1)))
                avg_usdnpr = (avg_usdnpr + (data[i][4] * (count + 1)))
                count = count + 1
            avg_gold = avg_gold/15
            # print "Average number is: " + str(j)
            # print avg_gold
            avg_nasdaq = avg_nasdaq/15
            avg_oil = avg_oil/15
            avg_usdnpr = avg_usdnpr/15
            m = [avg_gold, avg_nasdaq, avg_oil, avg_usdnpr]
            list1.append(m)
        return list1


    def normalize(self,data):
        norm = []
        for i in range(0,len(data)):
            norm_temp = []
            a = (data[i][0] - min_max[0][0]) / (min_max[0][1] - min_max[0][0]) #normalized value of gold
            norm_temp.append(a)
            b = (data[i][1] - min_max[1][0]) / (min_max[1][1] - min_max[1][0])
            norm_temp.append(b)
            c = (data[i][2] - min_max[2][0]) / (min_max[2][1] - min_max[2][0])
            norm_temp.append(c)
            d = (data[i][3] - min_max[3][0]) / (min_max[3][1] - min_max[3][0])
            norm_temp.append(d)

            norm.append(norm_temp)
        return norm

    def normalize_predict(self,data):
        norm = []
        a = (data[0] - min_max[0][0]) / (min_max[0][1] - min_max[0][0]) #normalized value of gold
        norm.append(a)
        b = (data[1] - min_max[1][0]) / (min_max[1][1] - min_max[1][0])
        norm.append(b)
        c = (data[2] - min_max[2][0]) / (min_max[2][1] - min_max[2][0])
        norm.append(c)
        d = (data[3] - min_max[3][0]) / (min_max[3][1] - min_max[3][0])
        norm.append(d)

        return norm









    def norm_target1(self,data):
       target1 = []
       for i in range(0,len(data)):
            target1.append(data[i])
        # min_max.append([min(gold),max(gold)],[min(nasdaq),max(nasdaq)],[min(oil),max(oil)],[min(usdnpr),max(usdnpr)])
       min_max12 = ([min(target1), max(target1)])
       norm = []
       for i in range(0, len(data)):
           norm_temp = []
           a = (data[i] - min_max12[0]) / (min_max12[1] - min_max12[0])  # normalized value of target
           norm.append(a)

       return norm

    def denormalize(self,data):
        d_price = []
        i=0
        for i in range(0,len(data)):
            b = (data[i]*(min_max[3][1]-min_max[3][0])) + min_max[3][0] #denormalized value and getting normalized value

        return b

    def denormalize12(self, data):
        d_price = []
        i = 0
        # for i in range(0, len(data)):

        # print(data)
        # print(min_max[3][1])

        b = (data * (min_max[3][1] - min_max[3][0])) + min_max[3][0]  # denormalized value and getting normalized value
        return b


print ("Training of the model for fundamental analysis is going on...")

datas = import_data()
s1 = calcu_pre()
store_data = []
create_table()


#calculating averages
average_datas = s1.average(datas)

#calculating min target max, normalization
s1.min_max1(average_datas)
norm_datas = s1.normalize(average_datas)

#min max and normalization for target
norm_target = s1.norm_target1(target)

from . import testing
c = testing.neuralnet(4,8,1)


count1 = 0
error = 1
count = 0
while abs(error) > 0.0000001:
    count1 = count1 + 1
    a = []
    for j in range(0, 4):
        a.append(norm_datas[count][j])

    error = c.feedforward(a, norm_target, count)
    # print "error ......... " + str(error)
    c.backpropagate(norm_target, count)
    count = count + 1
    if count > 1993:
        count = 0
print ("Total Iteration for training is....." + str(count1))



s1.min_max_target(target)

#testing the training datas
# a = c.final11(norm_datas[10])
# print ("normalized value for 10................" + str (a))
# dde = s1.denormalize(a)
# # print  (dde)
# # print datas[11][4]
#
#
# a = c.final11(norm_datas[50])
# print "normalized value for 50................" + str (a)
# dde = s1.denormalize(a)
# print  dde
# print datas[51][4]
count23 = 0
m = 0
while m < 1994:

    a = c.final11(norm_datas[m])
    # print ("iteration......" + str(m))
    dde = s1.denormalize(a)
    # print  (dde)
    # print (datas[m+1][4])


    store_data.append(dde)
    count23 = count23 + 1
    m = m + 1




#extract testing data
li = import_target()
s1.min_max1(li)
norm_datas_testing = s1.normalize(li)

norm_target123 = s1.norm_target1(target123)



# norm_datas_testing = s1.normalize(li)
# print norm_datas_testing
# print s1.denormalize(norm_target123[0][3])
s1.min_max_target(target123)

print ("Training of the model for fundamental analysis is going on...")

temp_acc = 0.0
m = 0
asd1 = 0
final_predict = 0
while m < counttt-2001:

    a = c.final11(norm_datas_testing[m])
    dde = s1.denormalize(a)
    # print  ("predicted data......" + str(dde))
    s = norm_target123[m]
    # print ("actual data......." + str(s1.denormalize12(s)))
    acc = c.accuracy(target123[m], dde)
    temp_acc = temp_acc + acc
    store_data.append(dde)
    asd1 = dde
    final_predict = dde
    count23 = count23 + 1
    m = m + 1


# print "exact"
# print temp_acc
acc = (temp_acc) / (m)
print ("Mean absolute percentage error is ...")
print (acc)




# qeqwe = abc()

# li = import_target()
# s1.min_max1(li)
# norm_datas_testing = s1.normalize_predict(qeqwe)
#
# s1.min_max_target(target123)
#
# a = c.final11(norm_datas_testing)
# dde = s1.denormalize(a)
# print  ("predicted data......" + str(dde))
# predicted_data =dde



class abc11:

    def read_all(self):
        return asd1

    def finaldata(self):
        return final_data

    def abc(self):
        return store_data

    def dateee(self):
        return date12345



a=abc11()

# import pandas as pd
#
# df = pd.DataFrame(read_all(), columns=["Actual"], index=a.dateee())
# ax = df.plot( rot=45)
#
# threshold = 20
# for t in ax.get_xticklabels():
#     if len(t.get_text()) > threshold:
#         t.set_rotation(90)
#
# plt.plot(store_data, label = 'Predicted')
# plt.xlabel('Date', weight = 'bold')
# plt.ylabel('USD/NPR (Rs)', weight = 'bold')
# plt.title('Fundamental Analysis', weight = 'bold')
#
#
# plt.legend()
#
# plt.tight_layout()
# plt.savefig('ig1.png')
#
# plt.show()




fname = join(dirname(dirname(abspath(__file__))), 'prediction', 'trainingdata.xls')
workbook1 = xlrd.open_workbook(fname)
asd1=[]
sheet = workbook1.sheet_by_index(0)
ee = sheet.nrows - 1
j1 = 0

for j in range(0, len(store_data)):
    i = 0
    temp = []
    if j1 == 1995:
        j1 = j1 + 6
    while i < 5:
        temp.append(sheet.cell_value(j1, i))
        i = i + 1
    j1 = j1 + 1
    if j1 == 2106:
        j1 = j1 + 1

    temp.append(store_data[j])
    asd1.append(temp)


abc()
final_data.append(final_predict)





















