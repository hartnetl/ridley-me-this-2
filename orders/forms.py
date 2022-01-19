from django import forms
from django.forms import inlineformset_factory
from .widgets import CustomClearableFileInput
from .models import Product, Category, Turtles


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'sku', 'title', 'price', 'description', 'image_url', 'image', 'slug']

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    

    # override the init method to make changes to the fields 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # After getting all the categories, create a list of tuples of the 
        # friendly names associated with their category ids using list
        # comprehension. This is just a shorthand way of creating a for loop that adds items to a list.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Use friendly names instead of id
        self.fields['category'].choices = friendly_names
        # Add style classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class TurtleForm(forms.ModelForm):
    class Meta:
        model = Turtles
        fields = ['species', 'sponsored_status']


