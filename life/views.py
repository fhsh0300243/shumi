from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import LifePost
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from .forms import LifePostForm
from django.utils import timezone

def life_home(request):
    life_list=LifePost.objects.all().order_by('LifeCreated_date')[::-1]
    return  render(request, 'life/life_list.html',{'life_list': life_list})

def life_detail(request, pk):
    life_post=LifePost.objects.get(pk=pk)
    life_hitcount=HitCount.objects.get_for_object(life_post)
    life_hitcount_response=HitCountMixin.hit_count(request, life_hitcount)
    return render(request, 'life/life_detail.html', {'life_post':life_post, 'life_hitcount_response':life_hitcount_response})

def life_new(request):
    if request.method=="POST":
        life_form=LifePostForm(request.POST)
        if life_form.is_valid():
            LifePost=life_form.save(commit=False)
            LifePost.LifeCreated_date=timezone.now()
            LifePost.save()
            return  redirect('life_detail', pk=LifePost.pk)
    else:
        life_form = LifePostForm()
    return render(request, 'life/life_edit.html', {'life_form': life_form})

def life_edit(request, pk):
    life_post = get_object_or_404(LifePost, pk=pk)
    if request.method == "POST":
        life_form = LifePostForm(request.POST, instance=life_post)
        if life_form.is_valid():
            life_post = life_form.save(commit=False)
            life_post.LifeCreated_date = timezone.now()
            life_post.save()
            return redirect('life_detail', pk=life_post.pk)
    else:
        life_form = LifePostForm(instance=life_post)
    return render(request, 'life/life_edit.html', {'life_form': life_form})