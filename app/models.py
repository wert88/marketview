from django.db import models
from django.shortcuts import render, reverse
from django.conf import settings

CATEGORY_CHOICES = (
    ('S', 'Sports'),
    ('H', 'Health & Beauty'),
    ('B', 'Books'),
	('MF', 'Men Fashion'),
	('WF', 'Women Fashion'),
	('PH', 'Phones & Tablets'),
	('K', 'Kids & Babies'),
	('L', 'Laptops & PCs')
)

LABEL_CHOICES = (
	('A', ''),
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1,)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()
    image2 = models.ImageField(default="blank")
    image3 = models.ImageField(default="blank")
    image4 = models.ImageField(default="blank")
    Buy_url = models.TextField(default='#')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse("app:product", kwargs = {'slug': self.slug})
	   