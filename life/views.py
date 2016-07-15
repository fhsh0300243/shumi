from django.shortcuts import render

# Create your views here.
from .models import LifePost
from hitcount.views import HitCountMixin
from hitcount.models import HitCount

def life_home(request):
    life_list=LifePost.objects.all().order_by('LifeCreated_date')[::-1]
    return  render(request, 'life/life_list.html',{'life_list': life_list})

def life_detail(request, pk):
    life_post=LifePost.objects.get(pk=pk)
    life_hitcount=HitCount.objects.get_for_object(life_post)
    life_hitcount_response=HitCountMixin.hit_count(request, life_hitcount)
    return render(request, 'life/life_detail.html', {'life_post':life_post, 'life_hitcount_response':life_hitcount_response})