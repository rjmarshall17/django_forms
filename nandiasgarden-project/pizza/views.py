from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza_pk = filled_form.save().id
            note = 'Thank-you for your order. '
            note += 'Your %s %s and %s pizza is on its way' % (str(filled_form.cleaned_data.get('size')).lower(),
                                                               filled_form.cleaned_data.get('topping1'),
                                                               filled_form.cleaned_data.get('topping2'))
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Your order has failed. Please try again.'
        return render(request, 'pizza/order.html', {'pizza_form':filled_form,
                                                    'note': note,
                                                    'multiple_form': multiple_form,
                                                    'created_pizza_pk': created_pizza_pk})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizza_form': form,
                                                    'multiple_form': multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data.get('number')
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data.get('topping1'))
            note = 'Pizzas have been ordered'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html', {'note': note,
                                                     'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = "Order has been updated. Your %s with %s and %s is on its way." % (
                str(filled_form.cleaned_data.get('size')).lower(),
                filled_form.cleaned_data.get('topping1'),
                filled_form.cleaned_data.get('topping2')
            )
        return render(request, 'pizza/edit_order.html', {'pizza_form': form,
                                                         'pizza': pizza,
                                                         'note': note})
    return render(request, 'pizza/edit_order.html', {'pizza_form': form,
                                                     'pizza': pizza})

