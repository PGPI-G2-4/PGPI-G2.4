from django.urls import include, path

from . import views

app_name = "terms"

urlpatterns = [
    path("", views.terms, name="terms"),
    
]
