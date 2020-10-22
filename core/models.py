from django.db import models

# Create your models here.
class Pictures(models.Model):
  pictureUrl = models.CharField(max_length=250)
  returnData = models.TextField()
  queryDate = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return str(self.id)

  class Meta:
    db_table: 'Pictures'