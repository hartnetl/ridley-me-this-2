from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Product
from .forms import ProductForm


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    # Help with these functions
    # https://stackoverflow.com/questions/59630997/correct-implementation-of-userpassestestmixin-or-accessmixin-in-class-based-view 

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


class productsView(ListView):
    model = Product
    template_name = "orders/view_products.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "orders/product_detail.html"


class AddProduct(SuperUserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'orders/add_product.html'
    success_message = "Successfully added '%(title)s'"

    def get_success_url(self):
        return reverse('view_product', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.creator = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)


class EditProduct(SuperUserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'orders/edit_products.html'
    success_message = "Successfully updated '%(title)s'"

    def get_success_url(self):
        return reverse('view_product', kwargs={'slug': self.object.slug})


@login_required
def delete_product(request, slug):
    # user must be superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
