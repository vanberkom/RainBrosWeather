from django.urls import path
from . import views

from django.views.generic import RedirectView

urlpatterns = {
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('base/index/', RedirectView.as_view(pattern_name='index', permanent=True)),
}
