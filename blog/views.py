from django.shortcuts import render


def render_index(request):
    nome = 'Gabriel'

    if nome == 'Gabriel':
        return render(request, 'index.html', {'nome': nome})
