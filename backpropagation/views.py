import xlrd
from django.shortcuts import render
from django.http import HttpResponse
import django
from django.template import loader
from .models import data1



# Create your views here.
def index(request):
    from .models import data1

    all_data = data1.objects.all()

    template = loader.get_template('backpropagation/index.html')
    a2 = []

    for data1 in reversed(all_data):
        a1 = []

        a1.append(data1.date)
        a1.append(data1.lowa)
        a1.append(data1.opena)
        a1.append(data1.higha)
        a1.append(data1.closea)
        a1.append(data1.predicatea)
        a2.append(a1)

    img = {
        'all_data': a2,
        # 'predict': predict12,
    }
    #
    # return HttpResponse("<h1>sahii ho kta ho</h1>"+html)

    response = django.http.HttpResponse(template.render(img, request))
    return response



def crawlera(request):
    from . import webcrawler
    from .models import data1

    # obj = webcrawler.abc()
    # obj.extract()

    obj12 = webcrawler.abc()
    check = obj12.check1()

    from . import technical_pre

    #storing only last dvata


    a = data1()
    obj1 = technical_pre.abc11()
    abc = obj1.finaldata()


    all_data = data1.objects.all()

    for data1 in all_data:
        date1 =  data1.date

    if (check == date1):
        html = "<h1>Data is upto date</h1>"

    else:

        j = 0
        a.date = abc[0]
        a.lowa = abc[1]
        a.opena = abc[2]
        a.higha = abc[3]
        a.closea = abc[4]
        a.predicatea = abc[5]
        html = "<h1>Data stored sucessfully</h1>"
        a.save()

    return HttpResponse(html)
    # return HttpResponse("wait")

def traina(request):
    template = loader.get_template('backpropagation/train.html')
    a2 = "abc"
    img = {
        'all_data': a2,
    }

    response = django.http.HttpResponse(template.render(img, request))

    return response


def abca(request):
    from .models import data1

    all_data = data1.objects.all()

    template = loader.get_template('backpropagation/im.html')

    a2 = [123]



    img = {
        'all_data': a2,
        # 'predict': predict12,
    }

    response = django.http.HttpResponse(template.render(img, request))

    return response

