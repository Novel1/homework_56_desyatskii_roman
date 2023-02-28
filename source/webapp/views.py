from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProductForm
from webapp.models import Product, CategoryChoice


# Create your views here.

def index(request):
    products = Product.objects.exclude(is_deleted=True).order_by('category', 'name').filter(remainder__gt=0)
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)


def product_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponseNotFound('No Found')
    return render(request, 'inform.html', context={
        'product': product
    })


def add_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add.html', context={'choices': CategoryChoice.choices, 'form': form})
    form = ProductForm(data=request.Post)
    if not form.is_valid():
        return render(request, 'add.html', context={'choices': CategoryChoice.choices, 'form': form})
    else:
        Product.objects.create(**form.cleaned_data)
        return redirect('index')


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.image = request.POST.get('image')
        product.remainder = request.POST.get('remainder')
        product.save()
        return redirect('product_view', pk=product.pk)
    return render(request, 'product_update.html',
                  context={
                      'product': product,
                      'choices': CategoryChoice.choices
                  })


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    book = get_object_or_404(Product, pk=pk)
    book.delete()
    return redirect('index')
