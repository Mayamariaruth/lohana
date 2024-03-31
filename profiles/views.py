from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserDetailsForm
from checkout.models import Order


# Create your views here.
@login_required
def profile(request):
    """
    Render user profile
    """
    if request.user.is_superuser:
        messages.error(request, "You are not allowed to access user profiles.")
        return redirect('home')

    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist_items = profile.user.wishlist_items.all()

    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery details updated successfully!')
        else:
            messages.error(
                request,
                'Updating your delivery details failed. \
                    Please ensure all fields are valid.'
            )
    else:
        form = UserDetailsForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'on_profile': True,
        'wishlist_items': wishlist_items,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is your previous confirmation for order number {order_number} .'
        'The confirmation email was sent to your email on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
