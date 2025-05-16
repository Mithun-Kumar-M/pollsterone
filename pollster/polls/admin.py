from django.contrib import admin



from .models import question,choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin area"
admin.site.index_title = "Welcome to the Pollster admin area"
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = choice 
    extra = 3 
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
                 ('Date Information',  {'fields' : ['pub_date'] , 'classes':['collapse']}),]
    inlines = [ChoiceInLine]
    
admin.site.register(question,QuestionAdmin)

# admin.site.register(choice)