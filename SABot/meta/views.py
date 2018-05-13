from django.shortcuts import render

def Home(request):
    return render(request,'meta/frontend.html')

#remember that info is reference from Personalinfo class in model.py and -> line7
#in context={info(is the name that we provide but must the same):'it's  above info '} -> line 8

