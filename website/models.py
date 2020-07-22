from django.db import models


class Categorias(models.TextChoices):
    TECH = 'tc', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    cetegories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def full_name(self):
        return f"{self.title} {self.sub_title}"

    def get_category_label(self):
        return self.get_cetegories_display()

    # ordenando o full name no admin
    full_name.admin_order_field = 'title'
