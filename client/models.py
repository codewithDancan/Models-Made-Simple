from django.db import models
from team.models import Team
from django.contrib.auth.models import User

class InfoTable(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # proxy = True



class Comment(InfoTable):
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    

class Client(InfoTable):

    CHOICES = (
        ('active', 'Active'),
        ('archived', 'Archived')
    )
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    status = models.CharField(default = 'Archived', max_length=255, choices=CHOICES)


    # altering default ordering 
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



    # default functions 
    def __str__(self):
        return self.name


    # custom models 
    def number_of_comments(self):
        return self.comments.count()
    

    # overridng default save method 
    def save(self, *args, **kwargs):
        print('Saved')
        super(Client, self).save(*args, **kwargs)


class TodoList(InfoTable):
    client = models.OneToOneField(Client, related_name='todolists', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    # created_at = models.DateTimeField(auto_now_add= True)
    # changed_at = models.DateTimeField(auto_now=True)



    
