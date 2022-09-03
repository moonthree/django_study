from django.shortcuts import render

# Create your views here.
def food(request):
    foods = ['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
    context = {
        'foods': foods,
    }
    return render(request, 'menus/food.html', context)

def receipt(request):
    foods = ['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
    drinks = ['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']

    food_order = request.GET.get('food_order')
    drink_order = request.GET.get('drink_order')

    if food_order:
        if food_order in foods:
            context = {
                'order': food_order,
                'flag': True
            }
        else:
            context = {
                'order': food_order,
                'flag': False
            }
    else:
        if drink_order.lower() in drinks:
            context = {
                'order': drink_order.capitalize(),
                'flag': True
            }
        else:
            context = {
                'order': drink_order.capitalize(),
                'flag': False
            }
    return render(request, 'menus/receipt.html', context)

def drink(request):
    drinks = ['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']
    context = {
        'drinks': drinks,
    }
    return render(request, 'menus/drink.html', context)