from distutils.command.upload import upload
from django.db import models
# Create your models here.
class Service(models.Model):
    s_name = models.CharField(max_length=50)
    s_img = models.ImageField(upload_to="serpic",blank=True)

    def __str__(self):
        return self.s_name

# ทำความสะอาด
class S_Cleaning(models.Model):
    S_Cle_area = models.CharField(max_length=50)
    S_Cle_area_price = models.IntegerField(max_length=10)
    S_Cle_itme = models.IntegerField(max_length=10)
    S_Cle_itme_price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.S_Cle_area 


# กำจัดไรฝุ่น
class S_Eliminate(models.Model):
    S_Eli_itme = models.CharField(max_length=50)
    S_Eli_itme_price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.S_Eli_itme


# รีดผ้า
class S_Ironing(models.Model):
    S_Iron_item = models.CharField(max_length=50)
    S_Iron_itme_price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.S_Iron_item


# จัดสวน
class S_Iandscping(models.Model):
    S_Ian_area = models.CharField(max_length=50)
    S_Ian_area_price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.S_Ian_area


# นวด
class S_Massage(models.Model):
    S_Mass_itme = models.IntegerField(max_length=10)
    S_Mass_itme_price = models.IntegerField(max_length=10)



# ล้างสระว่ายน้ำ
class S_Pool(models.Model):
    S_Pool_item = models.CharField(max_length=50)
    S_Pool_item_price = models.IntegerField(max_length=10)

    def __str__(self):
        return self.S_Pool_item