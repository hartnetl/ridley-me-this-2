from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = 'RIDLEY ME THIS USER HAS USED THE CONTACT FORM'
            email_message = f'A user has used the contact form. User: {form.cleaned_data["name"]}. Contact: {form.cleaned_data["email"]}. Message: {form.cleaned_data["message"]}.'
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, settings.ADMIN_EMAIL)
            return render(request, 'contact/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
