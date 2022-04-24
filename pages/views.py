from django.shortcuts import render
from .models import Team
from carss.models import Car

# Create your views here.

def home(request):
    teams=Team.objects.all()
    featured_cars=Car.objects.all().order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.all().order_by('-created_date')
    # search_fields=Car.objects.values('model','city','year','body_style')
    # print(search_fields)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
  
    print(model_search)
    data={
        "teams":teams,
        "featured_cars":featured_cars,
        "all_cars":all_cars,
        # "search_fields":search_fields
        "model_search":model_search,
        "city_search":city_search,
        "year_search":year_search,
        "body_style_search":body_style_search,
    
        
    }
    return render(request , 'pages/home.html',context=data)


def about(request):
    teams=Team.objects.all()
    data={
        "teams":teams
    }
    return render(request,'pages/about.html',context=data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')