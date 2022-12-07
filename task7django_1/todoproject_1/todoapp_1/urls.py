from django.urls import path
from todoapp_1 import views

urlpatterns = [
    path('',views.add,name='add'),
    path('list/',views.cgvlist.as_view(),name='list'),
    path('details/<int:pk>/',views.cgvdetail.as_view(),name='details'),
    path('update/<int:pk>/',views.cgvupdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.cgvdelete.as_view(),name='delete'),



]