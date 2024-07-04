from django.contrib import admin
from django.urls import path

from bboard.views import index, by_rubric, BbCreateView, BbUpdateView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('change/<int:pk>/', BbUpdateView.as_view(), name='update'),
]