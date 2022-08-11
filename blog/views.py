from django.contrib.auth import forms
from django.shortcuts import render
from .models import Articles
# Required to access to websites where log in is required
from django.contrib.auth.decorators import login_required
# Import the file where the forms are created
from . import forms


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "Articles": Articles.objects.all().order_by("date")
    })


def article_detail(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request, "blog/articleContent.html", {
        'article': article
    })


# log in decorator provides the path to send the user that is not logged
# in to the log in page
@login_required(login_url="/users/login/")
def newarticle_view(request):
    # If user reaches via POST
    if request.method == "POST":
        # Creates the form and get the information posted by the user.
        # As the form submits media files, the reques.FILES argument is
        # required to be passed in.
        form = forms.NewArticle(request.POST, request.FILES)
        # If form is valid, save the article
        if form.is_valid():
            # To save create a variable and store de data, but not commit
            # momentarily
            articleToCreate = form.save(commit=False)
            # Now the actual user (request.User) is assigned as the author
            articleToCreate.author = request.user
            # Save the Article
            articleToCreate.save()
            # Return the arguments and display the list of articles
            return render(request, "blog/index.html", {
                "Articles": Articles.objects.all().order_by("date"),
                "message": "Article Succesfully Posted!",
            })

    # If user reaches via get
    else:
        # Create a new instance of the form for the new article
        form = forms.NewArticle()
        # Render the form variable to newarticle.html
    return render(request, "blog/newarticle.html", {
        "form": form
    })
