from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Goods, Category

class GoodsListView(ListView):
    model = Goods
    template_name = 'index.html'
    category = Category






def electronicPageView(request):
    context = {


    }

    return render(request, 'electronic.html', context)




def fashionPageView(request):
    context = {

    }

    return render(request, 'fashion.html', context)



def jewelleryPageView(requst):
    context = {

    }

    return render(requst, 'jewellery.html', context)


class GoodsUpdateView(UpdateView):
    model = Goods
    fields = ('name', 'price', 'category', )
    template_name = 'crud/goods_edit.html'


class GoodsDeleteView(DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = reverse_lazy('index')


class GoodsCreateView(CreateView):
    model = Goods
    fields = ('name', 'price', 'image', 'category', )
    template_name = 'crud/goods_create.html'



