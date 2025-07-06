from django.shortcuts import render, get_object_or_404, redirect
from .models import Burger, Category, OrderItem
from .forms import OrderForm
from django.contrib import messages


def home(request, category_id=None):
    categories = Category.objects.all()
    burgers = Burger.objects.all()

    if category_id:
        burgers = burgers.filter(category_id=category_id)

    return render(request, 'burger/home.html', {
        'burgers': burgers,
        'categories': categories,
        'selected_category': category_id,
    })


def burger_detail(request, pk):
    burger = get_object_or_404(Burger, pk=pk)
    related_burgers = Burger.objects.exclude(pk=pk)[:4]
    return render(request, 'burger/burger_detail.html', {
        'burger': burger,
        'related_burgers': related_burgers,
    })


def add_to_cart(request, pk):
    burger = get_object_or_404(Burger, pk=pk)
    cart = request.session.get('cart', {})

    pk_str = str(pk)
    if pk_str in cart:
        cart[pk_str] += 1
    else:
        cart[pk_str] = 1

    request.session['cart'] = cart
    messages.success(request, f"{burger.name} added to cart!")
    return redirect('burger_detail', pk=pk)


def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for key, quantity in cart.items():
        try:
            burger_id = int(key)
            burger = Burger.objects.get(pk=burger_id)
            item_total = burger.price * quantity
            total_price += item_total

            cart_items.append({
                'burger': burger,
                'quantity': quantity,
                'item_total': item_total
            })
        except Burger.DoesNotExist:
            continue

    return render(request, 'burger/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def increase_quantity(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        cart[str(pk)] += 1
        request.session['cart'] = cart
    return redirect('cart')


def decrease_quantity(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        if cart[str(pk)] > 1:
            cart[str(pk)] -= 1
        else:
            del cart[str(pk)]  # remove item if quantity goes to 0
        request.session['cart'] = cart
    return redirect('cart')


def checkout_view(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart')

    cart_items = []
    total_price = 0

    for key, quantity in cart.items():
        try:
            burger_id = int(key)
            burger = Burger.objects.get(pk=burger_id)
            item_total = burger.price * quantity
            total_price += item_total

            cart_items.append({
                'burger': burger,
                'quantity': quantity,
                'item_total': item_total
            })
        except Burger.DoesNotExist:
            continue

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    burger=item['burger'],
                    quantity=item['quantity'],
                    item_total=item['item_total']
                )

            request.session['cart'] = {}
            messages.success(request, "Order placed successfully!")
            return redirect('home')
    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'burger/checkout.html', context)

