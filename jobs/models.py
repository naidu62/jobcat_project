# jobs/models.py
from django.db import models
import uuid

class JobNotification(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('closed', 'Closed'),
        ('archived', 'Archived'),
    ]

    CATEGORY_CHOICES = [
        ('railway', 'Railway'),
        ('police', 'Police'),
        ('banking', 'Banking'),
        ('andhra_pradesh', 'Andhra Pradesh'),
        # add more if you want
    ]

    # 1️⃣ Basic Info
    title = models.CharField("Notification Name", max_length=255)
    advertisement_ref_no = models.CharField(max_length=100, blank=True, default="")
    job_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, default="")
    total_vacancies = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    # 2️⃣ Important Dates
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    admit_release_date = models.DateField(blank=True, null=True)
    exam_date = models.DateField(blank=True, null=True)
    result_date = models.DateField(blank=True, null=True)
    extended_date = models.TextField(blank=True, default="")

    # 3️⃣ Application Fee (strings so text like "Rs. 200" or "Exempt")
    fee_general = models.CharField(max_length=80, blank=True, default="")
    fee_obc = models.CharField(max_length=80, blank=True, default="")
    fee_sc = models.CharField(max_length=80, blank=True, default="")
    fee_st = models.CharField(max_length=80, blank=True, default="")
    fee_ews = models.CharField(max_length=80, blank=True, default="")
    fee_female = models.CharField(max_length=80, blank=True, default="")
    fee_ex_serviceman = models.CharField(max_length=80, blank=True, default="")
    fee_ph = models.CharField(max_length=80, blank=True, default="")
    fee_other = models.CharField(max_length=80, blank=True, default="")

    # 4️⃣ Age Limit
    dob_from = models.TextField(blank=True, default="")
    dob_to = models.TextField(blank=True, default="")
    age_relaxation = models.TextField(blank=True, default="")

    # 5️⃣ Qualification
    qualification = models.TextField(blank=True, default="")

    # 6️⃣ Job Description & Details (NEW)
    job_description = models.TextField(blank=True, default="", help_text="Full job description and overview")
    responsibilities = models.TextField(blank=True, default="", help_text="Key responsibilities and duties")
    selection_process = models.TextField(blank=True, default="", help_text="e.g., Written exam → Interview → Document verification")
    cutoff_marks = models.CharField(max_length=200, blank=True, default="", help_text="Expected cutoff marks")
    vacancies_breakdown = models.TextField(blank=True, default="", help_text="Gen: 50, OBC: 30, SC: 15, ST: 5")

    # 7️⃣ Important Links
    apply_online_link = models.URLField(blank=True, default="")
    admit_card_link = models.URLField(blank=True, default="")
    notification_pdf_link = models.URLField(blank=True, default="")
    official_website = models.URLField(blank=True, default="")

    # 8️⃣ System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"JobNotification {self.job_uid}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Job Notification'
        verbose_name_plural = 'Job Notifications'


class VacancyDetail(models.Model):
    job_notification = models.ForeignKey(
        JobNotification, on_delete=models.CASCADE, related_name='vacancy_details'
    )
    post_name = models.CharField(max_length=255)
    vacancy_number = models.IntegerField(blank=True, null=True)
    
    # NEW FIELDS - Salary Info
    salary_range = models.CharField(max_length=150, blank=True, default="", help_text="e.g., ₹25,000-35,000 per month")
    
    # NEW FIELDS - Experience & Qualifications
    experience_required = models.CharField(max_length=100, blank=True, default="", help_text="e.g., 2-5 years or Fresher")
    qualification_specific = models.TextField(blank=True, default="", help_text="Specific requirements for this post")
    skills_required = models.TextField(blank=True, default="", help_text="Technical and soft skills needed")
    
    # NEW FIELDS - Additional Info
    department = models.CharField(max_length=150, blank=True, default="")
    location = models.CharField(max_length=150, blank=True, default="", help_text="Job location/posting state")
    
    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post_name} ({self.vacancy_number or 'NA'}) - {self.salary_range}"

    class Meta:
        ordering = ['post_name']
        verbose_name = 'Vacancy Detail'
        verbose_name_plural = 'Vacancy Details'


class JobSeeker(models.Model):
    """User profile for job seekers"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default="")
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    # Additional Info
    headline = models.CharField(max_length=200, blank=True, default="", help_text="Professional headline")
    bio = models.TextField(blank=True, default="")
    
    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = 'Job Seeker'
        verbose_name_plural = 'Job Seekers'


class JobApplication(models.Model):
    """Track job applications from users"""
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('selected', 'Selected'),
        ('completed', 'Completed'),
    ]

    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='applications')
    vacancy_detail = models.ForeignKey(VacancyDetail, on_delete=models.CASCADE, related_name='applications')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # Optional: Interview date, notes
    interview_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, default="")
    
    def __str__(self):
        return f"{self.job_seeker.name} - {self.vacancy_detail.post_name} ({self.status})"

    class Meta:
        ordering = ['-applied_date']
        unique_together = ['job_seeker', 'vacancy_detail']  # Prevent duplicate applications
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'


class JobNotification(models.Model):
    """Notification alerts for job seekers"""
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('never', 'Never'),
    ]

    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='job_notifications')
    category = models.CharField(max_length=50, choices=JobNotification.CATEGORY_CHOICES)
    
    is_enabled = models.BooleanField(default=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='weekly')
    
    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.job_seeker.name} - {self.category}"

    class Meta:
        verbose_name = 'Job Notification'
        verbose_name_plural = 'Job Notifications'
        unique_together = ['job_seeker', 'category']
