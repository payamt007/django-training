from django.contrib import admin
from .models import Category, Ingredient


class CategoryModelAdmin(admin.ModelAdmin):
    fields = "__all__"
    #fields = ('country', 'province', 'title', 'type')
    #list_display = ('id','tag', 'province', 'en_title', 'fa_title', 'type', 'active')
    #ordering = ('tag',)


class IngredientModelAdmin(admin.ModelAdmin):
    fields = "__all__"


admin.site.register(Category)
admin.site.register(Ingredient)

# admin.site.register(User)

# Register your models here.
