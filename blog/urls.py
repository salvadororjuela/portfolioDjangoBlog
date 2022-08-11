from django.urls import path
from . import views


# Namespace urls to avoid conflict with urls named the same way in
# other app folders
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    # Path to create new articles by registered users
    path("newarticle", views.newarticle_view, name="newarticle"),
    # The slug path must be below any other paths that use slug as an argument
    # because the slug is the final parth of the url in the browser.
    path("<slug>", views.article_detail, name="article_detail"),
]
