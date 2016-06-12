from django.shortcuts import render
from django.shortcuts import render_to_response
from inventory.models import Author
from inventory.models import Book
from inventory.models import Compartment
from inventory.models import DVD
from inventory.models import Genre
from inventory.models import Language
from inventory.models import Media
from inventory.models import Room
from inventory.models import Shelf
from inventory.models import Tag

def listview(request, items_from_db):
    items = []
    class Item():
        id = None
        category = None
        title = None
        subtitle = None
        text = None
        image = None

    for i in items_from_db:
        item = Item()
        item.id = i.pk
        item.category = i.category
        item.title = i.title
        item.subtitle = i.author
        item.text = i.description
        item.image = i.cover
        items.append(item)

    context = {
            "bookcount": len(Book.objects.all()),
            "dvdcount": len(DVD.objects.all()),
            "items": items,
            }
    return render_to_response('inventory/list.html', context)
    
def home(request):
    items_from_db = []
    # get the objects
    books = Book.objects.order_by('?')[:5]
    movies = DVD.objects.order_by('?')[:5]
    for b in books:
        items_from_db.append(b)
    for m in movies:
        items_from_db.append(m)
    items_from_db = [x for x in items_from_db if x != None]
    print("HOME")
    print(items_from_db)

    return listview(request, items_from_db)
    
    
