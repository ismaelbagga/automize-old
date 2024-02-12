from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('blog/', views.blog_view, name="blog"),
    path('blog_sample/', views.blog_sample_view, name="blog_sample"),
    path('contact/', views.contact_view, name="contact"),
    path('portfolio/', views.portfolio_view, name="portfolio"),
    path('portfolio_sample/', views.portfolio_sample_view, name="portfolio_sample"),
    path('services/', views.services_view, name="services"),
    path('service_design_sample/', views.service_design_sample_view, name="service_design_sample"),
    path('services/web_development/', views.web_dev, name="web_dev"),
    path('services/mobile/', views.mobile, name="mobile_dev"),
    path('services/digital_marketing/', views.digital_marketing, name="digital_marketing"),
    path('technologies/android/', views.android, name="android"),
    path('technologies/ios/', views.ios, name="ios"),
]
