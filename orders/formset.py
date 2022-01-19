from django.forms import inlineformset_factory
from .models import Product, Turtles
from .forms import TurtleForm

TurtleFormset = inlineformset_factory(Product, Turtles, form=TurtleForm)

# followed here 
# https://stackoverflow.com/questions/31323497/combine-two-models-with-onetoone-relationship-into-one-form-django