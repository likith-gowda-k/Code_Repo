from django.contrib import admin
from . models import Watches, WatchesUploads, Wishlist, Cart, WatchReview

# Register your models here.

admin.site.register(Watches)


#WatchUploads
class WatchUploadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')
    list_filter = ('name', 'price')
    search_fields= ('name', 'description')
    fields=  ['name', 'description', 'price', 'image']
admin.site.register(WatchesUploads, WatchUploadsAdmin)

#WishList
# class WishlistAdmin(admin.ModelAdmin):
#     list_display= ('user', 'products')
#     list_filter= ('user','products')
# admin.site.register(Wishlist,  WishlistAdmin)
admin.site.register(Wishlist)


admin.site.register(Cart)

#Watch Review
class WatchReviewAdmin(admin.ModelAdmin):
    list_display= ('user', 'product', 'rating', 'review_text')
    list_filter =  ('user', 'product', 'rating')
admin.site.register(WatchReview, WatchReviewAdmin)
