from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.staff_form, name='staff_insert'),
    path('<int:id>/', views.staff_form, name='staff_update'),
    path('list/', views.staff_list,name='staff_list'),
    path('delete/<int:id>/',views.staff_delete,name='staff_delete')
]