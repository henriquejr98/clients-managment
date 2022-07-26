from django.contrib import admin
from .models import Person, Product, Sale

class PersonAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), ('age', 'salary'), 'bio', 'photo')
    list_display = ('first_name', 'last_name', 'age', 'salary', 'photo')
    list_filter = ('age', 'salary')
    search_fields = ('first_name', 'last_name', 'age')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'get_total')
    list_filter = ('person',)
    autocomplete_fields = ('person',)
    raw_id_fields = ('person',)
    readonly_fields = ('total',)
    filter_horizontal = ('products',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
