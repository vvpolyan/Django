from django.shortcuts import render

def product_list_view_1(request):
    return render(
        request,
        'products/page_1.html'
    )

def product_list_view_2(request):
    return render(
        request,
        'products/page_2.html'
    )

def product_list_view_3(request):
    return render(
        request,
        'products/page_3.html'
    )