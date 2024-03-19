from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """
    Show all products and sort/search queries
    """
    products = Product.objects.all()
    query = None
    categories = None
    title = 'Products'

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            title = categories[0].name.capitalize()

            if len(categories) == Category.objects.count():
                title = 'Products' 

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please add a valid search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(category__name__icontains=query) | Q(description__icontains=query) | Q(name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'title': title,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Show individual product detail
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
