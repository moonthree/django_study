from django.shortcuts import render

# Create your views here.
def calc(request):
    return render(request, 'cal/calc.html')

def result(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    plus = first+second
    multiply = first*second
    minus = first-second
    divide = 0
    if second != 0:
        divide = first/second

    context = {
        'first': first,
        'second': second,
        'plus': plus,
        'multiply': multiply,
        'minus': minus,
        'divide': divide,
    }

    return render(request, 'cal/result.html', context)