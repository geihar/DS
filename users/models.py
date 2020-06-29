from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='1.jpg', upload_to='user_images')

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    def save(self):
        super().save()

        img = Image.open(self.img.path)

        if img.height > 128 or img.width > 128:
            resize = (128, 128)
            img.thumbnail(resize)
            img.save(self.img.path)

