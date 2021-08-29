from django.db import models
from django.utils.html import escape
from PIL import Image
from django.core.files import File
from resizeimage import resizeimage
import os
from io import BytesIO
from datetime import datetime
# from django.conf import settings
from django.contrib.auth.models import User

    
class Categories(models.Model):
    date=models.DateField()
    image=models.ImageField(max_length=120, blank=True, null=True)
    is_image_compressed = models.BooleanField(default=False)
    category_name=models.CharField(max_length=120, blank=True, null=True)
    number_of_votes=models.IntegerField(blank=True, default=0)
    def save(self, *args, **kwargs):
        if self.is_image_compressed == False:
            new_image = self.compress(self.image)
            self.image = new_image
            self.is_image_compressed = True
        super().save(*args, **kwargs)

    # image compression method
    def compress(self, filename):
        im = Image.open(filename)

        im = im.convert('RGB')

        # get filename extension
        name, ext = os.path.splitext(filename.name)

        ''' new filename '''
        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        new_name = name + str(timestamp)
        new_name = new_name.replace('.', '')

        new_filename = new_name+ext

        max_width = 720
        if im.size[0] > max_width:
            im = resizeimage.resize_width(im, max_width)
        im_io = BytesIO()

        im.save(im_io, 'JPEG', quality=90)
        new_image = File(im_io, name=new_filename)
        return new_image


    def __str__(self):
        return self.category_name

    # def CategoryNominee(self):
    #     return self.nomiees_set.all()

    class Meta:
        verbose_name_plural = "Categories"



# Create your models here.
class Nominees(models.Model):
    date=models.DateField()
    image=models.ImageField(max_length=120, blank=True, null=True)
    is_image_compressed = models.BooleanField(default=False)
    fullname=models.CharField(max_length=120, blank=True, null=True)
    name=models.CharField(max_length=120, blank=True, null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE, blank=False, null=True)
    number_of_votes=models.IntegerField(default=0)

    # calling image compression function before saving the data
    def save(self, *args, **kwargs):
        if self.is_image_compressed == False:
            new_image = self.compress(self.image)
            self.image = new_image
            self.is_image_compressed = True
        super().save(*args, **kwargs)

    # image compression method
    def compress(self, filename):
        im = Image.open(filename)

        im = im.convert('RGB')

        # get filename extension
        name, ext = os.path.splitext(filename.name)

        ''' new filename '''
        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        new_name = name + str(timestamp)
        new_name = new_name.replace('.', '')

        new_filename = new_name+ext

        max_width = 720
        if im.size[0] > max_width:
            im = resizeimage.resize_width(im, max_width)
        im_io = BytesIO()

        im.save(im_io, 'JPEG', quality=90)
        new_image = File(im_io, name=new_filename)
        return new_image

    class Meta:
        verbose_name_plural = "Nominees"

    
class VoteResults(models.Model):
    date=models.DateField()
    image=models.ImageField(max_length=120, blank=True, null=True)
    is_image_compressed = models.BooleanField(default=False)
    name=models.CharField(max_length=120, blank=True, null=True)
    category=models.CharField(max_length=120, blank=True, null=True)
    number_of_votes=models.IntegerField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.is_image_compressed == False:
            new_image = self.compress(self.image)
            self.image = new_image
            self.is_image_compressed = True
        super().save(*args, **kwargs)

    # image compression method
    def compress(self, filename):
        im = Image.open(filename)

        im = im.convert('RGB')

        # get filename extension
        name, ext = os.path.splitext(filename.name)

        ''' new filename '''
        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        new_name = name + str(timestamp)
        new_name = new_name.replace('.', '')

        new_filename = new_name+ext

        max_width = 720
        if im.size[0] > max_width:
            im = resizeimage.resize_width(im, max_width)
        im_io = BytesIO()

        im.save(im_io, 'JPEG', quality=90)
        new_image = File(im_io, name=new_filename)
        return new_image

    class Meta:
        verbose_name_plural = "Votting Results"
  
    

  
    