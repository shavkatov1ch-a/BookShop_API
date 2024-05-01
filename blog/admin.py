from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_display_links = ('name', 'author')


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(About)
admin.site.register(Profile)
admin.site.register(User)