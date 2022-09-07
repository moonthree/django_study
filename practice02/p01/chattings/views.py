from django.shortcuts import render, redirect
from .models import Chatting
from .forms import ChattingForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    chattings = Chatting.objects.all()
    context = {
        'chattings': chattings,
    }
    return render(request, 'chattings/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ChattingForm(request.POST)
        if form.is_valid():
            chatting = form.save()
            return redirect('chattings:detail', chatting.pk)
        print(f'{form}')
    else:
        form = ChattingForm()
        print(f'{form}')
    context = {
        'form': form,
    }
    return render(request, 'chattings/create.html', context)
    
@require_safe
def detail(request, pk):
    chatting = Chatting.objects.get(pk=pk)
    context = {
        'chatting': chatting,
    }
    return render(request, 'chattings/detail.html', context)

@require_POST
def delete(request, pk):
    if request.method == 'POST':
        chat = Chatting.objects.get(pk=pk)
        chat.delete()
    return redirect('chattings:index')