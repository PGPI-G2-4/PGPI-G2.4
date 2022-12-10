from django.urls import path

from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.product_all, name="store_home"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("<slug:slug>/<int:appointment_id>", views.product_detail, name="product_detail"),
    path("shop/<str:name>/", views.category_list, name="category_list"),
    path('event/new/', views.event, name='event_new'),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    path("set_session_email/", views.set_session_email, name="set_session_email"),
    
]
