
from django.urls import path #index, contact, catalog
#from django.conf.urls.static import static
#from django.conf import settings

from .views import (index, contact, catalog)


urlpatterns = [

    #path('index/', index), #'index/' можно переназначать на пользовательское значение
    path('contact/', contact),
    path('catalog/', catalog),
    path('', index)
]