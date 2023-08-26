from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.main_view),
    path('headers', views.headers_view, name="headers"),
    path('footers', views.footers_view, name="footers"),
    path('cards', views.cards_view, name="cards"),
    path('buttons', views.buttons_view, name="buttons"),
    path('typography', views.typography_view, name="typography"),
    path('headings', views.headings_view, name="headings"),
    path('components', views.components_view, name="components"),
    path('portfolio', views.portfolio_components_view, name="portfolio-components"),
    path('blog', views.blog_components_view, name="blog-components"),
    path('services', views.services_components_view, name="services-components"),
    path('docs_page', views.docs_page, name="docs_page"),
    path('blank', views.bank_view, name="blank"),
    # ====> return components
    path('test', views.test_view, name="test"),
    # headers
    path('header1', views.header1_view, name="header1"),
    # footers
    path('footer1', views.footer1_view, name="footer1"),
    # cards
    path('info-card', views.info_card_view, name="info-card"),
    # buttons
    path('button-primary', views.button_primary_view, name="button-primary"),
    path('button-white', views.button_white_view, name="button-white"),
    path('button-secondary', views.button_secondary_view, name="button-secondary"),
    path('button-base', views.button_base_view, name="button-base"),
    # headings
    path('heading-big', views.heading_big_view, name="heading-big"),
    path('heading-medium', views.heading_medium_view, name="heading-medium"),
    path('heading-small', views.heading_small_view, name="heading-small"),
    # typography
    path('typography-hx', views.typography_hx_view, name="typography-hx"),
]
