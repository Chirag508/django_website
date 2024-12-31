from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_home_page,name='home'),
    path('about/',views.show_about_us_page,name='about'),
    path('contact/',views.show_contact_us_page,name='contact'),
    path('blogs/',views.show_blogs_page,name='blogs'),
    path('blogs/<int:blog_id>/', views.show_blog_detail, name='blog_detail'),
    path('login/',views.show_login_page,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.show_registartion_page,name='register'),
    path('product/',views.show_product_page,name='product'),
    path('product/delete_product/<int:id>',views.delete_product_data,name='delete_product'),
    path('product/update_product/<int:id>',views.update_product_data,name='update_product'),
]
