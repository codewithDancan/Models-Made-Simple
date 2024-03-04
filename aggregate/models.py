from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    posts = models.ImageField(upload_to='posts', default='C:/Users/Dancan Ngaga/Desktop/modelsmadesimple/static/img/.blank_image.png')

