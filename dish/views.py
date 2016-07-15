from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import DishPost
from hitcount.views import HitCountMixin
from hitcount.models import HitCount

def dish_home(request):
    dish_list=DishPost.objects.all().order_by('DishCreated_date')[::-1]
    return  render(request, 'dish/dish_list.html',{'dish_list': dish_list})

def dish_detail(request, pk):
    dish_post=DishPost.objects.get(pk=pk)
    dish_hitcount=HitCount.objects.get_for_object(dish_post)
    dish_hitcount_response=HitCountMixin.hit_count(request, dish_hitcount)
    return render(request, 'dish/dish_detail.html', {'dish_post':dish_post, 'dish_hitcount_response':dish_hitcount_response})