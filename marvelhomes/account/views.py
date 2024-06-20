from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView,FormView,TemplateView
# Create your views here.
from django.views import View
from .models import News,Properties,Location,Image,Developer
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class about(View):
    def get(self,request):
        return render (request,"about.html")
    def post(self,request):
        print(request.POST)
        data = {
            'name':request.POST.get('name'),
            'email':request.POST.get('email'),
            'phone':request.POST.get('phone'),
            'message':request.POST.get('message'),
        }
        html_content = render_to_string('email_about.html', {'data': data})
        email = EmailMessage(subject='Message', body='', from_email='from@gmail.com', to=['to@gmail.com'])
        email.content_subtype = 'html'  # Set content type to HTML
        email.body = html_content
        email.send()
        return render(request,'success.html')
class ForSellers(View):
    def get(self,request):
        return render (request,"forsellers.html")
    def post(self,request):
        data = {
            'type':request.POST.get('inquiryType'),
            'info':request.POST.get('information'),
            'full_name':request.POST.get('full_name'),
            'phone':request.POST.get('phone'),
            'email':request.POST.get('email'),
        }
        html_content = render_to_string('email_forsellers.html', {'data': data})
        email = EmailMessage(subject='Email ForSellers', body='', from_email='from@gmail.com', to=['to@gmail.com'])
        email.content_subtype = 'html'  # Set content type to HTML
        email.body = html_content
        email.send()
        return render(request,'success.html')
class FreeReport(View):
    def get(self,request):
        return render(request,'free_report.html')
    def post(self,request):
        print(request.POST)
        data = {
            'location':request.POST.get('location'),
            'email':request.POST.get('email'),
            'project_or_building':request.POST.get('project_or_building'),
            'full_name':request.POST.get('full_name'),
            'ph1':request.POST.get('phone_number'),
            'ph2':request.POST.get('phone_number2'),
        }
        html_content = render_to_string('email_body_free_report.html', {'data': data})
        print(request.POST)
        email = EmailMessage(subject='Your Email Subject', body='', from_email='from@gmail.com', to=['to@gmail.com'])
        email.content_subtype = 'html'  # Set content type to HTML
        email.body = html_content
        email.send()
        return render(request,'success.html')

class AllDeveloper(ListView):
    template_name='all_developer.html'
    queryset = Properties.objects.all()
    context_object_name='property'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        for i in Developer.objects.all():
            context[i.name] = self.queryset.filter(developer=i)
        return context

class DeveloperView(View):
    def get(self,request,dev):
        dev = Developer.objects.get(name=dev)
        properties = Properties.objects.filter(developer=dev).order_by('-created_at')
        return render(request,'developer.html',{'dev':dev,'properties':properties})
    
    
class AllProperty(ListView):
    template_name='all_property.html'
    queryset = Properties.objects.all()
    context_object_name='property'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["apartment"] = self.queryset.filter(category='apartments')
        context["villas"] = self.queryset.filter(category='villas')
        context["townhouses"] = self.queryset.filter(category='townhouses')
        return context
    
    
class PropertyDetails(DetailView):
    template_name='property_details.html'
    queryset = Properties.objects.all()
    pk_url_kwarg='pid'
    context_object_name='property'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        property = Properties.objects.get(id=self.kwargs.get('pid'))
        image = Image.objects.filter(property = property)
        context['image'] = image
        return context
    

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
    latest_news= News.objects.all().order_by('-created_at')[:6]
    return render(request,'detail_news.html',{"news":news,"latest":latest_news})

def all_news(request):
    news = News.objects.all()
    return render(request,'news_list.html',{"news_list":news})


def mainpage(request):
    properties = Properties.objects.all().order_by('-created_at')[:6]
    news_list=News.objects.all().order_by('-updated_date')[:6]
    return render(request, 'mainpage.html',{'news_items':news_list,'properties':properties})




class home(View):
    def get(self,request):
        return render (request,"mainpage.html")

class listing(View):
    def get(self,request):
        # print('about view called')
       
        return render (request,"listing.html")

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
