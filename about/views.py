from django.shortcuts import render


def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')


def learn(request):
    """ A view to return the learn more page """

    return render(request, 'about/learn.html')


def disclaimer(request):
    """ A view to return the disclaimer page """

    return render(request, 'about/disclaimer.html')
