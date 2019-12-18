from django.shortcuts import render
from .forms import UserRegistrationForms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from testapp.models import Post
# Create your views here.
def home(request):
    post=Post.objects.all()
    return render(request,'blog/home.html',{'p':post})

def UserRegistration(request):
    if request.method=="POST":
        form=UserRegistrationForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form=UserRegistrationForms()
        return render(request,'user/register.html',{'form':form})

@login_required
def profile(request):
    post=Post.objects.all()
    return render(request,'user/profile.html',{'p':post})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForms(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             # messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForms()
#     return render(request, 'users/register.html', {'form': form})