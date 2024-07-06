from django.db import models

# Create your models here.


class Category:
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


class Author:
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    b_date = models.DateField()
    tel = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name}"


class News:
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField()
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField()
    location = models.CharField()
    views = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
