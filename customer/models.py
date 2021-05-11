from django.db import models

class Customer(models.Model):
    name                  = models.CharField(max_length=25, blank=True)
    mobile                = models.CharField(max_length=18, blank=True, null=True)
    email                 = models.EmailField(max_length=50, blank=True)
    created_at            = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'