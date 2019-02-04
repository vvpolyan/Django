from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #template = Template(
        #'Hello {{ name }}'
    #)
    #context = Context({
        #'name': 'Anton'
    #})
    return render(
        request,
        'main/index.html'
    )
    #template = get_template(
        #'main/index.html'
    #)
    #context = Context({
        #'name': 'Anton'
    #})
    #return HttpResponse(
        #template.render(context)
    #)


def contact (request):
    return render(
        request,
        'main/contact.html'
    )

def catalog (request):
    return render(
        request,
        'main/catalog.html'
    )