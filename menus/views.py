from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Item
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ItemForm
from django.views.generic.edit import FormView






class ItemListView(ListView):
    model = Item
    template_name = 'menus/item_list.html'
    context_object_name = 'items'
    ordering = ['name']  # Specify the ordering of the list

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug is None:
            return Item.objects.all()
        queryset = Item.objects.filter(
            Q(category__icontains=slug) | Q(location__icontains=slug) | Q(name__icontains=slug)
        )
        return queryset
    


class ItemDetailView(DetailView):
    model = Item
    template_name = 'menus/item_detail.html'
    context_object_name = 'item'






class AddItemView(LoginRequiredMixin, FormView):
    template_name = 'menus/add_item.html'  # Update with the correct template path
    form_class = ItemForm
    success_url = '/item_list'  # Update with the correct view name
    login_url = '/admin/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user to the user field
        if super().form_valid(form):
            form.save()
            return redirect('/')
        else:
            return redirect('/admin/')
    