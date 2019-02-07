from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #template = Template(
        #'Hello {{ name }}'
    #)
    #context = Context({
        #'name': 'Anton'
    #})
    #return render(
        #request,
        #'main/index.html'
    #)
    template = get_template('main/index.html')
    context = {'name': 'Виталий'}
    return HttpResponse(template.render(context))


#def contact (request):
    #return render(
        #request,
        #'main/contact.html'
    #)

def contact(request):
    rendered_page = render_to_string(
        'main/contact.html',
        {
            'contacts': [
                'Телефон: +7 (861) 000-00-00',
                'E-mail: smart_shoes@net.ru',

            ]
        }
    )
    return HttpResponse(
        rendered_page
    )

def catalog (request):
    return render(
        request,
        'main/catalog.html',
        {
            'about_text': 'Это страница Каталога'
        }
    )