from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'index.html')


def headers_view(request):
    return render(request, 'headers.html')


def footers_view(request):
    return render(request, 'footers.html')


def cards_view(request):
    return render(request, 'cards.html')


def buttons_view(request):
    return render(request, 'buttons.html')


def components_view(request):
    return render(request, 'components.html')


def typography_view(request):
    return render(request, 'typography.html')


def headings_view(request):
    return render(request, 'headings.html')


def portfolio_components_view(request):
    return render(request, 'portfolio_components.html')


def blog_components_view(request):
    return render(request, 'blog_components.html')


def services_components_view(request):
    return render(request, 'services_components.html')



def docs_page(request):
    return render(request, 'docs_page.html')


def bank_view(request):
    return render(request, 'blank.html')


def test_view(request):
    return render(request, 'elements/test.html')


# =====> returns components
# headers
def header1_view(request):
    return render(request, 'elements/headers/header1.html')


# footers
def footer1_view(request):
    return render(request, 'elements/footers/footer1.html')


# cards
def info_card_view(request):
    return render(request, 'elements/cards/info_card.html')


# buttons
def button_primary_view(request):
    return render(request, 'elements/buttons/primary_button.html')


def button_white_view(request):
    return render(request, 'elements/buttons/white_button.html')


def button_secondary_view(request):
    return render(request, 'elements/buttons/secondary_button.html')


def button_base_view(request):
    return render(request, 'elements/buttons/base_button.html')


# headings
def heading_big_view(request):
    return render(request, 'elements/headings/big_heading.html')


def heading_medium_view(request):
    return render(request, 'elements/headings/medium_heading.html')


def heading_small_view(request):
    return render(request, 'elements/headings/small_heading.html')


# typography
def typography_hx_view(request):
    return render(request, 'elements/typography/hx.html')