from django.urls import path
from . import views

app_name = 'rotaryapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact_view, name='contact'),
    path('joinus', views.joinus, name='joinus'),


]