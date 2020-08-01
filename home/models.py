from django.db import models

# Create your models here.
class Room(models.Model):
    Name = models.CharField(max_length=50, unique=True, null=False)
    Image = models.ImageField(upload_to='pics', max_length=100)
    Description = models.TextField()
    Fees = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.id) + " - " + self.Name


class Bed(models.Model):
    RID = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Department(models.Model):
    Name = models.CharField(max_length=50, unique=True, null=False)
    Description = models.TextField()

    def __str__(self):
        return str(self.id)


class Doctor(models.Model):
    Sex_Choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    Username = models.CharField(max_length=10, null=True)
    Password = models.CharField(max_length=10, null=True)
    Name = models.CharField(max_length=50, null=False)
    Image = models.ImageField(upload_to='pics', max_length=100)
    DOB = models.DateField(null=True)
    Sex = models.CharField(max_length=6, null=True, choices=Sex_Choices)
    DID = models.ForeignKey(Department, on_delete=models.CASCADE)
    Address = models.TextField()
    Contact = models.PositiveIntegerField(null=False)
    Email = models.EmailField()
    Fees = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return str(self.id) + " - " + self.Name + " - " + self.DID.Name


class Laboratory(models.Model):
    Name = models.CharField(max_length=50, unique=True, null=False)
    Description = models.TextField()
    Fees = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return str(self.id) + " - " + self.Name


class Patient(models.Model):
    Sex_Choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    Username = models.CharField(max_length=10, null=True)
    Password = models.CharField(max_length=10, null=True)
    Name = models.CharField(max_length=30, null=False)
    Image = models.ImageField(upload_to='pics', max_length=100)
    DOB = models.DateField(null=True)
    Age = models.PositiveIntegerField(null=False)
    Sex = models.CharField(max_length=6, null=False, choices=Sex_Choices)
    Address = models.TextField()
    Contact = models.PositiveIntegerField(null=False)
    Email = models.EmailField()
    DOJ = models.DateField(null=False)
    BID = models.ForeignKey(Bed, on_delete=models.CASCADE)
    DID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + " - " + self.Name + " - " + self.DID.Name


class Report(models.Model):
    PID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    LID = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    Date = models.DateField()

    def __str__(self):
        return str(self.id) + " - " + self.PID.Name + " - " + str(self.Date)


class Admin(models.Model):
    Sex_Choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    Username = models.CharField(max_length=10, null=False)
    Password = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=30, null=False)
    Image = models.ImageField(upload_to='pics', max_length=100)
    DOB = models.DateField(null=False)
    Sex = models.CharField(max_length=6, null=False, choices=Sex_Choices)
    Address = models.TextField()
    Contact = models.PositiveIntegerField(null=False)
    Email = models.EmailField()

    def __str__(self):
        return str(self.id) + " - " + self.Name