from django.shortcuts import render
from django.db.models import Q
from dish.models import Dish_post
from life.models import Life_post

# Create your views here.
def search(request):
    query=request.GET.get('q', '')
    if query:
        qset_for_dish=Q(Dish_title__icontains=query)
        qset_for_life=Q(Life_title__icontains=query)
        result_for_dish=Dish_post.objects.filter(qset_for_dish)
        result_for_life=Life_post.objects.filter(qset_for_life)
    else:
        result_for_dish=[]
        result_for_life=[]
    return render(request, 'search/search.html', {'result_for_dish':result_for_dish, 'result_for_life':result_for_life})
