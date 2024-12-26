from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User
from .models import Session
from .forms import SessionForm

# Create your views here.
class SessionList(generic.ListView):
    queryset = Session.objects.all()
    template_name = "session_list.html"
    paginate_by = 10

def user_session_list(request):
    sessions = Session.objects.filter(user=request.user)
    return render(
        request,
        'surf_sessions/user_session_list.html',
        {'sessions': sessions}
    )


def log_session(request):
    if request.method == 'POST':
        session_form = SessionForm(request.POST)
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('home') 
    
    session_form = SessionForm()

    return render(
        request, 
        "surf_sessions/log_session.html",
        {
            "session_form": session_form,
        }
    )