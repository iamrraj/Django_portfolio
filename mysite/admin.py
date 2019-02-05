from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Student,Contact,work,About,Cdetail,blog


# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		(None, {'fields': ['model_pic']}),
# 		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
# 	]
#
# 	list_display = ('model_pic', 'pub_date')
# 	list_display = ('model_pic', 'pub_date', 'was_published_recently')
# 	list_filter = ['pub_date']
# 	search_fields = ['question']



class QuestionAdmin(admin.ModelAdmin):
#     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('title', 'pub_date')
    list_display = ('title','by', 'pub_date', 'was_published_recently')
    list_filter = [ 'pub_date','by','title' ]
    search_fields = ['by','title','pub_date']


    def image_tag( self, obj ):
        return format_html( '<img src="{}" />'.format( obj.image.url ) )


        image_tag.short_description = 'Image'

        list_display = [ 'image_tag', ]



class ContactAdmin(admin.ModelAdmin):
#     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('fname', 'lname')
    list_display = ('fname', 'lname', 'phone','email','message')
    list_filter = [ 'fname','email']
    search_fields = ['fname','lname','email']




class DeatilsAdmin(admin.ModelAdmin):
#     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('phone', 'pub_date')
    list_display = ('phone','email', 'pub_date', 'was_published_recently')
    list_filter = [ 'phone','pub_date','email' ]
    # search_fields = ['phone','title','pub_date']
#
# class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
#
#     readonly_fields = [..., "headshot_image"]
#
#     def headshot_image(self, obj):
#         return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
#             url = obj.image.url,
#             width=obj.image.width,
#             height=obj.image.height,
#             )
#     )

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_display = ('link', 'by','title', 'pub_date', 'was_published_recently')
    list_filter = [ 'pub_date', 'by', 'title' ]
    search_fields = [ 'by', 'title', 'pub_date' ]

    def author_link(self, book):
        url = reverse("admin:book_author_change", args=[book.link.id])
        link = '<a href="%s">%s</a>' % (url, book.link.name)
        return mark_safe(link)
    author_link.short_description = 'Author'



admin.site.register(Student)
admin.site.register(Contact,ContactAdmin)
admin.site.register(About)
admin.site.register(blog,BookAdmin )
admin.site.register(Cdetail,DeatilsAdmin)
admin.site.register(work,QuestionAdmin)


