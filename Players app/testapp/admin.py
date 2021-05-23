from django.contrib import admin
from testapp.models import Player
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    '''
        Admin View for Player
    '''
    list_display = ('jersyno','name','age','iplteam')
   

admin.site.register(Player, PlayerAdmin)