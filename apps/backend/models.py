from django.db import models


#Service Class ==> Service Table
class Service(models.Model):
    service     = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.service

#Entity_Type Class ==> Entity_Type Table
class Entity_Type(models.Model):
    type = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.type

#Entity Class ==> Entity Table
class Entity(models.Model):
    entity      = models.CharField(max_length=50)
    descrition  = models.TextField(blank=True)
    service     = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='entities')
    type        = models.ForeignKey(Entity_Type, on_delete=models.CASCADE, related_name='entities')
    
    def __str__(self) -> str:
        return self.entity

#Function Class ==> Function Table
class Function(models.Model):
    function    = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.function

#Employee Class ==> Employee Table
class Employee(models.Model):
    ppr         = models.CharField(max_length=20)
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    entity      = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='employees')
    function    = models.ForeignKey(Function, on_delete=models.CASCADE, related_name='employees')
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

#Project Class ==> Project Table
class Project(models.Model):
    title           = models.CharField(max_length=150)
    description     = models.TextField(blank=False)
    
    def __str__(self) -> str:
        return self.title
    
#Phase Class ==> Phase Table
class Phase(models.Model):
    title           = models.CharField(max_length=150)
    description     = models.TextField(blank=False)
    project         = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='phases')
    
    def __str__(self) -> str:
        return self.title
    
#Task Class ==> Task Table
class Task(models.Model):
    title           = models.CharField(max_length=100)
    description     = models.TextField(blank=False)
    phase           = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self) -> str:
        return self.title
    
    
#Responsible Class ==> Responsible Table
class Responsible(models.Model):
    employee    = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reponsibles')
    task        = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reponsibles')
    start_date  = models.DateField(blank=True)
    end_date    = models.DateField(blank=True)
    observation = models.TextField(blank=True)
    
