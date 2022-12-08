from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.add,name="add"),
    path('done/<int:taskid>/',views.done,name="done"),
    path('edit/<int:taskid>/',views.edit,name="edit"),
]