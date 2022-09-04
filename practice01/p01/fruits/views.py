from django.shortcuts import render

# Create your views here.
def fruit(request):
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]

    context = {
        'fruits':fruit_list,
        'hate':hate,

    }
    return render(request, 'fruits/fruit.html', context)

def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

    if thing in product_price:
        t_price = product_price[thing] * cnt
        context = {
            'thing':thing,
            'cnt':cnt,
            't_price':t_price,
            'flag':True,
        }
    else:
        context = {
            'thing':thing,
            'flag':False,
        }
    return render(request, 'fruits/price.html', context)

def cal(request, a, b):
    add = a + b
    multiply = a * b
    minus = a - b
    if b == 0:
        divide = ''
    else:
        divide = a / b
    context = {
        'a': a,
        'b': b,
        'add': add,
        'multiply': multiply,
        'minus': minus,
        'divide': divide,
    }
    return render(request, 'fruits/cal.html', context)

def first(request):
    s_mes = request.GET.get('s_mes')
    if s_mes == None:
        s_mes = 'nothing'
    context = {
        's_mes': s_mes,
    }

    return render(request, 'fruits/first.html', context)

def second(request):
    f_mes = request.GET.get('f_mes')
    
    context = {
        'f_mes': f_mes,
    }
    return render(request, 'fruits/second.html', context)
