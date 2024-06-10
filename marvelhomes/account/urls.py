
from django.urls import path

from .views import about,listing,news_list,home,forsellers
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
    # path('news/<str:category>',views.news_list, name='news_list'),
    



    
    
    # path('about',about, name='about'),  # Corrected path for about
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
