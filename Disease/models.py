from django.db import models

class DiseasePrecaution(models.Model):
    disease = models.CharField(max_length=100)
    symptom_precaution_0 = models.CharField(max_length=100, blank=True, null=True)
    symptom_precaution_1 = models.CharField(max_length=100, blank=True, null=True)
    symptom_precaution_2 = models.CharField(max_length=100, blank=True, null=True)
    symptom_precaution_3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.disease
class RecMed(models.Model):
    disease = models.CharField(max_length=100)
    drug_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.disease} - {self.drug_name}"
