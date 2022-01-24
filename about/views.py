from django.shortcuts import render

def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')


def learn(request):
    """ A view to return the about page """

    return render(request, 'about/learn.html') 
