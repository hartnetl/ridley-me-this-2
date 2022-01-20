from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm, TurtleForm
from .formset import TurtleFormset


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    # Help with these functions
    # https://stackoverflow.com/questions/59630997/correct-implementation-of-userpassestestmixin-or-accessmixin-in-class-based-view 

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


# class productsView(ListView):
#     model = Product
#     template_name = "orders/view_products.html"

#     def get_queryset(self):
#         query = self.kwargs.get('name', '')
#         object_list = self.model.objects.all()
#         if name:
#             object_list = object_list.filter(name__icontains=name)
#         return object_list

def products_view(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    species = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(turtle__species__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # query for sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'

            # if sort is there, also check for direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'orders/view_products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "orders/product_detail.html"


@login_required
def AddProduct(request):
    # user must be superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_form = ProductForm()
    turtle_details_formset = TurtleFormset()

    if request.method == 'POST':
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            turtle_details_formset = TurtleFormset(request.POST, instance=product)

            if turtle_details_formset.is_valid():
                product_form.save()
                turtle_details_formset.save()
                messages.success(request, f"Successfully added '{product.title}'")
                return redirect(reverse('view_product', args=[product.slug]))
            else:
                turtle_details_formset = TurtleFormset(request.POST)
        else:
            messages.error(request, 'Failed to add product, please ensure form is filled correctly')
    else:
        product_form = ProductForm()

    context = {
        'product_form': product_form,
        'turtle_details_form': turtle_details_formset
    }
    return render(request, 'orders/add_product.html', context=context)


@login_required
def EditProduct(request, slug):
    # user must be superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    turtle_details_formset = TurtleFormset(product)

    if request.method == 'POST':
        print('IS THIS THE PROBLEM')
        product_form = ProductForm(request.POST, instance=product)

        if product_form.is_valid():
            print("PRODUCT FORM IS VALID")
            products = product_form.save(commit=False)
            turtle_details_formset = TurtleFormset(request.POST, instance=products)

            if turtle_details_formset.is_valid():
                print("TURTLE DETAILS FORM IS VALID")
                product_form.save()
                turtle_details_formset.save()
                messages.success(request, f"Successfully updated '{product.title}'")
                # return redirect('products')
                return redirect(reverse('view_product', args=[product.slug]))
            else:
                print("TURTLE FORM NOT VALID")
                messages.error(request, 'Failed to update product. Please ensure the form is valid.')
                turtle_details_formset = TurtleFormset(request.POST)
        else:
            messages.error(request, 'Failed to add product, please ensure form is filled correctly')
    else:
        print("PRODUCT FORM NOT VALID")
        product_form = ProductForm(instance=product)
        turtle_details_formset = TurtleFormset(instance=product)

    context = {
        'product_form': product_form,
        'turtle_details_form': turtle_details_formset,
        'product': product
    }
    return render(request, 'orders/edit_products.html', context=context)


# class AddProduct(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'orders/add_product.html'
#     success_message = "Successfully added '%(title)s'"

#     def get_success_url(self):
#         return reverse('view_product', kwargs={'slug': self.object.slug})


#     def get_context_data(self, **kwargs):
#         context = super(AddProduct, self).get_context_data(**kwargs)

#         if self.request.POST:
#             context['turtle_formset'] = TurtleFormset(self.request.POST)
#         else:
#             context['turtle_formset'] = TurtleFormset()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         turtle_details_form = context['TurtleFormset']
#         if turtle_details_form.is_valid():
#             self.object = form.save()
#             turtle_details_form.instance = self.object
#             turtle_details_form.save()
#             return redirect(reverse('view_product', args=[product.slug]))


# class AddProduct(SuperUserRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'orders/add_product.html'
#     success_message = "Successfully added '%(title)s'"

#     def get_success_url(self):
#         return reverse('view_product', kwargs={'slug': self.object.slug})

#     def form_valid(self, form):
#         form.instance.creator = self.request.user
#         print(form.cleaned_data)
#         return super().form_valid(form)


# class EditProduct(SuperUserRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'orders/edit_products.html'
#     success_message = "Successfully updated '%(title)s'"

#     def get_success_url(self):
#         return reverse('view_product', kwargs={'slug': self.object.slug})

@login_required

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
