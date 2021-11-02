from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.username
