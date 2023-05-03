from django.db import models

# Create your models here.


# Creating company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100,
        choices=(
            ("IT", "IT"),
            ("Non IT", "Non IT"),
            ("Mobiles Phones", "MobilePhones"),
        ),
    )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # override and show name of company instead of object 1, 2
    def __str__(self):
        return f"{self.name}  {self.location}"


# Creating Employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    bio = models.TextField()
    role = models.CharField(
        max_length=100,
        choices=(
            ("Intern", "Intern"),
            ("Junior", "Junior"),
            ("Senior", "Senior"),
            ("Lead", "Lead"),
        ),
    )
    joined_date = models.DateTimeField(auto_now=False)
    isFullTime = models.BooleanField(default=False)
    # Showing Relations
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
