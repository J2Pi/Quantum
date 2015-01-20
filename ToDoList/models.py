from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskList(models.Model):
	user = models.ForeignKey(User)
	tasks = models.OneToManyField('Task')

class Task(models.Model):
	task_title = models.CharField(max_length=200)
	checkbox = models.BooleanField(default = False)

class TaskInfo(models.Model):
	task_desc = models.CharField(max_length=200)
	create_date = models.DateTimeField('date created')
	due_date = models.DateTimeField('date due')

class CollaboratorList(model.Model):
	collaborator = models.OneToManyField(User)