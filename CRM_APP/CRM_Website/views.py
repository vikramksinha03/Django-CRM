from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddRecordForm
from .models import Record


# Create your views here.

def home(request):
  records = Record.objects.all()
  return render(request, 'home.html', {'records': records})

def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    #authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Logged in successfully')
      return redirect('home')
    else:
      messages.success(request, 'There was an error loggin in')
      return redirect('home')
  else:
    return render(request, 'login.html')

def logout_user(request):
  logout(request)
  messages.success(request, 'You have been successfully logged out')
  return redirect('home')


def signup_user(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      new_user = form.save(commit=False)
      new_user.set_password(form.cleaned_data['password1'])
      new_user.save()
      return render(request, 'signup.html', {'new_user':new_user})
  else:
    form = SignupForm()
    # return render(request, 'signup.html', {'form':form})
  return render(request, 'signup.html', {'form':form})


def customer_record(request, pk):
  if request.user.is_authenticated:
    record = Record.objects.get(id=pk)
    print(record)
    return render(request, 'record.html', {'record':record})
  else:
    messages.error(request, 'You must be logged in to view the record')
    return redirect('home')
  

def delete_record(request, pk):
  if request.user.is_authenticated:
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Record deleted successfully !')
    return redirect('home')
  else:
    messages.error(request, 'You must be logged in to delete the record')
    return redirect('home')
  

def add_record(request):
  form = AddRecordForm(request.POST or None)
  if request.user.is_authenticated:
    if request.method == 'POST':
      if form.is_valid():
        form.save()
        messages.success(request, 'Record got added')
        return redirect('home')
  
    return render(request, 'add_record.html', {'form':form})
    
  else:
    messages.error(request, 'You must be logged in')
    return redirect('home')

      
def update_record(request, pk):
  if request.user.is_authenticated:
    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=record)
    if form.is_valid():
      form.save()
      messages.success(request, 'Record got updated')
      return redirect('home')
    return render(request, 'update_record.html', {'form': form})
  else:
    messages.error(request, 'You must be logged in to update the record') 
    return redirect('home')             
  