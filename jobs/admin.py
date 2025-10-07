from django.contrib import admin
from .models import JobNotification, VacancyDetail


class VacancyDetailInline(admin.TabularInline):
    model = VacancyDetail
    extra = 1
    fields = ("post_name", "vacancy_number")


@admin.register(JobNotification)
class JobNotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "total_vacancies", "start_date", "end_date")
    list_filter = ("category", "start_date")
    search_fields = ("title", "advertisement_ref_no")
    inlines = [VacancyDetailInline]


@admin.register(VacancyDetail)
class VacancyDetailAdmin(admin.ModelAdmin):
    list_display = ("post_name", "vacancy_number", "job_notification")
    search_fields = ("post_name",)