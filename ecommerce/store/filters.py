from django.db.models import fields, Q
import cv2
import pytesseract

import django_filters

from .models import *
from functools import reduce

import operator
# from django.db import Q


class Pic2Filter(django_filters.FilterSet):

    # Text Detection

    img = cv2.imread('CV/static/images/IMG_1159.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hImg,wImg,_ = img.shape
    boxes = pytesseract.image_to_data(img)
    lst = []
    for x,b in enumerate(boxes.splitlines()):
        if x!=0:
            b = b.split()
            
            if len(b)==12:
                
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                detected_text = b[11]
                lst.append(detected_text)
    #Product identification
    
    products =   Product.objects.values_list('name', flat=True)
   


    d = [x.lower() for x in lst]
    # make dict of list with less elements
    search_result = []


    
    for m in products:


# search against bigger list  
        if m.lower() in d: 

            searched_name = Product.objects.filter(name__iexact=m)
            search_result += searched_name
    # print(search_result)
    
    # class Meta:
    #     model = Product
    #     fields = ['name']


class StoreFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Product Name')

    class Meta:
        model = Product
        fields = ['name']


        