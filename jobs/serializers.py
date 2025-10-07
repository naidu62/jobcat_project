# jobs/serializers.py
from rest_framework import serializers
from .models import JobNotification, VacancyDetail


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyDetail
        fields = ("id", "post_name", "vacancy_number")


class JobNotificationSerializer(serializers.ModelSerializer):
    vacancy_details = VacancyDetailSerializer(many=True, read_only=True)

    class Meta:
        model = JobNotification
        fields = (
            "id",
            "job_uid",
            "title",
            "advertisement_ref_no",
            "category",
            "total_vacancies",
            "start_date",
            "end_date",
            "admit_release_date",
            "exam_date",
            "result_date",
            "extended_date",
            "fee_general",
            "fee_obc",
            "fee_sc",
            "fee_st",
            "fee_ews",
            "fee_female",
            "fee_ex_serviceman",
            "fee_ph",
            "fee_other",
            "dob_from",
            "dob_to",
            "age_relaxation",
            "qualification",
            "apply_online_link",
            "admit_card_link",
            "notification_pdf_link",
            "official_website",
            "vacancy_details",
            "created_at",
            "updated_at",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in list(data.items()):
            if value in (None, "", [], {}):
                data[key] = "Not Available"
        return data