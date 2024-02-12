from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'amStaticApp/home.html')


def about_view(request):
    return render(request, 'amStaticApp/about.html')


def blog_view(request):
    return render(request, 'amStaticApp/blog.html')


def blog_sample_view(request):
    return render(request, 'amStaticApp/blog_sample.html')


def contact_view(request):
    return render(request, 'amStaticApp/contact.html')


def portfolio_view(request):
    return render(request, 'amStaticApp/portfolio.html')


def portfolio_sample_view(request):
    return render(request, 'amStaticApp/portfolio_sample.html')


def services_view(request):
    return render(request, 'amStaticApp/services.html')


def service_design_sample_view(request):
    return render(request, 'amStaticApp/service_design_sample.html')


def web_dev(request):
    return render(request, 'amStaticApp/services/web_dev.html')


def mobile(request):
    return render(request, 'amStaticApp/services/mobile.html')