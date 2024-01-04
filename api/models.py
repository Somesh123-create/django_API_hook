from django.db import models

# Create your models here.
class TicketIDTriggered(models.Model):
    tiket_id = models.CharField(max_length=55, blank=True, null=True, unique=True)
    tiket_comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tiket_id}"
