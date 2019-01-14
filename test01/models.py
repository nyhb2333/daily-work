# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class MobileBrand(models.Model):
    #id  标识
    #品牌名称
    brand_text=models.CharField(max_length=255)
    #所属国家
    country_text=models.CharField(max_length=255)

    #品牌总销量
    sales=models.IntegerField(null=True)

    #点赞总量
    thumbs=models.IntegerField(null=True)

    #好评总量
    haopins=models.IntegerField(null=True)

    #品牌日期
    create_date=models.DateField(null=True)



    #为了显示对象而自定义
    def __str__(self):
        # type = sys.getfilesystemencoding()
        return self.brand_text


#手机产品
class MobileProduct(models.Model):
    #id 标识
    product_text=models.CharField(max_length=255)
    scores=models.IntegerField()
    brand=models.ForeignKey(
        MobileBrand,
        on_delete=models.CASCADE,
        related_name='products',
        related_query_name='product'
    )

    class Meta:
        default_related_name='ps'
        ordering=['-scores']

    def __str__(self):
        return self.product_text
