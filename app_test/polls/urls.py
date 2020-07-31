from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('extend', views.html_response, name='not_important_at_the_moment')
]
