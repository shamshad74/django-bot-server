from django.db import models
from django.contrib.auth.models import User

class NumberofCalls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def calls(self):
        qs=self.call.all().count()
        return qs