from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Expens(models.Model):
    title = models.CharField(max_length=64, verbose_name="Motif")
    amount = models.IntegerField(verbose_name="Montant")
    ddate = models.DateField(
        default=date.today, verbose_name="Date")
    person = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, 
        verbose_name="Responsable de la dépense",
        related_name="expens")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.TextField(
        max_length=512, blank=True, verbose_name="Commentaires")

    def __str__(self):
        return f"Dépense de {self.amount}€ par {self.person} ({self.title}) [{self.ddate}]"

    def get_absolute_url(self):
        return reverse('finances:expens_detail', args=(self.pk,))

    class Meta:
        ordering = ["amount"]
        verbose_name_plural = "Expenses"


class Salary(models.Model):
    amount = models.IntegerField(verbose_name="Salaire")
    ddate = models.DateField(
        default=date.today, verbose_name="Date")
    person = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, 
        verbose_name="Personne qui a eu ce salaire",
        related_name="salary")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.TextField(
        max_length=512, blank=True, verbose_name="Commentaires")
    
    def __str__(self):
        return f"Salaire de {self.person.first_name} au  {self.ddate}: {self.amount}€"
    
    def get_absolute_url(self):
        return reverse('finances:salary_detail', args=(self.pk,))

    class Meta:
        ordering = ["amount"]
        verbose_name_plural = "Salaries"