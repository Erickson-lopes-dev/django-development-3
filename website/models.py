from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    def full_name(self):
        return f"{self.title} {self.sub_title}"

    # ordenando o full name no admin
    full_name.admin_order_field = 'title'
