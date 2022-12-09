from django.urls import path

from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.product_all, name="store_home"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_name>/", views.category_list, name="category_list"),
    path("catalogue/medics", views.listar_medico, name="listar_medico"),
    path('event/new/', views.event, name='event_new'),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    
]
