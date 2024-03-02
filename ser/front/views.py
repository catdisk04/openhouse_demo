from django.shortcuts import render, HttpResponse
from .forms import Inp_form

def home(request):
    if request.method == "POST":
        form = Inp_form(request.POST)
        if form.is_valid():
            input = form.cleaned_data
            print(input["name"], input["hash"])
            return render(request, "test1.html", {"form":form})
        


        else:
            print("NOT VALID")


    else:
        form = Inp_form()
        return render(request, "test1.html", {"form":form})

# Create your views here.
