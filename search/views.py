from django.shortcuts import render
from django.db.models import Q
from dish.models import Dish_post
from life.models import Life_post
from functools import reduce
import operator

# Create your views here.
def search(request):
    global result_empty_for_dish, result_empty_for_life, errors
    result_empty_for_dish=[]
    result_empty_for_life=[]
    errors = []
    query=request.GET.get('q')
    if query:
        result_for_dish = Dish_post.objects.filter(Q(Dish_title__icontains=query))
        result_for_life = Life_post.objects.filter(Q(Life_title__icontains=query))
        if not result_for_dish:
            result_empty_for_dish.append('Not found')
        if not result_for_life:
            result_empty_for_life.append('Not found')
        return render(request, 'search/search.html',
                      {'result_for_dish': result_for_dish, 'result_for_life': result_for_life, 'result_empty_for_dish':result_empty_for_dish, 'result_empty_for_life':result_empty_for_life})
    else:
        errors.append('請輸入搜尋項目')
        return render(request, 'search/search.html', {'errors': errors})



