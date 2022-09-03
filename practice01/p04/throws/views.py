from django.shortcuts import render

# Create your views here.
def first(request):
    t_mes = request.GET.get('t_mes')
    if t_mes == None:
        t_mes = 'nothing'
    context = {
        't_mes': t_mes,
    }

    return render(request, 'throws/first.html', context)

def second(request):
    f_mes = request.GET.get('f_mes')
    
    context = {
        'f_mes': f_mes,
    }
    return render(request, 'throws/second.html', context)

def third(request):
    s_mes = request.GET.get('s_mes')

    context = {
        's_mes': s_mes,
    }
    return render(request, 'throws/third.html', context)