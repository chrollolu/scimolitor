from django.shortcuts import render
from .models import Post, Bien
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    posts = Post.published.all()
    biens = Bien.objects.all()
    return render(request, 'web/pages/index/index.html', { 'posts': posts, 'biens': biens })

def about(request):
    return render(request, 'web/pages/about/index.html')

def vision(request):
    return render(request, 'web/pages/about/vision.html')

def leitmotiv(request):
    return render(request, 'web/pages/about/leitmotiv.html')

# 
def bien(request):
    biens = Bien.objects.all()
    return render(request, 'web/pages/bien/index.html', {'biens': biens})

def bien_detail(request, year, month, day, bien):
    bien = get_object_or_404(Bien, slug=bien, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'web/pages/bien/detail.html', {'bien': bien})
#
def blog(request):
    posts = Post.published.all()
    return render(request, 'web/pages/blog/index.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'web/pages/blog/detail.html', {'post': post})

def post_list(request):
    posts = Post.published.all()
    return render(request, 'web/sections/_news.html', {'posts': posts})

def career(request):
    return render(request, 'web/pages/career/index.html')

def contact(request):
    return render(request, 'web/pages/contact/index.html')

def devis(request):
    return render(request, 'web/pages/devis/index.html')

def faq(request):
    return render(request, 'web/pages/faq/index.html')

#   Services views

def service(request):
    return render(request, 'web/pages/service/index.html')
    
def lotissement(request):
    return render(request, 'web/pages/service/lotissement.html')

def amenagementfoncier(request):
    return render(request, 'web/pages/service/amenagementfoncier.html')

def formation(request):
    return render(request, 'web/pages/service/formation.html')

def locationmaisons(request):
    return render(request, 'web/pages/service/locationmaisons.html')

def engins(request):
    return render(request, 'web/pages/service/engins.html')

def terrains(request):
    return render(request, 'web/pages/service/terrains.html')

def ventemaisons(request):
    return render(request, 'web/pages/service/ventemaisons.html')

def promotionimmobiliere(request):
    return render(request, 'web/pages/service/promotionimmobiliere.html')


#

def gallery(request):
    return render(request, 'web/pages/gallery/index.html')

def team(request):
    return render(request, 'web/pages/team/index.html')

def notfound(request):
    return render(request, 'web/pages/notfound/index.html')