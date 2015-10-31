# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from livecode.helpgit.forms import UserForm, UserProfileForm

def user_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect('https://vaibhawlabs.pythonanywhere.com/new/')
            else:
                return HttpResponse("Your account has been diasbled")
        else:
            return HttpResponse("Invalid Username/Password")
    else:
        return render(request, 'login.html')

def files(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('https://vaibhawlabs.pythonanywhere.com/files/')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        'welcome.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def new(request):
    return render(request,'new.html')

def about(request):
    return render(request,'about.html')

def search(request):
    suicide_list = ["How to commit suicide", "how to commit suicide","I want to commit suicide", "i want to commit suicide", "I don't want to live", "i don't want to live", "I don't want to live anymore","i don't want to live anymore", "I want to die", "i want to die"]
    if 'q' in request.GET:
        if request.GET['q'] in suicide_list:
            return render_to_response(
            'search.html',
            {'text':'Need help? Call! "Aasra" - 022 2754 6669'},
            context_instance=RequestContext(request)
        )
        else:
            try:
                import wikipedia
                text = wikipedia.summary(request.GET['q'], sentences=10)
                return render_to_response(
                'search.html',
                {'text': text},
                context_instance=RequestContext(request)
                )
            except:
                return redirect ('https://vaibhawlabs.pythonanywhere.com/new/')

def register(request):
    registered = False
    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect ('https://vaibhawlabs.pythonanywhere.com')
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request, 'register.html', {'user_form':user_form, 'profile_form': profile_form, 'registered': registered} )


def user_logout(request):
    logout(request)
    return render (request, 'login.html')

def robot(request):
    return render (request, 'robot.html')
