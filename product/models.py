from django.db import models


# Create your models here.
class ProductModel(models.Model):
    class Meta:
        db_table = "Products"

    p_name = models.CharField(max_length=256, null=False)
    category = models.CharField(max_length=256, null=False)
    image = models.ImageField(blank=True, upload_to="images", null=True)
    desc = models.TextField()
    price = models.CharField(max_length=256, null=False)
    count = models.CharField(max_length=6, null=False)
    # 상품 이름, 상품 카테고리, 이미지, 설명, 가격, 재고량


class Category(models.Model):
    class Meta:
        db_table = "categories"

    category = models.CharField(max_length=256)
    desc = models.TextField(max_length=256, blank=True)