from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import m2m_changed


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10 , decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"{self.name} ${self.price}"

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10 , decimal_places=2)
    bio = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='media_sub' , null=True , blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.pk})

class Sale(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
    discount = models.DecimalField(max_digits=10 , decimal_places=2)
    total = models.DecimalField(max_digits=10 , decimal_places=2, null=True, blank=True)

    def get_total(self):
        tot = 0
        for product in self.products.all():
            tot += product.price
        return tot - self.discount

@receiver(m2m_changed, sender=Sale.products.through)
def update_sale_total(sender, instance, **kwargs):
    instance.total = instance.get_total()
    instance.save()





