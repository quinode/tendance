# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404,redirect,render_to_response


def my404view(request):
    return redirect('/')

from product.models import Category

def home(request):
    rdict ={}
    rdict['test'] = 'coucou'
    rdict['int_cats'] = Category.objects.filter(parent__slug='collections-interieur')
    rdict['ext_cats'] = Category.objects.filter(parent__slug='collections-exterieur')
    return render_to_response('shop/index.html',rdict,RequestContext(request))
