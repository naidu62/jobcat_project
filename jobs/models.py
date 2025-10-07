# jobs/models.py
from django.db import models
import uuid

class JobNotification(models.Model):
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

    # 6️⃣ Important Links
    apply_online_link = models.URLField(blank=True, default="")
    admit_card_link = models.URLField(blank=True, default="")
    notification_pdf_link = models.URLField(blank=True, default="")
    official_website = models.URLField(blank=True, default="")

    # 8️⃣ System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"JobNotification {self.job_uid}"


class VacancyDetail(models.Model):
    job_notification = models.ForeignKey(
        JobNotification, on_delete=models.CASCADE, related_name='vacancy_details'
    )
    post_name = models.CharField(max_length=255)
    vacancy_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.post_name} ({self.vacancy_number or 'NA'})"