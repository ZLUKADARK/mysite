from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
<<<<<<< HEAD
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
=======
>>>>>>> 4a8502e26d49c16bc3553844a31aef4c03dd1611
]