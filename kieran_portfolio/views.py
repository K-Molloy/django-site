from django.shortcuts import render


def kieran_portfolio_view(request):
    template = 'portfolio/portfolio.html'
    return render(request, template)
