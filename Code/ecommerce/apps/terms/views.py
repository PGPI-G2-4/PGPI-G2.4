import json


from django.shortcuts import render




def terms(request):
    return render(request, "terms/terms.html", {"email": request.session["email"]})
