from rest_framework import serializers
from .models import (
    JobNotification,
    VacancyDetail,
    ExtraField
)


class VacancyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyDetail
        fields = "__all__"


class ExtraFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraField
        fields = (
            "field_name",
            "field_value"
        )


class JobNotificationSerializer(serializers.ModelSerializer):

    vacancy_details = VacancyDetailSerializer(
        many=True,
        read_only=True
    )

    extra_fields = ExtraFieldSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = JobNotification

        fields = (
            "id",
            "title",
            "advertisement_ref_no",
            "category",
            "total_vacancies",
            "start_date",
            "end_date",
            "qualification",
            "apply_online_link",
            "notification_pdf_link",
            "official_website",
            "vacancy_details",
            "extra_fields",
            "created_at",
            "updated_at",
            "admit_release_date",
            "start_date",
            "admit_release_date",
            "exam_date",
            "result_date",
            "dob_from",
            "dob_to",
            "admit_card_link",
        )