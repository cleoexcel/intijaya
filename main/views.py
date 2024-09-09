from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306244886',
        'nama': 'Cleo Excellen Iskandar',
    
    }

    return render(request, "main.html", context)


# Create your views here.
