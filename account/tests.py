# from django.test import TestCase
from .models import Profile, Image


# Create your tests here.
class ProfileTests(TestCase):
  def setUp(self):
    self.one=Profile(name='one', bio='bio')

  def test_instance(self):
    self.assertTrue(isinstance(self.one,Profile))

  def test_save_method(self):
    self.one.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)

  def test_delete_method(self):
    profs = Profile.objects.filter(name='name')
    profs.delete()
    self.assertTrue(len(Profile.objects.all()) == 0)

  def test_update_method(self):
    update = 'two'
    num='num'
    pic='pic'
    create= '2022-03-11 06:30'
    modi='2022-03-11 06:30'
    self.one.update_profile(self.one.id,update,num,pic,create,modi)
    update = Profile.objects.filter(bio='two')
    self.assertFalse(len(update) == 1)


class ImageTests(TestCase):
  def setUp(self):
    self.one=Image(image_name='image_name', image_caption='image_caption', likes=2, comments='comments')
    self.one.save_image()

  def test_save_method(self):
    self.one.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images) > 0)


  def test_delete_method(self):
    images = Image.objects.filter(image_name='name')
    images.delete()
    self.assertFalse(len(Image.objects.all()) == 0)

  def test_update_method(self):
    update = 'two'
    updat = 'image', 
    upda = 'image_caption', 
    upd = 1
    up = 3
    u = 'comments', 
    pud = '2022-03-11 06:30', 
    date = '2022-03-11 06:30'

    self.one.update_image(self.one.id,update,updat,upda,upd,up,u,pud,date)
    update = Image.objects.filter(one='two')
    self.assertTrue(len(update) == 1)
