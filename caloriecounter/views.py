from django.shortcuts import render, redirect
from .forms import FoodItemForm
from .models import FoodItem

def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    else:
        form = FoodItemForm()
    return render(request, 'add_food.html', {'form': form})


def view_food(request):
    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)

    return render(request, 'view_food.html', {'food_items': food_items, 'total_calories': total_calories})


def remove_food(request, food_id):
    food_item = FoodItem.objects.get(id=food_id)
    food_item.delete()

    return redirect('view_food')


def reset_calories(request):
    FoodItem.objects.all().delete()
    return redirect('view_food')
