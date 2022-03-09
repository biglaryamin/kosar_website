from django.contrib import admin
from .models import Article,Category,Comment

def make_published(modeladmin, request , queryset):
    rows_update =queryset.update(status='p')
    if rows_update ==1:
        message_bit="منتشر شد"
    else:
        message_bit="منتشر شدند"
    modeladmin.message_user(request,"{} مقاله {}".format(rows_update,message_bit ) )
make_published.short_description="انتشار مقالات انتخاب شده"




def make_draft(modeladmin, request , queryset):
    rows_update =queryset.update(status='d')
    if rows_update ==1:
        message_bit="پیش نویس شد"
    else:
        message_bit="پیش نویس شدند"
    modeladmin.message_user(request,"{} مقاله {}".format(rows_update,message_bit ) )
make_draft.short_description="پیش نویس شدن مقالات انتخاب شده"

class ArticleAdmin(admin.ModelAdmin):
    list_display        = ('title','author','thumbnail_tag','slug','jpublish','status','category_to_str')
    list_filter         =('publish','status','author')
    search_fields       =('title','description')
    prepopulated_fields ={'slug':('title',)}
    ordering            = ['-status', '-publish']
    actions             =[make_published,make_draft]




admin.site.register(Article,ArticleAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','parent','title','slug','status')
    list_filter  =(['status'])
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}


admin.site.register(Category,CategoryAdmin)


admin.site.register(Comment)