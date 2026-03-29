from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
	categoryName = models.CharField(max_length=200, null=True)
	categoryImage = models.ImageField(upload_to='images/Categories/', null=True, blank=True)

	def __str__(self):
		return self.categoryName


class Product(models.Model):
	productName = models.CharField(max_length=200, null=True)
	categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	price = models.CharField(max_length=200, null=True)
	productDescript = RichTextUploadingField(null=True)
	weight = models.CharField(max_length=200, null=True)
	availability = models.CharField(max_length=200, null=True)
	shipping = models.CharField(max_length=200, null=True)
	productImage = models.ImageField(upload_to='images/Products/', null=True, blank=True)
	productDate = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.productName
