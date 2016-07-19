from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import DishPost
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from .forms import DishPostForm
from django.utils import timezone

def dish_home(request):
    dish_list=DishPost.objects.all().order_by('DishCreated_date')[::-1]
    return  render(request, 'dish/dish_list.html',{'dish_list': dish_list})

def dish_detail(request, pk):
    dish_post=DishPost.objects.get(pk=pk)
    dish_hitcount=HitCount.objects.get_for_object(dish_post)
    dish_hitcount_response=HitCountMixin.hit_count(request, dish_hitcount)
    return render(request, 'dish/dish_detail.html', {'dish_post':dish_post, 'dish_hitcount_response':dish_hitcount_response})

def dish_new(request):
    if request.method=="POST":
        dish_form=DishPostForm(request.POST)
        if dish_form.is_valid():
            DishPost=dish_form.save(commit=False)
            DishPost.DishCreated_date=timezone.now()
            DishPost.save()
            return  redirect('dish_detail', pk=DishPost.pk)
    else:
        dish_form = DishPostForm()
    return render(request, 'dish/dish_edit.html', {'dish_form': dish_form})

def dish_edit(request, pk):
    dish_post = get_object_or_404(DishPost, pk=pk)
    if request.method == "POST":
        dish_form = DishPostForm(request.POST, instance=dish_post)
        if dish_form.is_valid():
            dish_post = dish_form.save(commit=False)
            dish_post.DishCreated_date = timezone.now()
            dish_post.save()
            return redirect('dish_detail', pk=dish_post.pk)
    else:
        dish_form = DishPostForm(instance=dish_post)
    return render(request, 'dish/dish_edit.html', {'dish_form': dish_form})