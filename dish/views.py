from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import DishPost
from django.utils import timezone

def dish_home(request):
    dish_list=DishPost.objects.filter(DishCreated_date__lte=timezone.now()).order_by('DishCreated_date')
    return  render(request, 'dish/dish_list.html',{'dish_list': dish_list})

def dish_detail(request, pk):
    dish_post=DishPost.objects.get(pk=pk)
    return render(request, 'dish/dish_detail.html', {'dish_post':dish_post})