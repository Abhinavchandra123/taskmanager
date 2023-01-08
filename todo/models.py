from email.headerregistry import Address
from django.db import models

# Create your models here.
class Branch(models.Model):
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branchs'
    branch=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.branch

class Department(models.Model):
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    department=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.department

class Thought(models.Model):
    class Meta:
        verbose_name = 'Thought'
        verbose_name_plural = 'Thoughts'
    date=models.CharField(max_length=10,null=True,blank=True)
    day=models.CharField(max_length=10,null=True,blank=True)
    desce=models.CharField(max_length=500,null=True,blank=True)
    typ=models.CharField(max_length=100,null=True,blank=True)
    descm=models.CharField(max_length=500,null=True,blank=True)
    img=models.ImageField(height_field=None, width_field=None, max_length=100,null=False)
    def __str__(self):
        return self.desce


class Estatus(models.Model):
    class Meta:
        verbose_name = 'Estatus'
        verbose_name_plural = 'Estatuss'
    status=models.CharField(max_length=10,null=True,blank=True)
    reason=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.status
    
class Strategy(models.Model):
    class Meta:
        verbose_name ='Strategy'
        verbose_name_plural = "Strategys"
    sid=models.CharField(max_length=10,null=False,blank=False)
    stime=models.CharField(max_length=10, null=True,blank=True)
    etime=models.CharField(max_length=10, null=True,blank=True)
    sdate=models.CharField(max_length=20,null=True,blank=True)
    day=models.CharField(max_length=20, null=True,blank=False)
    fdate=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.sid

class Operation(models.Model):
    class Meta:
        verbose_name ='Operation'
        verbose_name_plural = "Operations"
    sid=models.CharField(max_length=10,null=False,blank=False)
    pid=models.CharField(max_length=10,null=False,blank=False)
    stime=models.CharField(max_length=10, null=True,blank=True)
    etime=models.CharField(max_length=10, null=True,blank=True)
    sdate=models.CharField(max_length=20,null=True,blank=True)
    day=models.CharField(max_length=20, null=True,blank=False)
    fdate=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=200, null=True,blank=True)
    thought=models.ForeignKey(Thought,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.sid

class Employee(models.Model):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    name = models.CharField(max_length=100, null=False, blank=False)
    details = models.CharField(max_length=100, null=True, blank=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True,blank=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    phone=models.CharField(max_length=100, null=True, blank=True)
    progress=models.CharField(max_length=200, null=True,blank=True)
    task=models.CharField(max_length=200, null=True,blank=True)
    tempc=models.CharField(max_length=100, null=True,blank=True)
    tempp=models.CharField(max_length=200, null=True,blank=True)
    tempt=models.CharField(max_length=200, null=True,blank=True)
    estatus=models.CharField(max_length=200, null=True,blank=True)
    status=models.ForeignKey(Estatus,on_delete=models.SET_NULL,null=True,blank=True)
    completed=models.CharField(max_length=100, null=True,blank=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    job=models.CharField(max_length=30,null=True,blank=True)
    date=models.CharField(max_length=30,null=True,blank=True)
    opsid=models.ForeignKey(Operation,on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=20,null=True,blank=True)
    tasks=models.CharField(max_length=250,null=False,blank=False)
    quantity=models.CharField(max_length=100,null=True,blank=True)
    remark=models.CharField(max_length=100,null=True,blank=True)
    empid=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    sid=models.ForeignKey(Strategy,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.job
class Strgtask(models.Model):
    class Meta:
        verbose_name = 'Strgtask'
        verbose_name_plural = 'Strgtasks'
    sid=models.ForeignKey(Strategy,on_delete=models.SET_NULL,null=True,blank=True)
    date=models.CharField(max_length=30,null=True,blank=True)
    deliv=models.CharField(max_length=30,null=True,blank=True)
    howmes=models.CharField(max_length=20,null=True,blank=True)
    wgt=models.CharField(max_length=250,null=False,blank=False)
    base=models.CharField(max_length=200,null=True,blank=True)
    goal=models.CharField(max_length=200,null=True,blank=True)
    hilo=models.CharField(max_length=200,null=True,blank=True)
    result=models.CharField(max_length=200,null=True,blank=True)
    empid=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.result



class Count(models.Model):
    class Meta:
        verbose_name = 'Count'
        verbose_name_plural = 'Counts'
    count=models.CharField(max_length=20, null=True,blank=True)
    date=models.CharField(max_length=20, null=True,blank=True)
    job=models.ForeignKey(Job,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.date