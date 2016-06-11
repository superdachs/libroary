from django.contrib import admin
from inventory.models import Author
from inventory.models import Book
from inventory.models import Compartment
from inventory.models import DVD
from inventory.models import Language
from inventory.models import Media
from inventory.models import Shelf
from inventory.models import Tag
from inventory.models import Room
from inventory.models import Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Compartment)
admin.site.register(DVD)
admin.site.register(Language)
#admin.site.register(Media)
admin.site.register(Shelf)
admin.site.register(Tag)
admin.site.register(Room)
admin.site.register(Genre)

