from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """
    Show all products and sort/search queries
    """
    products = Product.objects.all()
    query = None
    categories = None
    title = 'Products'
    sort_by = request.GET.get('sort_by')

    if request.GET:
        if 'sort_by' in request.GET:
            if sort_by == 'name_asc':
                products = products.order_by('name')
            elif sort_by == 'name_desc':
                products = products.order_by('-name')
            elif sort_by == 'price_asc':
                products = products.order_by('price')
            elif sort_by == 'price_desc':
                products = products.order_by('-price')
            elif sort_by == 'category_asc':
                products = products.order_by('category__name')
            elif sort_by == 'category_desc':
                products = products.order_by('-category__name')
        if sort_by == 'reset':
            sort_by = None

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
        'sort_by': sort_by,
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


def add_products(request):
    """
    Add products to the site
    """
    form = ProductForm()

    return render(request, 'products/add_products.html', {'form': form})
