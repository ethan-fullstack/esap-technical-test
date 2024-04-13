from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile


def indexView(request):

    return render(request, "welcome/index.html")


def profileView(request):
    if request.method == "POST":
        profile_data = request.POST
        profile = UserProfile.objects.create(
            full_name=profile_data["full_name"],
            country=profile_data["country"],
            description=profile_data["description"],
            github=profile_data["github"],
            linkedin=profile_data["linkedin"],
        )
        profile.save()
        return render(request, "welcome/profile.html", {"profile": profile_data})
    else:
        return HttpResponse("Invalid request method")


def profileDetailView(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    return render(request, "welcome/profile.html", {"profile": profile})

def listView(request):
    profiles = UserProfile.objects.all()
    return render(request, "welcome/list.html", {"profiles": profiles})
