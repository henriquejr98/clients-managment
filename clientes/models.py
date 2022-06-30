from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10 , decimal_places=2)
    bio = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='media_sub' , null=True , blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'