from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Humor_post, Humor_comment, Humor_comment_reply
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from .forms import HumorPostForm, HumorCommentForm, HumorCommentReplyForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def humor_home(request):
    humor_post_list=Humor_post.objects.all().order_by('Humor_post_created_date')[::-1]
    return  render(request, 'humor/humor_list.html',{'humor_post_list': humor_post_list})

def humor_detail(request, pk):
    humor_post_from_db=Humor_post.objects.get(pk=pk)
    humor_hitcount=HitCount.objects.get_for_object(humor_post_from_db)
    humor_hitcount_response=HitCountMixin.hit_count(request, humor_hitcount)
    return render(request, 'humor/humor_detail.html', {'humor_post_from_db':humor_post_from_db, 'humor_hitcount_response':humor_hitcount_response})

def humor_new(request):
    if request.method=="POST":
        humor_post_form=HumorPostForm(request.POST)
        if humor_post_form.is_valid():
            Humor_post_from_admin=humor_post_form.save(commit=False)
            Humor_post_from_admin.Humor_post_created_date=timezone.now()
            Humor_post_from_admin.save()
            return  redirect('humor_detail', pk=Humor_post_from_admin.pk)
    else:
        humor_post_form = HumorPostForm()
    return render(request, 'humor/humor_edit.html', {'humor_post_form': humor_post_form})

def humor_edit(request, pk):
    humor_post_from_db = get_object_or_404(Humor_post, pk=pk)
    if request.method == "POST":
        humor_post_form = HumorPostForm(request.POST, instance=humor_post_from_db)
        if humor_post_form.is_valid():
            humor_post_from_admin = humor_post_form.save(commit=False)
            humor_post_from_admin.Humor_post_created_date = timezone.now()
            humor_post_from_admin.save()
            return redirect('humor_detail', pk=humor_post_from_admin.pk)
    else:
        humor_post_form = HumorPostForm(instance=humor_post_from_db)
    return render(request, 'humor/humor_edit.html', {'humor_post_form': humor_post_form})

def humor_add_comment_to_post(request,pk):
    humor_post_from_db=get_object_or_404(Humor_post, pk=pk)
    if request.method=="POST":
        humor_comment_form=HumorCommentForm(request.POST)
        if humor_comment_form.is_valid():
            humor_comment_from_admin=humor_comment_form.save(commit=False)
            humor_comment_from_admin.Humor_comment_post=humor_post_from_db
            humor_comment_from_admin.save()
            return redirect('humor.views.humor_detail', pk=humor_post_from_db.pk)
    else:
        humor_comment_form=HumorCommentForm()
    return render(request, 'humor/humor_add_comment_to_post.html', {'humor_comment_form': humor_comment_form})

@login_required
def humor_comment_approve(request, pk):
    humor_comment_from_db = get_object_or_404(Humor_comment, pk=pk)
    humor_comment_from_db.approve()
    return redirect('humor.views.humor_detail', pk=humor_comment_from_db.Humor_comment_post.pk)

@login_required
def humor_comment_remove(request, pk):
    humor_comment_from_db = get_object_or_404(Humor_comment, pk=pk)
    humor_post_pk = humor_comment_from_db.Humor_comment_post.pk
    humor_comment_from_db.delete()
    return redirect('humor.views.humor_detail', pk=humor_post_pk)

def humor_add_reply_to_comment(request, pk1, pk2):
    humor_post_from_db=get_object_or_404(Humor_post, pk=pk1)
    humor_comment_from_db=Humor_comment.objects.get(pk=pk2)
    if request.method=="POST":
        humor_reply_form=HumorCommentReplyForm(request.POST)
        if humor_reply_form.is_valid():
            humor_reply_from_admin=humor_reply_form.save(commit=False)
            humor_reply_from_admin.Humor_comment_reply_post=humor_comment_from_db
            humor_reply_from_admin.save()
            return redirect('humor.views.humor_detail', pk=humor_post_from_db.pk)
    else:
        humor_reply_form=HumorCommentReplyForm()
    return render(request, 'humor/humor_add_reply_to_comment.html', {'humor_reply_form': humor_reply_form})