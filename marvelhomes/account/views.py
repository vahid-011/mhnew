from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView,FormView,TemplateView
# Create your views here.
from django.views import View
from .models import News,Properties,Location
from django.views.generic import ListView,DetailView


class AllProperty(TemplateView):
    template_name='all_property.html'
    
class PropertyDetails(DetailView):
    template_name='property_details.html'
    queryset = Properties.objects.all()
    pk_url_kwarg='pid'
    context_object_name='property'

class PlaceView(View):
    def get(self,request,place):
        loc = Location.objects.get(place=place)
        properties = Properties.objects.filter(location=loc)
        place_of_location = Location.objects.get(place = place)
        return render(request,'place.html',{'property':properties,'place':place_of_location})

class Category(ListView):
    template_name='category_property.html'
    queryset=Properties.objects.all()
    context_object_name='property'
    def get_context_data(self, **kwargs):
        res = Properties.objects.filter(category=self.kwargs.get('category')) 
        return {'property':res}

def detail_news(request,id):
    news = News.objects.get(id=id)
    return render(request,'detail_news.html',{"news":news})

def all_news(request):
    news = News.objects.all()
    return render(request,'news_list.html',{"news_list":news})


def mainpage(request):
    apartments = Properties.objects.filter(category='apartments')
    news_list=News.objects.all().order_by('-updated_date')[:6]
    return render(request, 'mainpage.html',{'news_items':news_list,'apartments':apartments})




class about(View):
    def get(self,request):
        # print('about view called')
       
        return render (request,"about.html")
class home(View):
    def get(self,request):
        return render (request,"mainpage.html")

class listing(View):
    def get(self,request):
        # print('about view called')
       
        return render (request,"listing.html")
class forsellers(View):
    def get(self,request):
        # print('about view called')
       
        return render (request,"forsellers.html")

from django.shortcuts import render
from .models import News

# def news_list(request, category):
#     news_list = News.objects.filter(category=category)
#     print(news_list)
#     context = {
#         'news_list': news_list,
#     }
#     return render(request, 'mainpage.html',context)



# views.py
from django.shortcuts import render
from .models import News

def news_list(request):
    news_items = News.objects.all()
    return render(request, 'mainpage.html', {'news_items': news_items})
