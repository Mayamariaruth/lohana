from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
from profiles.models import UserProfile

import stripe
import json


# Create your views here.
@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data view
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'We are very sorry but your payment is not able \
            to be processed at this moment. Please try again later.'
        )
        return HttpResponse(status=400)


def checkout(request):
    """
    Checkout view
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        quantity = item_data
                    else:
                        try:
                            quantity = item_data['quantity']
                        except (KeyError, TypeError):
                            messages.error(
                                request,
                                "Invalid quantity data in the bag. \
                                    Please contact support."
                            )
                            continue
                    order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag doesn't exist."
                        "Please contact us for help!"))
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                           Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'There is nothing in your bag.')
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form_initial = {
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.user_phone_number,
                    'country': profile.user_country,
                    'postcode': profile.user_postcode,
                    'town_or_city': profile.user_town_or_city,
                    'street_address1': profile.user_street_address1,
                    'street_address2': profile.user_street_address2,
                    'county': profile.user_county,
                }
            except UserProfile.DoesNotExist:
                order_form_initial = {}
        else:
            order_form_initial = {}

        order_form = OrderForm(initial=order_form_initial)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                         Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts and save user info
    """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        save_info = request.session.get('save_info')
        if save_info:
            profile.user_phone_number = order.phone_number
            profile.user_country = order.country
            profile.user_postcode = order.postcode
            profile.user_town_or_city = order.town_or_city
            profile.user_street_address1 = order.street_address1
            profile.user_street_address2 = order.street_address2
            profile.user_county = order.county
            profile.save()

    messages.success(request,
                     f'Order processed! Your order number is {order_number}. '
                     f'A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    return render(request, 'checkout/checkout_success.html', {'order': order})
