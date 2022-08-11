from django.shortcuts import render
# Creates forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Required to display the articles after logging out (logout_view)
from blog.models import Articles
# Import forms to retreive NewArticle() inside login_view when user is not
# logged in when trying to access to create a new article
from blog import forms


# Function to sign up
def signup_view(request):
    # If user reaches via post
    if request.method == "POST":
        # The form obtains the user information
        form = UserCreationForm(request.POST)
        # Validation
        if form.is_valid():
            # Saves the user's information into the database
            user = form.save()
            # Log the user in
            login(request, user)
            # After logging in the user is redirected to the list of articles
            # When redirecting to a html file in another app folderl use ":"
            # ("blog:index")
            # return redirect("blog:index")
            return render(request, "blog/index.html", {
                # Imported from blog.models
                "Articles": Articles.objects.all().order_by("date"),
                "message": "User Succesfuly Created",
            })

        # If form data is not valid, it is returned to the sign up form to
        # correct it
        else:
            return render(request, "users/signup.html", {
                "form": form,
                "message": "Upss. Something Went Wrong!",
            })
    # If user reaches via get
    else:
        # Creates the form
        form = UserCreationForm()
        return render(request, "users/signup.html", {
            "form": form
        })


# Function to log in
def login_view(request):
    # if user reaches via post
    if request.method == "POST":
        # Creates the authentication form. It requires to name the parameter
        # (data=request.POST)
        form = AuthenticationForm(data=request.POST)
        # Validation
        if form.is_valid():
            # Log in the user
            # Gets the data of the user from the form variable
            user = form.get_user()
            # Logs in using the user variable as a parameter
            login(request, user)
            # In case the user is trying to post a blog article but is
            # not logged in, he is redirected to the log in website
            if "next" in request.POST:
                # Both options work for return, but the second one allows
                # returning a message
                # return redirect(request.POST.get("next"))
                # Allows returning a message as a parameter
                form = forms.NewArticle()
                return render(request, "blog/newarticle.html", {
                    "message": "Succesfully Logged In!",
                    "form": form,
                })
            else:
                return render(request, "blog/index.html", {
                    # Imported from blog.models
                    "Articles": Articles.objects.all().order_by("date"),
                    "message": "You are Logged In!",
                })
        # If form data is not valid, it is returned to the log in form to
        # correct it
        else:
            return render(request, "users/login.html", {
                "form": form,
                "message": "Upss. Something Went Wrong!",
            })

    # If user reaches via get
    else:
        # Creates and displays the form
        form = AuthenticationForm()
        return render(request, "users/login.html", {
            "form": form,
        })


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, "blog/index.html", {
            # Imported from blog.models
            "Articles": Articles.objects.all().order_by("date"),
            "message": "Succesfully Logged Out!",
        })
