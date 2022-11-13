from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("correspondencia/", views.index, name='correspondencia'),
    path('correspondencia/<int:residencia_id>/', views.residencia, name='residencia'),
]
