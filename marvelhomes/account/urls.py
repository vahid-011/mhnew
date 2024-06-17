
from django.urls import path

from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path("about",about.as_view(),name="about"),
    path('about/', about.as_view(), name='about'),
    path('forsellers/', forsellers.as_view(), name='forsellers'),
    path('home/',home.as_view(), name='home'),
    path('',listing.as_view(),name='listing'),
     path('news/',news_list, name='news_list'),
     path('newslist/',all_news, name='news'),
     path('news/<int:id>',detail_news, name='detail_news'),
     path('property/<category>',Category.as_view(), name='category_property'),
     path('property_details/<int:pid>',PropertyDetails.as_view(), name='property_detail'),
     path('place/<place>',PlaceView.as_view(), name='place'),
     path('all_property/',AllProperty.as_view(), name='all_property'),
     path('developer/<dev>',DeveloperView.as_view(), name='dev'),
     path('all_developer/',AllDeveloper.as_view(), name='all_developer'),
    # path('news/<str:category>',views.news_list, name='news_list'),
    



    
    
    # path('about',about, name='about'),  # Corrected path for about
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
