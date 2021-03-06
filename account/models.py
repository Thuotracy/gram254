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

class Profile(models.Model):
  name=models.CharField(max_length=50, null=True)
  profile_picture=models.ImageField()
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
  image_name=models.CharField(max_length=50, blank=True)
  image=CloudinaryField('image')
  image_caption=models.CharField('Caption(optional)', max_length=300, blank=True)
  profile=models.ForeignKey(NUser, on_delete=models.CASCADE, blank=True, null=True)
  likes=models.IntegerField(default=0)
  created=models.DateTimeField(auto_now_add=True)
  modified=models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
      return self.image_name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def update_image(cls,id,image_name,image,image_caption,profile,likes,comments,created,modified):
    cls.objects.filter(id=id).update(image_name=image_name,image=image,image_caption=image_caption,profile=profile,likes=likes,comments=comments,created=created,modified=modified)



class Profile(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=30)
    bio = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = 'images/')
  
    def __str__(self):
        return self.username
    def save_profile(self):
        self.save()
    def delete_profile(self,username):
        to_delete= Profile.objects.filter(username=username).delete()
    def update_profile(self,old_user,new_user):
        Profile.objects.filter(username=old_user).update(name=new_user)
        self.save()
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =60)
    image_caption= models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
   
    def __str__(self):
        return self.image_name
    def save_image(self):
        self.save()
    def delete_image(self,image_reff):
        to_delete= Image.objects.filter(name=image_reff).delete()
    def total_likes(self):
        return self.likes.count()         

class Comment(models.Model):
    image= models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    comments =models.CharField(max_length=100, blank=True, default='great')
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.image.image_name, self.author)   
