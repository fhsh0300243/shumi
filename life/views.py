from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Life_post, Life_comment, Life_comment_reply
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from .forms import LifePostForm, LifeCommentForm, LifeCommentReplyForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def life_home(request):
    life_post_list=Life_post.objects.all().order_by('Life_post_created_date')[::-1]
    return  render(request, 'life/life_list.html',{'life_post_list': life_post_list})

def life_detail(request, pk):
    life_post_from_db=Life_post.objects.get(pk=pk)
    life_hitcount=HitCount.objects.get_for_object(life_post_from_db)
    life_hitcount_response=HitCountMixin.hit_count(request, life_hitcount)
    return render(request, 'life/life_detail.html', {'life_post_from_db':life_post_from_db, 'life_hitcount_response':life_hitcount_response})

def life_new(request):
    if request.method=="POST":
        life_post_form=LifePostForm(request.POST)
        if life_post_form.is_valid():
            Life_post_from_admin=life_post_form.save(commit=False)
            Life_post_from_admin.Life_post_created_date=timezone.now()
            Life_post_from_admin.save()
            return  redirect('life_detail', pk=Life_post_from_admin.pk)
    else:
        life_post_form = LifePostForm()
    return render(request, 'life/life_edit.html', {'life_post_form': life_post_form})

def life_edit(request, pk):
    life_post_from_db = get_object_or_404(Life_post, pk=pk)
    if request.method == "POST":
        life_post_form = LifePostForm(request.POST, instance=life_post_from_db)
        if life_post_form.is_valid():
            life_post_from_admin = life_post_form.save(commit=False)
            life_post_from_admin.Life_post_created_date = timezone.now()
            life_post_from_admin.save()
            return redirect('life_detail', pk=life_post_from_admin.pk)
    else:
        life_post_form = LifePostForm(instance=life_post_from_db)
    return render(request, 'life/life_edit.html', {'life_post_form': life_post_form})

def life_add_comment_to_post(request,pk):
    life_post_from_db=get_object_or_404(Life_post, pk=pk)
    if request.method=="POST":
        life_comment_form=LifeCommentForm(request.POST)
        if life_comment_form.is_valid():
            life_comment_from_admin=life_comment_form.save(commit=False)
            life_comment_from_admin.Life_comment_post=life_post_from_db
            life_comment_from_admin.save()
            return redirect('life.views.life_detail', pk=life_post_from_db.pk)
    else:
        life_comment_form=LifeCommentForm()
    return render(request, 'life/life_add_comment_to_post.html', {'life_comment_form': life_comment_form})

@login_required
def life_comment_approve(request, pk):
    life_comment_from_db = get_object_or_404(Life_comment, pk=pk)
    life_comment_from_db.approve()
    return redirect('life.views.life_detail', pk=life_comment_from_db.Life_comment_post.pk)

@login_required
def life_comment_remove(request, pk):
    life_comment_from_db = get_object_or_404(Life_comment, pk=pk)
    life_post_pk = life_comment_from_db.Life_comment_post.pk
    life_comment_from_db.delete()
    return redirect('life.views.life_detail', pk=life_post_pk)

def life_add_reply_to_comment(request, pk1, pk2):
    life_post_from_db=get_object_or_404(Life_post, pk=pk1)
    life_comment_from_db=Life_comment.objects.get(pk=pk2)
    if request.method=="POST":
        life_reply_form=LifeCommentReplyForm(request.POST)
        if life_reply_form.is_valid():
            life_reply_from_admin=life_reply_form.save(commit=False)
            life_reply_from_admin.Life_comment_reply_post=life_comment_from_db
            life_reply_from_admin.save()
            return redirect('life.views.life_detail', pk=life_post_from_db.pk)
    else:
        life_reply_form=LifeCommentReplyForm()
    return render(request, 'life/life_add_reply_to_comment.html', {'life_reply_form': life_reply_form})