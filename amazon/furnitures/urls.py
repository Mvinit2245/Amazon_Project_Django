from django.urls import path
from furnitures import views


urlpatterns = [
    path("", views.home, name="home"),
    path('update/<int:id>/',views.update_product, name='update_product'),
    path("delete_product/<int:id>", views.delete_product, name="delete_product"),
    
]