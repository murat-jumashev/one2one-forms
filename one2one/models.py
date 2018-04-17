from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Profile(models.Model):
    email = models.EmailField(max_length=255)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile_of')

    def __str__(self):
        return 'Profile of ' + str(self.user)
