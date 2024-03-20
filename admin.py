from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
class Admin(admin.ModelAdmin):
    list_display=[
        'end_year','intensity','sector','topic','insight',
        'url','region','start_year','impact','added','published',
        'country','relevance','pestle','source','title',
        'likelihood'
    ]