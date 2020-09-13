from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add', views.add, name='add_student'),
    path('show', views.show, name='show_student'),
    path('edit/<std_id>', views.edit, name='edit_student'),
]
