from django.shortcuts import render

def show_main(request):
    context = {
        'kelas' : 'PBP C',
        'nama': 'Cleo Excellen Iskandar'
    }

    return render(request, "main.html", context)