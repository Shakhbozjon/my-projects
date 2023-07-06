from django.urls import path

from .views import GoodsListView, electronicPageView, jewelleryPageView, fashionPageView, GoodsDeleteView, GoodsUpdateView, GoodsCreateView

urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),
    path('goods/create/', GoodsCreateView.as_view(), name='goods_new'),
    path("goods/<int:pk>/delete/", GoodsDeleteView.as_view(), name='goods_delete'),
    path("goods/<int:pk>/edit/", GoodsUpdateView.as_view(), name='goods_edit'),
    path('electronic/', electronicPageView, name='electronic'),
    path('fashion/', fashionPageView, name='fashion'),
    path('jewellery/', jewelleryPageView, name='jewellery'),

]