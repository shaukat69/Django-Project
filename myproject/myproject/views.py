from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'clist':['HTML','CSS','React JS','Python'],
        'student_details':[
        {'Name':'Shaukat','Phone': 1234567891},
        {'Name':'Avez','Phone': 1234567891},
        {'Name':'Tushar','Phone': 1987654321}
        ],
        'numbers':[10,50,40,80.99,55,33,19]
    }
    return render(request,"index.html", data)


def aboutUs(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def portfolio(request):
    return render(request, "portfolio.html")

def sevices(request):
    return render(request, "services.html")

# def courseDetails(request, courseId):
#     return HttpResponse(courseId)

# def product(request, productName):
#     return HttpResponse(productName)