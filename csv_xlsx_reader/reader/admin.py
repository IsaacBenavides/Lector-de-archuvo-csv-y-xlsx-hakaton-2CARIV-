from django.contrib import admin

# Register your models here.
from reader.models import Xlsx, Uploader, CsvModel


@admin.register(Xlsx)
class XlsxAdmin(admin.ModelAdmin):
    list_display = ('country', 'item_type', 'sales_channel', 'order_priority', 'order_date', 'order_id', 'ship_date', 'units_sold', 'unit_price', 'unit_cost', 'total_revenue',
                    'total_cost', 'total_profit')
    search_fields = ('country', 'item_type', 'sales_channel', 'order_priority')


admin.site.register(Uploader)


@admin.register(CsvModel)
class CsvModelAdmin(admin.ModelAdmin):
    list_display = ("date", "description", "deposits", "withdrawls", "balance")
