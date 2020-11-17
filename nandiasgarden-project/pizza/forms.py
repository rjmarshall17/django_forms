from django import forms
from .models import Pizza, Size


# class PizzaForm(forms.Form):
#     toppings = forms.MultipleChoiceField(
#         choices=[
#             ('pepperoni', 'Pepperoni'),
#             ('cheese', 'Cheese'),
#             ('olives','Olives'),
#         ],
#         widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='size', choices=[('Small', 'Small'),
#                                                     ('Medium', 'Medium'),
#                                                     ('Large', 'Large')])


class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects,
    #                               empty_label=None,
    #                               widget= forms.RadioSelect)

    class Meta:
        model = Pizza
        fields = ('topping1', 'topping2', 'size')
        labels = {
                  'topping1': 'Topping 1',
                  'topping2': 'Topping 2',
                  }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
