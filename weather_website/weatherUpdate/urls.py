from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weatherUpdate/daily/', views.daily, name='daily'),
    path('weatherUpdate/weekly/', views.weekly, name='weekly'),
    path('error/', views.errorpage, name='errorpage'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
