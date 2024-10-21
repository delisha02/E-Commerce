from django.urls import path
from . import views

urlpatterns = [
    # Redirect base URL to the login page
    path('', views.login_view, name='login'),  # Set login_view as the default
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('store/', views.store, name='store'),  # Make sure to keep 'store' as a separate path
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]
