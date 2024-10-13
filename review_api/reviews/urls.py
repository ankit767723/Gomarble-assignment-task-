from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('api/reviews/', views.ReviewsAPI.as_view()),  # Capture URL as a query parameter
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]