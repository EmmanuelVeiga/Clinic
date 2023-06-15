from django.urls import path
from .views import CustomLoginView
from accounts import views

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),

]