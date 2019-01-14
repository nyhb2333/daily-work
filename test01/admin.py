# -*- coding:utf-8 -*-
from django.contrib import admin
from models import MobileBrand,MobileProduct
# Register your models here.

class MobileProductInline(admin.TabularInline):
    model = MobileProduct
    extra = 3  # 定义3个对象


class MobileBrandAdmin(admin.ModelAdmin):
    search_fields = ['brand_text']
    list_filter = ['create_date']
    list_display = ('brand_text', 'country_text', 'create_date', 'sales', 'thumbs', 'haopins')
    fieldsets = [
            (None, {'fields': ['brand_text','country_text', 'create_date']}),
            ('number information', {'fields': ['sales','thumbs','haopins']}),
        ]
    inlines = [MobileProductInline]


admin.site.register(MobileProduct)
admin.site.register(MobileBrand,MobileBrandAdmin)
