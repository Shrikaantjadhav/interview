from django.shortcuts import render, redirect
# from .forms import UploadFileForm  # Adjust this line according to your actual form class name
from .form import UploadFileForm ,RegisterForm ,LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')




def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")