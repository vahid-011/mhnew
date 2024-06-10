from django.shortcuts import render
from django.views.generic import CreateView,FormView,TemplateView
# Create your views here.
from django.views import View
from .models import News


def mainpage(request):
    news_list=News.objects.all().order_by('-updated_date')[:6]
    return render(request, 'mainpage.html',{'news_items':news_list})




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
