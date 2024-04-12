from django.shortcuts import render, redirect, get_object_or_404
from Note.models import Note
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def notes(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(owner = request.user)
    else:
        notes = None
    return render(request, 'notes.html', {'mynotes' : notes})


@login_required(login_url='/login/')
def add_note_note(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('body'):
            newnotedata = Note(title = request.POST['title'], body= request.POST['body'], owner= request.user)
            newnotedata.save()
            messages.success(request, "New note created!")
            return redirect('notes')
        
        else:
            messages.error(request, "Fill in note title and content.")
            return redirect('new_note')

    return render(request, 'newnote.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('notes')
    
    if request.method == 'POST':
        uname= request.POST.get('username') 
        password =  request.POST.get('password')  
        cpassword = request.POST.get('cpassword')

        if (uname and password and cpassword) and (password == cpassword):
            if not get_user_model().objects.filter(username = uname).exists():
                get_user_model().objects.create(username=uname, password=password)
                messages.success(request, "Your account has been created sucessfully")
                return redirect('signin')
            else:
                messages.warning(request, "This account already exists. Please, login.")
                return redirect('signin')
        else:
            messages.warning(request, "Please, fill in all the fields.")
            return redirect('register')    

    return render(request, 'signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('notes')
    
    if request.method == 'POST':
        uname= request.POST.get('username') 
        password =  request.POST.get('password')  

        if (uname and password ):
            if not get_user_model().objects.filter(username = uname).exists():
                messages.error(request, "No user with this username", extra_tags="danger")
                return redirect('signin')
            else:
                auth = authenticate(request=request, username= uname, password=password)
                if auth:
                    login(request, auth)
                    messages.success(request, "Logged in.")
                    return redirect('notes')
                else:
                    messages.error(request, "Please, check your details and try again.")
                    return redirect('signin')
        else:
            messages.warning(request, "Please, fill in all the fields.")
            return redirect('signin')    
        
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/login/')
def view_note(request, username, slug):
    get_note_owner = get_object_or_404(get_user_model(), username = username)
    item_to_read = get_object_or_404(Note, owner = get_note_owner, slug = slug)
    return render(request, 'readnote.html', {'item_to_read': item_to_read})



@login_required(login_url='/login/')
def edit_note(request, username, slug):
    get_note_owner = get_object_or_404(get_user_model(), username = username)
    item_to_read = get_object_or_404(Note, owner = get_note_owner, slug = slug)

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('body'):
            item_to_read.title = request.POST['title']
            item_to_read.body = request.POST['body']
            
            item_to_read.save()
            messages.success(request, "Note updated successfully.")
            return redirect('notes') 
        else:
            messages.warning(request, "Please, make sure there is content in title and body.")
            return redirect(request.path)
    

    return render(request, 'editnote.html', {'note_to_edit': item_to_read})