from django.urls import include, path

from . import views

app_name = "checkout"

urlpatterns = [
    path("deliverychoices", views.deliverychoices, name="deliverychoices"),
    path("basket_update_delivery/", views.basket_update_delivery, name="basket_update_delivery"),
    path("delivery_address/", views.delivery_address, name="delivery_address"),
    path("payment_selection/", views.payment_selection, name="payment_selection"),
    path("payment_successful/", views.payment_successful, name="payment_successful"),
    path("update_email/", views.update_email, name="update_email"),
    path("update_email2/", views.update_email2, name="update_email2"),
    path("rellenar_info/", views.rellenar, name="rellenar"),
]
