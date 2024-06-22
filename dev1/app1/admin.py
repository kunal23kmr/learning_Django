from django.contrib import admin
from .models import chaiVerity, chaiReview, chaiCertificate, Store
# Register your models here.


class chaiReviewInLine(admin.TabularInline):
    model = chaiReview
    extra = 2


class chaiVerityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'data_added')
    inlines = [chaiReviewInLine]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varieties',)


class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


admin.site.register(chaiVerity, chaiVerityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(chaiCertificate, chaiCertificateAdmin)
