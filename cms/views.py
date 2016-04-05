from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

# Create your views here.

def new_page(request, page_name):

    page = Pages(name=page_name, page='You are in the page ' + page_name)  
    page.save()

    return HttpResponse(page.page)
