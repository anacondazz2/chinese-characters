from django.urls import path
from . import views

urlpatterns = [
    # When processing a request Django will go down this list until it finds a matching URL pattern.
    # When we want to go to a URL we send a GET request. We can also POST to a URL in our backend code.
    # On successful find, he view function is called with an httprequest object and additional provided args.

    path("", views.index, name="index"),
    path("print_dict", views.print_dict, name="print_dict"),
    path("lookup_entry", views.lookup_entry, name="lookup_entry"),
]
