from django.db.models import Model, CharField, ImageField, PositiveIntegerField, ForeignKey, FloatField, TextField, CASCADE


class Category(Model):
    name = CharField(max_length=120)
    parent = ForeignKey('self', CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=1000)
    price = FloatField()
    discount = PositiveIntegerField()
    color = CharField(max_length=30, null=True, blank=True)
    short_description = TextField()
    description = TextField()
    quantity = PositiveIntegerField(default=1)
    category = ForeignKey('products.Category', CASCADE, related_name='products')


class ProductImage(Model):
    image = ImageField(upload_to='products')
    Product = ForeignKey('products.Product', CASCADE, related_name='images')