from django.shortcuts import render
from django.views import generic
from .models import Item

# Gets data from database and display is to the frond end models
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_create")
    template_name = "index.html"

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"

