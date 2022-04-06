from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from account.forms import UserRegistrationForm, UserLoginForm,CommentForm,ProfileForm
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


def register(request):
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

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            new_comment=form.save(commit=False)
            # new_post.profile=current_user
            new_comment.save()
            print('comment saved')
            return redirect(home_view)
    else:
        form = CommentForm()
        return render(request, 'comment.html',{'form':form}) 

def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile= Profile.objects.filter(username=current_user)
            print(profile)
            if profile:
                print('profile exist')
                username = current_user
                useremail=form.cleaned_data['useremail']
                profile_image=form.cleaned_data['profile_image']
                Profile.objects.filter(username=current_user).update(useremail=useremail,profile_image=profile_image)
            else:
                print('profile does not exist')
                profile=form.save(commit=False)
                profile.username= current_user
                profile.save()
            message='saved successfuly'
            # profile_display(request)
            return redirect(profile_display)
    else:
        form = ProfileForm()
    return render(request, 'profiledisplay.html',{'form':form})        