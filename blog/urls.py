from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<slug:slug>', views.post_detail, name='post_detail_url'),
    path('category_detail/<slug:slug>', views.category_detail, name='category_detail_url'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login_site, name='login_site'),
    path('logout/', views.logout_site, name='logout_site'),
    path('post_detail/<slug:slug>/comment/', views.comment, name='comment'),
]