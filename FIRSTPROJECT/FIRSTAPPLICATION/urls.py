from FIRSTPROJECT.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('post/', views.index2, name='index2'),
]

