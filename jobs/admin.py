from django.contrib import admin
from .models import JobNotification, VacancyDetail, JobSeeker, JobApplication, JobNotificationAlert


# ========== VacancyDetail Inline ==========
class VacancyDetailInline(admin.TabularInline):
    model = VacancyDetail
    extra = 1
    fields = ("post_name", "vacancy_number", "salary_range", "experience_required", "location")
    readonly_fields = ("created_at", "updated_at")


# ========== JobNotification Admin ==========
@admin.register(JobNotification)
class JobNotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "is_active", "total_vacancies", "start_date", "end_date")
    list_filter = ("category", "status", "is_active", "start_date")
    search_fields = ("title", "advertisement_ref_no", "job_description")
    readonly_fields = ("job_uid", "created_at", "updated_at")
    
    fieldsets = (
        ('📋 Basic Information', {
            'fields': ('title', 'advertisement_ref_no', 'job_uid', 'category', 'status', 'is_active', 'total_vacancies')
        }),
        ('📝 Job Details', {
            'fields': ('job_description', 'responsibilities', 'selection_process', 'qualification', 'cutoff_marks', 'vacancies_breakdown'),
            'classes': ('collapse',)
        }),
        ('📅 Important Dates', {
            'fields': ('start_date', 'end_date', 'admit_release_date', 'exam_date', 'result_date', 'extended_date'),
        }),
        ('💰 Application Fees', {
            'fields': ('fee_general', 'fee_obc', 'fee_sc', 'fee_st', 'fee_ews', 'fee_female', 'fee_ex_serviceman', 'fee_ph', 'fee_other'),
            'classes': ('collapse',)
        }),
        ('👥 Age Limits', {
            'fields': ('dob_from', 'dob_to', 'age_relaxation'),
            'classes': ('collapse',)
        }),
        ('🔗 Important Links', {
            'fields': ('apply_online_link', 'admit_card_link', 'notification_pdf_link', 'official_website'),
        }),
        ('⏱️ System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [VacancyDetailInline]


# ========== VacancyDetail Admin ==========
@admin.register(VacancyDetail)
class VacancyDetailAdmin(admin.ModelAdmin):
    list_display = ("post_name", "vacancy_number", "salary_range", "experience_required", "job_notification", "location")
    list_filter = ("job_notification__category", "location", "created_at")
    search_fields = ("post_name", "job_notification__title", "department")
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        ('🏢 Post Information', {
            'fields': ('job_notification', 'post_name', 'vacancy_number', 'department', 'location')
        }),
        ('💼 Compensation & Experience', {
            'fields': ('salary_range', 'experience_required')
        }),
        ('📚 Qualifications & Skills', {
            'fields': ('qualification_specific', 'skills_required'),
            'classes': ('collapse',)
        }),
        ('⏱️ System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ========== JobSeeker Admin ==========
@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "headline", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        ('👤 Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('📸 Media & Profile', {
            'fields': ('profile_picture', 'resume', 'headline', 'bio')
        }),
        ('⏱️ System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ========== JobApplication Admin ==========
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("get_seeker_name", "get_post_name", "status", "applied_date", "interview_date")
    list_filter = ("status", "applied_date", "vacancy_detail__job_notification__category")
    search_fields = ("job_seeker__name", "vacancy_detail__post_name")
    readonly_fields = ("applied_date", "updated_date")
    
    fieldsets = (
        ('📋 Application Details', {
            'fields': ('job_seeker', 'vacancy_detail', 'status')
        }),
        ('📅 Dates', {
            'fields': ('applied_date', 'updated_date', 'interview_date')
        }),
        ('📝 Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    
    def get_seeker_name(self, obj):
        return obj.job_seeker.name
    get_seeker_name.short_description = 'Job Seeker'
    
    def get_post_name(self, obj):
        return obj.vacancy_detail.post_name
    get_post_name.short_description = 'Applied For'


# ========== JobNotificationAlert Admin ==========
@admin.register(JobNotificationAlert)
class JobNotificationAlertAdmin(admin.ModelAdmin):
    list_display = ("job_seeker_name", "category", "frequency", "is_enabled", "created_at")
    list_filter = ("is_enabled", "frequency", "category", "created_at")
    search_fields = ("job_seeker__name", "job_seeker__email")
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        ('🔔 Notification Settings', {
            'fields': ('job_seeker', 'category', 'frequency', 'is_enabled')
        }),
        ('⏱️ System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def job_seeker_name(self, obj):
        return f"{obj.job_seeker.name} ({obj.job_seeker.email})"
    job_seeker_name.short_description = 'Job Seeker'
