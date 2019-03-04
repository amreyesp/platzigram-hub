"""User admin classes"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Models
from users.models import Profile


@admin.register(Profile) #esto es equivalente a admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin."""
     #Toda esta clase hace referencia a comandos para visualizar estas
     #variables en la web
    list_display = ('pk','id','user_id','user','phone_number','website','picture','posts_count','get_following')
    list_display_links = ('user','pk')
    list_editable = ('website','phone_number','posts_count')

    search_fields = (
    'user__email',
    'user__last_name',
    'phone_number'#este no inicia con user_ porque no es un atributo heredado
    #del User ModelAdmin sino de la info que añadimos en el proxy model,
    #es decir, de nuestro propio modelo de usuario
    )

    list_filter = ('user__is_active','created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (('user','picture'),),
        }),
        ('More information', {
            'fields': (('website','phone_number'),
            ('biography')),
        }),
        ('Metadata',
        {
            'fields':(('created','modified'),),
        })
    )

    readonly_fields = ('created','modified')

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
