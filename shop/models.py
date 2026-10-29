from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="stores"
    )
    store_name = models.CharField(max_length=150)
    description = models.TextField()
    store_image = models.ImageField(
        upload_to="stores/",
        blank=True,
        null=True
    )
    store_owner = models.IntegerField()

    def __str__(self):
        return self.store_name


class Product(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="products"
    )
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    product_image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.product_name


class Review(models.Model):
    user = models.IntegerField()
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} - Store {self.store_id}"
