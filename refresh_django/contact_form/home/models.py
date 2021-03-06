from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateField()

    def __str__(self):
        """To change the title from contact object to name of user"""

        return self.name
