from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })

def createlisting(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = int(request.POST.get("price"))
        image = request.POST.get("image")
        category_id = int(request.POST["category"])
        category = Category.objects.get(id=category_id)
        username = request.user.username

        add = Listing(title=title, description=description, price=price, image=image, category=category, owner=username)
        add.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/createlisting.html", {
        "category": Category.objects.all()
    })

# function accepts listing_id as an "argument"
def listing(request, listing_id):

    #create variable "listing" with data from .models Listing by calling the listing_id argument

    listing = Listing.objects.get(pk=listing_id)

    # render template that then passes that flight info into the html page

    return render(request, "auctions/listing.html", {
        "listing": listing
    })


def bid(request, listing_id):
    if request.method == "POST":
        bid = int(request.POST.get("bid"))
        bidder = request.user.username
        listing = Listing.objects.get(pk=listing_id)
        bid = Bid(bid=bid, bidder=bidder, listing=listing)
        # bid.save()
        bid.bids.add(bid)
        return render(request, "auctions/listing.html", {
            "bid": bid,
            "listing": listing
        })



# user and login stuff --------

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
