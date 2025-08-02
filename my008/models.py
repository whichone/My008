from django.db import models
from django.utils import timezone
from datetime import timedelta

class SafetyCultureRecord(models.Model):
    model = models.CharField(max_length=100)
    unit_serial_number = models.CharField(max_length=100, unique=True)
    ums_sn = models.CharField(max_length=100, blank=True, null=True)
    audit_date = models.DateField()
    warranty_expiry = models.DateField()
    tm_device_id = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-calc warranty expiry if serial starts with "IG"
        if self.unit_serial_number.startswith('IG'):
            self.warranty_expiry = self.audit_date + timedelta(days=365*3)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.unit_serial_number} - {self.model}"