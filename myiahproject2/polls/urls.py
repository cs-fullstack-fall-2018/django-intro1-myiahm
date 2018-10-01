from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('language', views.language, name='language'),
    path('system', views.system, name='system'),
    path('IDE', views.IDE, name='IDE')
]