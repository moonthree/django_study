from django.shortcuts import render
import random

# Create your views here.
def certification1(request):
    age = range(25,31)
    grade = ['a', 'b', 'c', 'd', 's']
    context = {
        'age': random.choice(age),
        'grade': random.choice(grade).upper(),
    }
    return render(request, 'certification/certification1.html', context)

def certification2(request):
    age = range(25,31)
    grade = ['a', 'b', 'c', 'd', 's']
    context = {
        'age': random.choice(age),
        'grade': random.choice(grade).upper(),
    }
    return render(request, 'certification/certification2.html', context)

def certification3(request):
    age = range(25,31)
    grade = ['a', 'b', 'c', 'd', 's']
    context = {
        'age': random.choice(age),
        'grade': random.choice(grade).upper(),
    }
    return render(request, 'certification/certification3.html', context)