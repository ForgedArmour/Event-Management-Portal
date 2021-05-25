from django.db import models

# Create your models here.
class makeEvent(models.Model):
    event_no = models.AutoField
    event_name = models.CharField(max_length=50,default="")
    event_date = models.DateField()
    event_desc = models.CharField(max_length=300,default="")
    event_contact = models.CharField(max_length=13,default="")
    event_poster = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return self.event_name


class myEvent(models.Model):
    myeve_no = models.AutoField
    myeve_name = models.CharField(max_length=50)
    myeve_username = models.CharField(max_length=50)
    myeve_email = models.CharField(max_length=50)
    myeve_desc = models.CharField(max_length=300)
    myeve_contact = models.CharField(max_length=13)

    def __str__(self):
        return self.myeve_name