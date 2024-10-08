from django.urls import path
from .views import index, single

urlpatterns = [
    path('', index, name='index'),
    path('blog-single/', single, name='single')
]
