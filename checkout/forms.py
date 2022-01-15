from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
        }

        # set cursor 
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            # If the field is required, add a star 
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # set placeholder values as per above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add the css class we haven't created yet
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove labels
            self.fields[field].label = False
    

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='Choose country...').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=True)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='Choose country...').formfield(
        required=True,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=True)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES, required=True)


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
