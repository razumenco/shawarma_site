from django.contrib import admin

from .models import Shawarma, Review


class ShawarmaAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'short_name',
        'standart_price',
        'description',
        'start_time',
        'stop_time',
        'working_status',
        'location_iframe',
        'main_image'
    ]
    list_editable = ['standart_price', 'description']


admin.site.register(Shawarma, ShawarmaAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'about',
        'mark',
        'comment'
    ]


admin.site.register(Review, ReviewAdmin)

