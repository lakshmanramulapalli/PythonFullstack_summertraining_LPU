from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'ecommerce/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecommerce/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'price', 'description', 'stock_quantity']
    template_name = 'ecommerce/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'price', 'description', 'stock_quantity']
    template_name = 'ecommerce/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'ecommerce/product_delete.html'
    success_url = reverse_lazy('product_list')
