from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('about/', views.about, name='about'),
    path('about/vision', views.vision, name='vision'),
    path('about/leitmotiv', views.leitmotiv, name='leitmotiv'),
    # Bien
    path('bien/', views.bien, name='bien'),
    path('bien/<int:year>/<int:month>/<int:day>/<slug:bien>/', views.bien_detail, name='bien_detail'),

    # Blog
    path('blog/', views.blog, name='blog'),
    path('', views.post_list, name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    # path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('devis/', views.devis, name='devis'),
    path('faq/', views.faq, name='faq'),
    # Services routes
    path('service/', views.service, name='service'),
    path('service/lotissement/', views.lotissement, name='lotissement'),
    path('service/amenagementfoncier/', views.amenagementfoncier, name='amenagementfoncier'),
    path('service/formation/', views.formation, name='formation'),

    path('service/location/maisons/', views.locationmaisons, name='locationmaisons'),
    path('service/location/engins/', views.engins, name='engins'),

    path('service/vente/terrains/', views.terrains, name='terrains'),
    path('service/vente/maisons/', views.ventemaisons, name='ventemaisons'),
    path('service/vente/promotionimmobiliere/', views.promotionimmobiliere, name='promotionimmobiliere'),

    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('notfound/', views.notfound, name='notfound'),
]