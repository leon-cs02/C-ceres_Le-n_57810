import django
django.setup()

from django.contrib.auth.models import Group, User

# Crear grupos
admin_group, created = Group.objects.get_or_create(name='admin')
user_group, created = Group.objects.get_or_create(name='user')

# Asignar usuarios a grupos
user = User.objects.get(username='leon')  
user.groups.add(admin_group)
