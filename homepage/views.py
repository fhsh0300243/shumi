from django.shortcuts import render

# Create your views here.
def homepage_app(request):
    return render(request, 'homepage/app_list.html',{})