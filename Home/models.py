from django.db import models

# Create your models here.
class Person(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,)
    mobile=models.CharField(max_length=10)
    age=models.CharField(max_length=10)
    height=models.CharField(max_length=10)
    weight=models.CharField(max_length=10)
    address=models.TextField(default=" ")
    desc=models.TextField(default=" ")
    gender = models.CharField(max_length=10, default='male')
    photos=models.ImageField(upload_to="Images")
    contact_person=models.CharField(max_length=100)
    contact_person_number=models.CharField(max_length=10)
    last_seen_loc=models.CharField(max_length=200)
    missing_date=models.DateField()
    status=models.CharField(max_length=10,default="Active")
    f_status=models.CharField(max_length=10,default="Not Found")


    def __str__(self):
        return self.name


class Mails(models.Model):
    sna=models.AutoField(primary_key=True)
    Locations=models.CharField(max_length=500,default=" ")
    mails=models.CharField(max_length=500,null=False)
    def __str__(self):
        return self.mails