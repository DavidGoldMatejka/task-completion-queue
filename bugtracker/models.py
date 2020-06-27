from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class MyProjects(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bugtracker')


class Post(models.Model):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    STATUS_CHOICES = [
        (LOW , 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    ]

    TYPE_CHOICES = [
        ('Features', 'Feature Request'),
        ('Bug/Error', 'Bug/Error'),
        ('Design', 'Design'),
    ]

    PROGRESS_STATUS = [
        ('Open', 'Open'),
        ('InProgress', 'In Progress'),
        ('AddInfo', 'Additional Info Required'),
        ('Completed', 'Completed'),
    ]



    #all_users = Profile.objects.all()
    #all_user_choices = ((x.user, x.user) for x in all_users)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    priority = models.IntegerField( choices=STATUS_CHOICES, default=1)
    status = models.CharField(choices=PROGRESS_STATUS, default='Open', max_length=25)
    ticket_type = models.CharField(choices=TYPE_CHOICES, default ='Features', max_length=25)
    project = models.ForeignKey(MyProjects, on_delete=models.CASCADE, default=1)
    assigned_developer = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, related_name="+", default=1)
    #assigned_developer = models.CharField(choices=all_user_choices, default=author, max_length=50)
    #status = models.Choices(choices=PROGRESS)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bugtracker')