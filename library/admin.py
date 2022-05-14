from django.contrib import admin
from .models import Book,Client,IssuedBook
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
