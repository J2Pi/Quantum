from django.db import models

# Create your models here.
class Task(models.Model):
	task_title = models.CharField(max_length=200)
	checkbox = models.BooleanField(default = False)

class TaskInfo(models.Model):
	task_desc = models.CharField(max_length=200)
	create_date = models.DateTimeField('date created')
	due_date = models.DateTimeField('date due')
	#collaborator = User(constructor fields)