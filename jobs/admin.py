from django.contrib import admin
from .models import (
    JobNotification,
    VacancyDetail,
    ExtraField
)


class VacancyDetailInline(admin.TabularInline):
    model = VacancyDetail
    extra = 1


class ExtraFieldInline(admin.TabularInline):
    model = ExtraField
    extra = 1


@admin.register(JobNotification)
class JobNotificationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "category",
        "total_vacancies",
        "start_date",
        "end_date",
        "admit_release_date",
        "exam_date",
        "result_date"
    )

    search_fields = (
        "title",
        "advertisement_ref_no",
    )

    list_filter = (
        "category",
        "start_date",
        "admit_release_date",
        "exam_date",  
    )

    inlines = [
        VacancyDetailInline,
        ExtraFieldInline
    ]


@admin.register(VacancyDetail)
class VacancyDetailAdmin(admin.ModelAdmin):

    list_display = (
        "post_name",
        "vacancy_number",
        "job_notification",
    )

    search_fields = (
        "post_name",
    )


@admin.register(ExtraField)
class ExtraFieldAdmin(admin.ModelAdmin):

    list_display = (
        "field_name",
        "job_notification",
    )

    search_fields = (
        "field_name",
    )