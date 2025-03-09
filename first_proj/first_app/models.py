from django.db import models


# Create your models here.
class EmpDetails(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_city = models.CharField(max_length=25)
    emp_company = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.emp_name} {self.emp_city} {self.emp_company}"
