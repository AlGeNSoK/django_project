from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_page = request.GET.get('sort')
    print(sort_page)
    if sort_page is None:
        phones_all = Phone.objects.all()
        context = {'phones': phones_all}

    if sort_page == 'name':
        phones = Phone.objects.order_by('name')
        context = {'phones': phones}
        # return render(request, 'template')

    if sort_page == 'min_price':
        phones = Phone.objects.order_by('price')
        context = {'phones': phones}

    if sort_page == 'max_price':
        phones = Phone.objects.order_by('-price')
        context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
