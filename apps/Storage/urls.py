from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('Contact/', Contact, name='Contact'),
    path('About/', About, name='About'),
    path('Blog/', Blog, name='Blog'),
    path('Course-grid-2/', Curso, name='Course-grid-2'),

]