from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('student/<int:student_id>/', views.DetailPageView.as_view(), name='details'),
]
