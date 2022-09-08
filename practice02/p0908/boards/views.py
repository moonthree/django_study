from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Board
from .forms import BoardForm

# Create your views here.
@require_safe
def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', board.pk)
    else:
        # new
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    # board = Board.objects.get(pk=pk)
    # get_object_or_404 = 데이터를 조회하지 못하면 404 에러를 띄워라!
    # 일반적으로 웹에서 없는 데이터 조회 시 404 에러를 띄움
    # 웹 서버랑 연동하게 되면 더 자세히 이해할 수 있음
    board = get_object_or_404(Board, pk=pk)

    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)


@require_POST
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('boards:index')

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }
    return render(request, 'boards/update.html', context)
