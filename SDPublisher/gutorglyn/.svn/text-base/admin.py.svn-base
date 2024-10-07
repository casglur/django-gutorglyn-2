from django.contrib import admin
from SDPublisher.gutorglyn.models import manuscripts, manuscriptSort, personalNames, placeNames, poemSort

# admin.site.register(personalNames)
# admin.site.register(placeNames)

class manuscriptsAdmin(admin.ModelAdmin):
    list_display = ('manuscript_ref', 'poem_number', 'hand_cy')
    list_filter = ('poem_number', 'hand_cy')
    ordering = ['manuscript_ref']
    search_fields = ['manuscript_ref']

admin.site.register(manuscripts, manuscriptsAdmin) 

class manuscriptSortAdmin(admin.ModelAdmin):
    list_display = ('manuscript_name', 'sort_order')
    ordering = ['sort_order']
    
admin.site.register(manuscriptSort, manuscriptSortAdmin) 

class personalNamesAdmin(admin.ModelAdmin):
    list_display = ('name_in_text', 'line_ref')
    list_filter = ('name_type',)
    ordering = ['name_in_text']
    search_fields = ['name_in_text']       
    
admin.site.register(personalNames, personalNamesAdmin) 

class placeNamesAdmin(admin.ModelAdmin):
    list_display = ('place_in_text', 'line_ref')
    list_filter = ('place_type',)
    ordering = ['place_in_text']
    search_fields = ['place_in_text']    
    
admin.site.register(placeNames, placeNamesAdmin) 

class poemSortAdmin(admin.ModelAdmin):
    list_display = ('poem_number', 'sort_order')
    ordering = ['sort_order']
    
admin.site.register(poemSort, poemSortAdmin)