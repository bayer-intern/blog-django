from django.shortcuts import render
from blog.models import Publication


def render_index(request):
    return render(request, 'index.html', {})


def render_publication_done(request):
    dados = {
        'title': request.POST.get('title'),
        'preview_description': request.POST.get('preview_description'),
        'description': request.POST.get('description'),
        'external_article':  request.POST.get('external_article'),
        'image': request.POST.get('image'),
        'author':  request.POST.get('author')
    }

    publicacao = Publication(**dados)
    publicacao.save()

    return render(request, 'publication_done.html', {'dados': publicacao})
