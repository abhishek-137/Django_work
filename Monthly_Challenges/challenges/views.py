
from django.shortcuts import render
from django.http import Http404 ,  HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

texts = {"january": "Winter is finally here",
        "february": "This is February", "march": "Have done Nothing in this month",
        "april": "Learning django atleat 5 days a week",
        "may": "Will do internship in this month",
        "june": "University exams in this month",
        "july": "Learn something in this month",
        "august": "Monsoon Started! ,Go for vacation for 5 days",
        "september": "Not decided for this",
        "october": "Enjoy the rain",
        "november": "This is month of diwali have to go home",
        "december": "Winter is Coming"
         
}


def index(request):
    months = list(texts.keys())

    return render(request,"challenges/index.html",{"months":months})


def monthly_challenge_by_no(request, month):
    if month > 12 or month < 1:
        raise Http404()

    else:
        months = list(texts.keys())
        redirect_month = months[month-1]
        # return monthly_challenge(request,redirect_month)   ""It want to change url then /challenges/1-12

        # this will handle if path is changed later by website to something other.
        redirect_path = reverse("path_changed", args=[redirect_month])
       # return HttpResponseRedirect("/challenges/" + months[month-1]) #hardcoded here is challneges
        return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        #return httpresponse(render_to_string()) #in place of return(render)

        challenge_text=texts[month]
        return render(request,"challenges/challenge.html",{
            "text_month":challenge_text,
            "month_name":month
        })
        
    except:
        raise Http404()
