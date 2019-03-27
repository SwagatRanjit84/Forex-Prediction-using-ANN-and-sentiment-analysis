import xlrd
from django.shortcuts import render
from django.http import HttpResponse
from .models import data
import django
from django.template import loader

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic.base import View



# Create your views here.
def index(request):
    all_data = data.objects.all()

    template = loader.get_template('prediction/index.html')
    a2=[]

    for data1 in reversed(all_data):
        a1=[]

        a1.append( data1.date)
        a1.append(data1.gold)
        a1.append(data1.nasdaq)
        a1.append(data1.oil)
        a1.append(data1.usdnpr)
        a1.append(data1.predicate)
        a2.append(a1)


    img = {
        'all_data': a2,
        # 'predict': predict12,
    }
    #
    # return HttpResponse("<h1>sahii ho kta ho</h1>"+html)

    response = django.http.HttpResponse(template.render(img,request) )
    return response



def crawler(request):
    from . import webcrawler

    # obj = webcrawler.abc()
    # obj.extract()

    obj12 = webcrawler.abc()
    check = obj12.check1()

    from . import initial

    #storing only last dvata
    a=data()
    obj1 = initial.abc11()
    abc = obj1.finaldata()

    all_data = data.objects.all()

    for data1 in all_data:
        date1 =  data1.date


    if (check == date1):
        html = "<h1>Data is upto date</h1>"

    else:

        print("total datas")
        j = 0
        a.date = abc[0]
        a.gold = abc[1]
        a.nasdaq = abc[2]
        a.oil = abc[3]
        a.usdnpr = abc[4]
        a.predicate = abc[5]
        html = "<h1>Data stored sucessfully</h1>"
        a.save()

    return HttpResponse(html)
    # return HttpResponse("wait")



def train(request):
    template = loader.get_template('prediction/train.html')
    a2 = "abc"
    img = {
        'all_data': a2,
    }

    response = django.http.HttpResponse(template.render(img, request))

    return response


def abc(request):

    all_data = data.objects.all()

    template = loader.get_template('prediction/iq.html')
    a2 = [123]

    img = {
        'all_data': a2,
        # 'predict': predict12,
    }

    response = django.http.HttpResponse(template.render(img, request))

    return response


# def read()
#     # all_data = data.objects.all()






    #storing only last dvata
    # a=data()
    # print("total datas")
    # print((abc[1]))
    # # j = 0
    # a.date = abc[j][0]
    # a.gold = abc[j][1]
    # a.nasdaq = abc[j][2]
    # a.oil = abc[j][3]
    # a.usdnpr = abc[j][4]
    # a.predicate = abc[j][5]
    # print ("last data")
    # print (a.date)
    # print(a.gold)
    #
    #
    # print("abcdeee")
    # print(abc[j][0])
    # print(abc[j][1])
    #
    # # a.save()

    # #storing data
    # a = [data() for _ in range(len(abc))]
    #
    # j = 1
    # for i in range(0,len(abc)-1):
    #
    #     # a = data()
    #     a[j].date =  abc[j][0]
    #     a[j].gold = abc[j][1]
    #     a[j].nasdaq = abc[j][2]
    #     a[j].oil = abc[j][3]
    #     a[j].usdnpr = abc[j][4]
    #     a[j].predicate = abc[j][5]
    #     a[j].save()
    #     j = j+1
    #
    # # print("ASdasd")
    # # print(a)
    #












# def insert-database()
# from .initial import abc11
#
# a11 = abc11()
# abc = a11.read_all()
#
# a = [data() for _ in range(len(abc))]
#
#
# j = 0
# for i in range(0,len(abc)):
#
#     # a = data()
#     a[j].date =  abc[j][0]
#     a[j].gold = abc[j][1]
#     a[j].nasdaq = abc[j][2]
#     a[j].oil = abc[j][3]
#     a[j].usdnpr = abc[j][4]
#     a[j].predicate = abc[j][5]
#     a[j].save()
#     j = j+1
# print("ASdasd")
# print(a)
#
#
# return HttpResponse("<h1>sahii ho kta ho</h1>")
