from django.contrib import admin
from main import models

admin.site.site_header = 'FieldScanner Admin'                    # default: "Django Administration"
admin.site.index_title = 'Site Administration'                 # default: "Site administration"
admin.site.site_title = 'FieldScanner Adminsitration' # default: "Django site a

admin.site.register(models.deviceData)
admin.site.register(models.MyUser)