from django.db import models
from django.utils.formats import date_format

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Contact Name")
    email = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s <%s> %s" % (str(self.name), str(self.email), date_format(self.timestamp, "SHORT_DATETIME_FORMAT"))

    class Meta:
        verbose_name_plural = "Feedback"
