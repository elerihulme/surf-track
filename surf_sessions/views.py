from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Session
from .forms import SessionForm

# --- Class-Based Views (CBVs) ---


class SessionList(generic.ListView):
    """
    Display a paginated list of all surf sessions (public view).
    """
    queryset = Session.objects.all().order_by("-date")
    template_name = "session_list.html"
    paginate_by = 10


class MySessionList(ListView):
    """
    Display a paginated list of surf sessions for the logged-in user.
    """
    model = Session
    template_name = 'surf_sessions/my_session_list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Return only sessions belonging to the currently logged-in user.
        """
        return Session.objects.filter(user=self.request.user).order_by("-date")

# --- Function-Based Views (FBVs) ---


def log_session(request):
    """
    Allow users to log a new surf session.
    If the form is valid, the session is saved
    and associated with the logged-in user.
    Success and error messages are displayed accordingly.
    """
    # POST request - process form submission
    if request.method == 'POST':
        session_form = SessionForm(request.POST)
        # Save valid forms to the database
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.user = request.user
            session.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Surf session logged successfully!'
            )
            return HttpResponseRedirect(reverse('home'))
        
        # Return error for invalid forms
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error logging the session. Please try again.'
            )
            return render(
                request,
                "surf_sessions/log_session.html",
                {
                    "session_form": session_form,
                }
            )
    
    # If request method is GET, display an empty session form for logging
    else:
        session_form = SessionForm()

    return render(
        request,
        "surf_sessions/log_session.html",
        {
            "session_form": session_form,
        }
    )


def edit_session(request, session_id):
    """
    Allow users to edit an existing surf session.
    Only the session owner can edit.
    """
    """
    view to edit sessions
    """
    session = get_object_or_404(Session, id=session_id)
    # POST request - process form submission
    if request.method == "POST":
        session_form = SessionForm(data=request.POST, instance=session)

        # Allow valid forms to be edited
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Session Updated!'
            )
            return HttpResponseRedirect(reverse('my-sessions'))
        
        # Return error for invalid edits
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error editing the session. Please try again.'
            )
            return render(
                request,
                'surf_sessions/edit_session.html',
                {
                    'session_form': session_form,
                    'session': session
                }
            )

    # GET request - show the form pre-filled with existing data
    else:
        session_form = SessionForm(instance=session)

    return render(
        request,
        'surf_sessions/edit_session.html',
        {
            'session_form': session_form,
            'session': session
        }
    )


def delete_session(request, session_id):
    """
    Allow users to delete a surf session.
    Only the session owner can delete.
    """
    session = get_object_or_404(Session, id=session_id)

    # Ensure the session belongs to the logged-in user
    if session.user != request.user:
        messages.add_message(
            request, messages.ERROR,
            "You are not authorized to delete this session."
        )
        return HttpResponseRedirect(reverse('my-sessions'))

    # Delete the session if authorized
    session.delete()
    messages.add_message(
        request, messages.SUCCESS,
        "Session deleted successfully!"
    )
    return HttpResponseRedirect(reverse('my-sessions'))
