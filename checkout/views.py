from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J30RyAyvKhrXxat4PHB9KPZYZ4jICzSZmlZW0tliidqthrZ3ElTWhOwJARw8YerxTalC5OmrDIm4u2i4G2vDgxy00JsYtqelM',
        'client_secret': 'sk_test_51J30RyAyvKhrXxatGVOlktbl7heAzUDkoZwb0H21OM0Mu9c727NpwyZINm7jQAZEBxuBTHlbRAVC4GXYEy32Syqw00CmBW208w',
    }

    return render(request, template, context)
