from django.contrib import admin

# Register your models here.
from trade.models import TradePost

class TradePostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'content', 'author', 'price',
                    'product_status', 'payment', 'shipping', 'create_date', 'modify_date', 'image']

admin.site.register(TradePost, TradePostAdmin)