from cv2 import blur
from django.db import models

# Create your models here.

class img(models.Model):
    img_cus = models.ImageField(upload_to="User_Search/", null=True)
