from django.db import models

# Create your models here.
class Pic(models.Model):
    name=models.CharField(max_length=60)
    image=models.ImageField(upload_to='image')

    # def delete(self, *args, **kwargs):
    #     storage, path = self.image.storage, self.image.path
    #     #self.image.delete()
    #     #self.name.delete()
    #     super(Pic, self).delete(*args, **kwargs)
    #     storage.delete(path)