# -*- coding: utf-8 -*-

from django.contrib import admin
from product.models import Product, Category
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from product.models import Category
from product.admin import CategoryOptions,ProductOptions

from tinymce.widgets import AdminTinyMCE
from django import forms

## Pour django 1.4
# from tendance.utils import SimpleListFilter
# 
# 
# class Catlevel(SimpleListFilter):
#     title = _('Catégorie niveau 1')
#     parameter_name = 'parent'
#     def lookups(self, request, model_admin):
#         return tuple(('1','truc'),('2','machin'))
#         #Category.objects.filter(parent=None).values_list('id','name')
#     def queryset(self, request, queryset):
#         return queryset.filter(parent=value)


class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=AdminTinyMCE(attrs={'cols':80,'rows':20}))
    class Meta:
        model = Category


class CategoryAdmin(CategoryOptions):
    form = CategoryAdminForm
    list_display = ('name', '_parents_repr', 'is_active')
    list_display_links = ('name',)
    ordering = ['parent__id', 'ordering']
#    list_filter = (Catlevel,)
    
    filter_horizontal = ('related_categories',)
    
    def mark_active(self, request, queryset):
        queryset.update(is_active=True)
        return HttpResponseRedirect('')

    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)
        return HttpResponseRedirect('')
        
    mark_active.short_description = u"Activer les catégories sélectionnées"  
    mark_inactive.short_description = u"Désactiver les catégories sélectionnées" 

admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)