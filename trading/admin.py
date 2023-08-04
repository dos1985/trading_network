from django.contrib import admin

from trading.models import Factory, RetailNetwork, IndividualEntrepreneur, Product


class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name", "debt_to_supplier", "created", "updated")
    list_filter = ('city', )
    actions = ['clear_debt']

    def supplier(self, obj):
        # Ссылка на поставщика
        return obj.supplier.name

    def clear_debt(self, request, queryset):
        # Очистить задолженность
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком у выбранных объектов."


admin.site.register(Factory, FactoryAdmin)



class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "debt_to_supplier", "supplier",  "created", "updated")
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        # Очистить задолженность
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком у выбранных объектов."

admin.site.register(RetailNetwork, RetailNetworkAdmin)


class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ("name", "debt_to_supplier", "supplier",  "created", "updated")
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        # Очистить задолженность
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком у выбранных объектов."

admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "debt_to_supplier", "supplier",  "created", "updated")
    list_filter = ('supplier__city',)# для фильтрации по городу поставщика
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        # Очистить задолженность
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком у выбранных объектов."

admin.site.register(Product, ProductAdmin)