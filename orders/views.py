from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Product
from .forms import ProductForm


class productsView(ListView):
    model = Product
    template_name = "orders/view_products.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "orders/product_detail.html"


class AddProduct(SuccessMessageMixin, CreateView):
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


class EditProduct(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'orders/edit_products.html'
    success_message = "Successfully updated '%(title)s'"

    def get_success_url(self):
        return reverse('view_product', kwargs={'slug': self.object.slug})

