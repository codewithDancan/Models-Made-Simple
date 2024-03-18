from django.db import models
import uuid
from django.template.defaultfilters import slugify 
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User

class MyModel(models.Model):
    boolean = models.BooleanField(default = True, verbose_name='This a Boolean')
    char = models.CharField(verbose_name = 'Full name: ', max_length=255, unique=True, 
                            help_text='use your original names', default='Dancan Ngaga')
    date = models.DateTimeField(auto_now_add=True)
    decimal = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    email = models.EmailField(max_length=300, default='abc@gmail.com')
    file = models.FileField(upload_to='uploads', blank=True,
                             default='C:/Users/Dancan Ngaga/Desktop/modelsmadesimple/static/img/blank_image.png')
    image = models.ImageField(upload_to='uploads', blank=True,
                             default='C:/Users/Dancan Ngaga/Desktop/modelsmadesimple/static/img/blank_image.png')
    integer = models.IntegerField(default=0)
    positive_small_int = models.PositiveIntegerField(default=1)
    slug = models.SlugField(blank=True)
    text = models.TextField(default='I love Django')
    url = models.URLField(max_length=200, default='.')
    uuid1 = models.UUIDField(default=uuid.uuid4)
    uuid2 = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    phone_number = PhoneNumberField(default='+254797921698')



    def save(self, *args, **kwargs):
        self.slug = slugify(self.text[:30])
        super(MyModel, self).save(*args, **kwargs)
