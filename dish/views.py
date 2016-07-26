from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Dish_post, Dish_comment, Dish_comment_reply
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from .forms import DishPostForm, DishCommentForm, DishCommentReplyForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def dish_home(request):
    dish_post_list=Dish_post.objects.all().order_by('Dish_post_created_date')[::-1]
    return  render(request, 'dish/dish_list.html',{'dish_post_list': dish_post_list})

def dish_detail(request, pk):
    dish_post_from_db=Dish_post.objects.get(pk=pk)
    dish_hitcount=HitCount.objects.get_for_object(dish_post_from_db)
    dish_hitcount_response=HitCountMixin.hit_count(request, dish_hitcount)
    return render(request, 'dish/dish_detail.html', {'dish_post_from_db':dish_post_from_db, 'dish_hitcount_response':dish_hitcount_response})

def dish_new(request):
    if request.method=="POST":
        dish_post_form=DishPostForm(request.POST)
        if dish_post_form.is_valid():
            dish_post_from_admin=dish_post_form.save(commit=False)
            dish_post_from_admin.Dish_post_created_date=timezone.now()
            dish_post_from_admin.save()
            return  redirect('dish_detail', pk=dish_post_from_admin.pk)
    else:
        dish_post_form = DishPostForm()
    return render(request, 'dish/dish_edit.html', {'dish_post_form': dish_post_form})

def dish_edit(request, pk):
    dish_post_from_db = get_object_or_404(Dish_post, pk=pk)
    if request.method == "POST":
        dish_post_form = DishPostForm(request.POST, instance=dish_post_from_db)
        if dish_post_form.is_valid():
            dish_post_from_admin = dish_post_form.save(commit=False)
            dish_post_from_admin.Dish_post_created_date = timezone.now()
            dish_post_from_admin.save()
            return redirect('dish_detail', pk=dish_post_from_admin.pk)
    else:
        dish_post_form = DishPostForm(instance=dish_post_from_db)
    return render(request, 'dish/dish_edit.html', {'dish_post_form': dish_post_form})

def dish_add_comment_to_post(request,pk):
    dish_post_from_db=get_object_or_404(Dish_post, pk=pk)
    if request.method=="POST":
        dish_comment_form=DishCommentForm(request.POST)
        if dish_comment_form.is_valid():
            dish_comment_from_admin=dish_comment_form.save(commit=False)
            dish_comment_from_admin.Dish_comment_post=dish_post_from_db
            dish_comment_from_admin.save()
            return redirect('dish.views.dish_detail', pk=dish_post_from_db.pk)
    else:
        dish_comment_form=DishCommentForm()
    return render(request, 'dish/dish_add_comment_to_post.html', {'dish_comment_form': dish_comment_form})

@login_required
def dish_comment_approve(request, pk):
    dish_comment_from_db = get_object_or_404(Dish_comment, pk=pk)
    dish_comment_from_db.approve()
    return redirect('dish.views.dish_detail', pk=dish_comment_from_db.Dish_comment_post.pk)

@login_required
def dish_comment_remove(request, pk):
    dish_comment_from_db = get_object_or_404(Dish_comment, pk=pk)
    dish_post_pk = dish_comment_from_db.Dish_comment_post.pk
    dish_comment_from_db.delete()
    return redirect('dish.views.dish_detail', pk=dish_post_pk)

def dish_add_reply_to_comment(request, pk1, pk2):
    dish_post_from_db=get_object_or_404(Dish_post, pk=pk1)
    dish_comment_from_db=Dish_comment.objects.get(pk=pk2)
    if request.method=="POST":
        dish_reply_form=DishCommentReplyForm(request.POST)
        if dish_reply_form.is_valid():
            dish_reply_from_admin=dish_reply_form.save(commit=False)
            dish_reply_from_admin.Dish_comment_reply_post=dish_comment_from_db
            dish_reply_from_admin.save()
            return redirect('dish.views.dish_detail', pk=dish_post_from_db.pk)
    else:
        dish_reply_form=DishCommentReplyForm()
    return render(request, 'dish/dish_add_reply_to_comment.html', {'dish_reply_form': dish_reply_form})