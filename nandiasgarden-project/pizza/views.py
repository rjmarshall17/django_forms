from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thank-you for your order. '
            note += 'Your %s %s pizza is on its way' % (filled_form.cleaned_data.get('size').lower(),
                                                        ', '.join(filled_form.cleaned_data.get('toppings')))
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizza_form':new_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizza_form': form})
