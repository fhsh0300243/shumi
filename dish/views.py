from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import DishPost
from django.utils import timezone

def dish_home(request):
    dish_list=DishPost.objects.all().order_by('DishCreated_date')[::-1]
    return  render(request, 'dish/dish_list.html',{'dish_list': dish_list})

def dish_detail(request, pk):
    dish_post=DishPost.objects.get(pk=pk)
    return render(request, 'dish/dish_detail.html', {'dish_post':dish_post})

