# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404,redirect,render_to_response
from product.models import Product
from localsite.models import Matiere,Fabricant

def my404view(request):
    return redirect('/')

from product.models import Category

def home(request):
    rdict ={}
    rdict['int_cats'] = Category.objects.filter(parent__slug='collections-interieur')
    rdict['ext_cats'] = Category.objects.filter(parent__slug='collections-exterieur')
    return render_to_response('shop/index.html',rdict,RequestContext(request))


def matiere_list(request, slug):
    rdict ={}
    matiere = Matiere.objects.get(slug=slug)
    rdict['category'] = {'name':matiere.name, 'description':matiere.description}
    rdict['products'] = Product.objects.filter(matiere__slug=slug)
    return render_to_response('product/category.html', rdict, context_instance=RequestContext(request))

def fabricant_list(request, slug):
    rdict ={}
    fabricant = Fabricant.objects.get(slug=slug)
    rdict['category'] = {'name':fabricant.name, 'description':fabricant.description}
    rdict['logo'] = fabricant.picture
    rdict['products'] = Product.objects.filter(fabricant__slug=slug)
    return render_to_response('product/category.html', rdict, context_instance=RequestContext(request))
