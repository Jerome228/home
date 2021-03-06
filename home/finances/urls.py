from django.contrib import admin
from django.urls import path
from . import views

app_name = "finances"
urlpatterns = [
    path('', views.index, name='index'),
    path('depenses/', views.ExpensList.as_view(), name="expenses_list"),
    path('depenses/ajouter', views.ExpensCreate.as_view(), name="expens_add"),
    path('depenses/<int:pk>/',
         views.ExpensDetailView.as_view(), 
         name="expens_detail"),
    path('depenses/modifier/<int:pk>', views.ExpensUpdate.as_view(), name="expens_update"),
    path('depenses/suppression/<int:pk>', views.ExpensDelete.as_view(), name="expens_delete"),
    path('api/chartJSON', views.expensChart, name='chart_json'),
]
