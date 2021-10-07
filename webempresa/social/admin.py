from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Associate").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
