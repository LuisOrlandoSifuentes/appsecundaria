from django.shortcuts import render

# Create your views here.

def Index_visual(request):
    return render(request,"index.html")