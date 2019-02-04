from django.urls import path #index, contact, catalog
#from django.conf.urls.static import static
#from django.conf import settings

from .views import (product_list_view_1, product_list_view_2, product_list_view_3)


urlpatterns = [
    path('Page_1/', product_list_view_1),
    path('Page_2/', product_list_view_2),
    path('Page_3/', product_list_view_3),

]