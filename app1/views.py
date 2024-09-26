from django.shortcuts import render, redirect # type: ignore
from .models import Item
from .forms import ItemForm  # We'll define this form in the next step


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)  # Add request.FILES to handle image upload
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app1/item_form.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'app1/item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'app1/item_detail.html', {'item': item})

def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)  # Handle image upload
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app1/item_form.html', {'form': form})


def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app1/item_confirm_delete.html', {'item': item})
