from django.shortcuts import render

# Create your views here.
from .models import LifePost
from django.utils import timezone

def life_home(request):
    life_list=LifePost.objects.filter(LifeCreated_date__lte=timezone.now()).order_by('LifeCreated_date')
    return  render(request, 'life/life_list.html',{'life_list': life_list})

def life_detail(request, pk):
    life_post=LifePost.objects.get(pk=pk)
    return render(request, 'life/life_detail.html', {'life_post':life_post})