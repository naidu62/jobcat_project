from django.db import models


class JobNotification(models.Model):

    # Basic
    title = models.CharField(
        max_length=255
    )

    advertisement_ref_no = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # Category (simple text)
    category = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    total_vacancies = models.IntegerField(
        blank=True,
        null=True
    )

    # Dates
    start_date = models.DateField(
        blank=True,
        null=True
    )

    end_date = models.DateField(
        blank=True,
        null=True
    )

    admit_release_date = models.DateField(

        blank=True,

        null=True
    )

    exam_date = models.DateField(

        blank=True,

        null=True

    )
    result_date = models.DateField(

        blank=True,

        null=True

)   
    # Age Limit

    dob_from = models.DateField(

        blank=True,

        
        null=True

    )

    dob_to = models.DateField(

        blank=True,

        null=True

)

    # Qualification
    qualification = models.TextField(
        blank=True,
        default=""
    )

    # Links
    apply_online_link = models.URLField(
        blank=True,
        default=""
    )
    admit_card_link = models.URLField(
        blank=True,
        default=""
    )
    notification_pdf_link = models.URLField(
        blank=True,
        default=""
    )

    official_website = models.URLField(
        blank=True,
        default=""
    )

    # System
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class VacancyDetail(models.Model):

    job_notification = models.ForeignKey(
        JobNotification,
        on_delete=models.CASCADE,
        related_name="vacancy_details"
    )

    post_name = models.CharField(
        max_length=255
    )

    vacancy_number = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.post_name


class ExtraField(models.Model):

    job_notification = models.ForeignKey(
        JobNotification,
        on_delete=models.CASCADE,
        related_name="extra_fields"
    )

    field_name = models.CharField(
        max_length=100
    )

    field_value = models.TextField()

    def __str__(self):
        return self.field_name