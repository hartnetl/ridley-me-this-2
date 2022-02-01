# import this file https://github.com/django/django/blob/main/django/forms/
# widgets.py
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# create a custom class which inherits from the original one
class CustomClearableFileInput(ClearableFileInput):
    # override these settings
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'orders/custom_widget_templates/custom_clearable_file_input.html'
