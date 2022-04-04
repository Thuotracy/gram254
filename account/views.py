from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from account.forms import UserRegistrationForm, UserLoginForm
from .models import Profile,Image
from django.views.generic.edit import CreateView

# Create your views here.

def landing(request):
  image=Profile.objects.all()
  context={'image':image}
  return render(request, 'account/landing.html', context)


def home_view(request):
  pics=Image.objects.all()
  context={'pics':pics}
  return render(request, 'account/dashboard.html', context)


# def register(request):
  context={}
  if request.POST:
    form=UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    context['register_form']=form

  
  else:
    form=UserRegistrationForm()
    context['register_form']=form
  return render(request, 'account/register.html',context)


def login_view(request):
  context={}
  if request.POST:
    form=UserLoginForm(request.POST)
    if form.is_valid():
      email=request.POST['email']
      password=request.POST['password']
      user=authenticate(request, email=email, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')

    else:
      context['login_form']=form


  else:
    form=UserLoginForm()
    context['login_form']=form
  return render(request,'account/login.html', context)



def logout_view(request):
  logout(request)
  return redirect('login')



def search_results(request):
  if 'image' in request.GET and request.GET["image"]:
    search_term = request.GET.get("image")
    searched_images = Image.objects.filter(image_name__icontains = search_term) 
    message = f"{search_term}"

    return render(request, 'account/search.html', {"message":message,"images":searched_images})

  else:
    message = "No images with that tag"
    return render(request, 'account/search.html',{"message":message})


class Post(CreateView):
  model=Image
  fields=['image_name','image','image_caption','likes','comments']
  success_url='account/dashboard.html'