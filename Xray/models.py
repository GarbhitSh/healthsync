# Xray/models.py
from django.db import models
# Xray/models.py
from django.core.exceptions import ValidationError

def validate_content_file(value):
    # Your validation logic here
    pass

# Your models definition here


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
