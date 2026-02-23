from django.shortcuts import render


def catalog(request):
    return render(request, "home.html")


def catalog_con(request):
    return render(request, "contacts.html")
