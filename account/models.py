# import email
# from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from cloudinary.models import CloudinaryField


# Create your models here.

# customised model for authentication
class Manager(BaseUserManager):
  def create_user(self,name, email, password=None):
    if not name:
      raise ValueError("Name is required")
    if not email:
      raise ValueError("Email is required")

    
    user=self.model(
      name=name,
      email=self.normalize_email(email)
    )
    user.set_password(password)
    user.save(using=self._db)
    return user


  def create_superuser(self, name, email, password=None):
    user=self.create_user(
      name=name,
      email=self.normalize_email(email),
      password=password,
    )
    user.is_admin=True
    user.is_staff=True
    user.is_superuser=True
    user.save(using=self._db)
    return user
    


class NUser(AbstractBaseUser):
  # id=models.IntegerField(primary_key=True)
  name=models.CharField(verbose_name="Name", max_length=50)
  email=models.EmailField(verbose_name="email address", max_length=50,unique=True)
  date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
  last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
  is_active=models.BooleanField(default=True)
  is_admin=models.BooleanField(default=False)
  is_staff=models.BooleanField(default=False)
  is_superuser=models.BooleanField(default=False)

  USERNAME_FIELD='email'
  
  REQUIRED_FIELDS=['name']

  objects=Manager()

  def __str__(self):
    return self.name

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True



# Image and Profile models

# class Profile(models.Model):
  name=models.CharField(max_length=50, null=True)
  # profile_picture=models.ImageField()
  profile_picture=CloudinaryField('image')
  bio=models.TextField()
  created=models.DateTimeField(auto_now_add=True)
  modified=models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
      return self.name

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  @classmethod
  def update_profile(cls,id,name,profile_picture,bio,created,modified):
    cls.objects.filter(id=id).update(name=name,profile_picture=profile_picture,bio=bio,created=created,modified=modified)

  
class Image(models.Model):
  # image=models.ImageField()
  image_name=models.CharField(max_length=50, blank=True)
  image=CloudinaryField('image')
  image_caption=models.CharField('Caption(optional)', max_length=300, blank=True)
  profile=models.ForeignKey(NUser, on_delete=models.CASCADE, blank=True, null=True)
  likes=models.IntegerField(default=0)
  comments=models.TextField()
  created=models.DateTimeField(auto_now_add=True)
  modified=models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
      return self.image_name

  # def __str__(self):
  #   if not self.image_name:
  #     return ""
  #   return str(self.image_name)

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def update_image(cls,id,image_name,image,image_caption,profile,likes,comments,created,modified):
    cls.objects.filter(id=id).update(image_name=image_name,image=image,image_caption=image_caption,profile=profile,likes=likes,comments=comments,created=created,modified=modified)