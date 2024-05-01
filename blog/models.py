from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=212)
    password = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=212, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='books')
    author = models.CharField(max_length=212)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    page_count = models.CharField(max_length=212)
    short_desc = models.CharField(max_length=212)
    price = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.CharField(max_length=212)
    phone = models.CharField(max_length=211)
    address = models.CharField(max_length=211)
    note = models.TextField()
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client


class Profile(models.Model):
    first_name = models.CharField(max_length=212)
    last_name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    image = models.ImageField(upload_to='profile')
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    video = models.FileField(upload_to='about')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
