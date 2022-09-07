from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm

# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    memos = Memo.objects.all()
    context = {
        'memos': memos,
    }
    return render(request, 'memos/index.html', context)

def create(request):
    if request.method == 'POST':
        # create
        form = MemoForm(request.POST)
        if form.is_valid():                                 # is_valid를 통과하지 못하면
            memo = form.save()
            return redirect('memos:detail', memo.pk)
    else:
        # new
        form = MemoForm()

    context = {                                             # is_valid를 통과하지 못한 것을 여기서 받음
        'form': form,
    }
    return render(request, 'memos/create.html', context)


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo': memo,
    }
    return render(request, 'memos/detail.html', context)


def delete(request, pk):
    if request.method == 'POST':
        memo = Memo.objects.get(pk=pk)
        memo.delete()
    return redirect('memos:index')

