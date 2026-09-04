from django.shortcuts import render


def home(request):
    """Display the MISHI-ERP foundation page."""
    return render(request, "home.html")

