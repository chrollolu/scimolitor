import os
from django.conf import settings

BASE_DIIR = settings.BASE_DIR

employe_image_1 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/employe/1.jpg')
employe_image_2 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/employe/2.jpg')
employe_image_3 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/employe/3.jpg')
employe_image_4 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/employe/4.jpg')
employe_image_5 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/employe/5.jpg')
employe_image_6 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/employe/6.jpg')

bien_image_1 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/bien/1.jpg')
bien_image_2 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/bien/2.jpg')
bien_image_3 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/bien/3.jpg')
bien_image_4 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/bien/4.jpg')
bien_image_5 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/bien/5.jpg')
bien_image_6 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/bien/6.jpg')

post_image_1 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/post/1.jpg')
post_image_2 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/post/2.jpg')
post_image_3 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/post/3.jpg')
post_image_4 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/post/4.jpg')
post_image_5 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/post/5.jpg')

client_image_1 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/client/1.jpg')
client_image_2 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/client/2.jpg')
client_image_3 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/client/3.jpg')
client_image_4 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/client/4.jpg')
client_image_5 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/client/5.jpg')


gallery_image_1 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/1.jpg')
gallery_image_2 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/2.jpg')
gallery_image_3 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/3.jpg')
gallery_image_4 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/4.jpg')
gallery_image_5 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/5.jpg')
gallery_image_6 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/6.jpg')
gallery_image_7 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/7.jpg')
gallery_image_8 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/8.jpg')
gallery_image_9 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/9.jpg')
gallery_image_10 = os.path.join(settings.BASE_DIR, 'web/management/commands/images/gallery/10.jpg')

# The root user
super_user = {
    'username': 'admin',
    'email': 'admin@gmail.com',
    'password': 'admin'
}

default_users = [
    {'username': 'accueil', 'password': '1234'}, 
]

bien = [
    {'titre': 'bien 1', 'location': 'Abidjan', 'body': 'this is the bien 1', 'image': bien_image_1},
    {'titre': 'bien 2', 'location': 'San Pédro', 'body': 'this is the bien 2', 'image': bien_image_2},
    {'titre': 'bien 3', 'location': 'Aboisso', 'body': 'this is the bien 3', 'image': bien_image_3},
    {'titre': 'bien 4', 'location': 'Grand-Bassam', 'body': 'this is the bien 4', 'image': bien_image_4},
    {'titre': 'bien 5', 'location': 'Yamoussoukro', 'body': 'this is the bien 5', 'image': bien_image_5},
]

employe = [
    {'titre': 'Mr.', 'nom': 'Annicet Eby Amoa', 'fonction': 'Directeur des Opérations', 'mobile': '+(225) 05 05 05 05 05', 'email': 'annicet@gmail.com', 'image': employe_image_1},
    {'titre': 'Mme.', 'nom': 'Amon', 'fonction': 'Comptabilité', 'mobile': '+(225) 05 05 05 05 05', 'email': 'annicet@gmail.com', 'image': employe_image_2},
    {'titre': 'Miss.', 'nom': 'Marina Amani', 'fonction': 'Chargéé de Clientèle', 'mobile': '+(225) 05 05 05 05 05', 'email': 'annicet@gmail.com', 'image': employe_image_4},
    {'titre': 'Mme.', 'nom': 'Rita Bleu', 'fonction': 'Chargéé de Clientèle', 'mobile': '+(225) 05 05 05 05 05', 'email': 'annicet@gmail.com', 'image': employe_image_3},
    {'titre': 'Mr.', 'nom': 'You Zan Bi', 'fonction': 'Responsable Technique', 'mobile': '+(225) 05 05 05 05 05', 'email': 'annicet@gmail.com', 'image': employe_image_5},
]


post = [
    {'title': 'post 1', 'body': 'This is the post 1', 'image': post_image_1},
    {'title': 'post 2', 'body': 'This is the post 2', 'image': post_image_2},
    {'title': 'post 3', 'body': 'This is the post 3', 'image': post_image_3},
    {'title': 'post 4', 'body': 'This is the post 4', 'image': post_image_4},
    {'title': 'post 5', 'body': 'This is the post 5', 'image': post_image_5},
]

gallery = [
    {'titre': 'gallery 1', 'image': gallery_image_1},
    {'titre': 'gallery 2', 'image': gallery_image_2},
    {'titre': 'gallery 3', 'image': gallery_image_3},
    {'titre': 'gallery 4', 'image': gallery_image_4},
    {'titre': 'gallery 5', 'image': gallery_image_5},
    {'titre': 'gallery 6', 'image': gallery_image_6},
    {'titre': 'gallery 7', 'image': gallery_image_7},
    {'titre': 'gallery 8', 'image': gallery_image_8},
    {'titre': 'gallery 9', 'image': gallery_image_9},
    {'titre': 'gallery 10', 'image': gallery_image_10},
]


client = [
    {'nom': 'client 1', 'image': client_image_1},
    {'nom': 'client 2', 'image': client_image_2},
    {'nom': 'client 3', 'image': client_image_3},
    {'nom': 'client 4', 'image': client_image_4},
    {'nom': 'client 5', 'image': client_image_5},
]