from django.shortcuts import render, redirect
from ..models import SocialHistory, UserProfile, MedicalHistory
import json
from functools import wraps

def staff_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')  
        elif not request.user.is_staff:
            return redirect('home')  
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

@staff_login_required
def social_history_analysis(request):
   
    smoker_age_groups = {
        '0-20': SocialHistory.objects.filter(smoker=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': SocialHistory.objects.filter(smoker=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': SocialHistory.objects.filter(smoker=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': SocialHistory.objects.filter(smoker=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

 
    smoker_gender = {
        'Male': SocialHistory.objects.filter(smoker=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': SocialHistory.objects.filter(smoker=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

  
    prohibited_drugs_age_groups = {
        '0-20': SocialHistory.objects.filter(prohibited_drug=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': SocialHistory.objects.filter(prohibited_drug=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': SocialHistory.objects.filter(prohibited_drug=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': SocialHistory.objects.filter(prohibited_drug=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }


    prohibited_drugs_gender = {
        'Male': SocialHistory.objects.filter(prohibited_drug=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': SocialHistory.objects.filter(prohibited_drug=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

 
    alcohol_intake_age_groups = {
        '0-20': SocialHistory.objects.filter(alcohol_intake=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': SocialHistory.objects.filter(alcohol_intake=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': SocialHistory.objects.filter(alcohol_intake=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': SocialHistory.objects.filter(alcohol_intake=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }


    alcohol_intake_gender = {
        'Male': SocialHistory.objects.filter(alcohol_intake=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': SocialHistory.objects.filter(alcohol_intake=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }


    smoker_age_groups_json = json.dumps(smoker_age_groups)
    smoker_gender_json = json.dumps(smoker_gender)
    prohibited_drugs_age_groups_json = json.dumps(prohibited_drugs_age_groups)
    prohibited_drugs_gender_json = json.dumps(prohibited_drugs_gender)
    alcohol_intake_age_groups_json = json.dumps(alcohol_intake_age_groups)
    alcohol_intake_gender_json = json.dumps(alcohol_intake_gender)

    context = {
        'smoker_age_groups': smoker_age_groups_json,
        'smoker_gender': smoker_gender_json,
        'prohibited_drugs_age_groups': prohibited_drugs_age_groups_json,
        'prohibited_drugs_gender': prohibited_drugs_gender_json,
        'alcohol_intake_age_groups': alcohol_intake_age_groups_json,
        'alcohol_intake_gender': alcohol_intake_gender_json,
    }

    return render(request, 'base\staff-section\social_analysis.html', context)

def medical_history_analysis(request):
    
    diabetes_age_groups = {
        '0-20': MedicalHistory.objects.filter(diabetes=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': MedicalHistory.objects.filter(diabetes=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': MedicalHistory.objects.filter(diabetes=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': MedicalHistory.objects.filter(diabetes=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

    diabetes_gender = {
        'Male': MedicalHistory.objects.filter(diabetes=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': MedicalHistory.objects.filter(diabetes=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

  
    asthma_age_groups = {
        '0-20': MedicalHistory.objects.filter(asthma=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': MedicalHistory.objects.filter(asthma=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': MedicalHistory.objects.filter(asthma=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': MedicalHistory.objects.filter(asthma=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

    asthma_gender = {
        'Male': MedicalHistory.objects.filter(asthma=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': MedicalHistory.objects.filter(asthma=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }


    hypertension_age_groups = {
        '0-20': MedicalHistory.objects.filter(hypertension=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': MedicalHistory.objects.filter(hypertension=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': MedicalHistory.objects.filter(hypertension=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': MedicalHistory.objects.filter(hypertension=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

    hypertension_gender = {
        'Male': MedicalHistory.objects.filter(hypertension=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': MedicalHistory.objects.filter(hypertension=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

    pulmonary_tuberculosis_age_groups = {
        '0-20': MedicalHistory.objects.filter(pulmonary_tubercolosis=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': MedicalHistory.objects.filter(pulmonary_tubercolosis=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': MedicalHistory.objects.filter(pulmonary_tubercolosis=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': MedicalHistory.objects.filter(pulmonary_tubercolosis=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

    pulmonary_tuberculosis_gender = {
        'Male': MedicalHistory.objects.filter(pulmonary_tubercolosis=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': MedicalHistory.objects.filter(pulmonary_tubercolosis=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

    cancer_age_groups = {
        '0-20': MedicalHistory.objects.filter(cancer=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': MedicalHistory.objects.filter(cancer=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': MedicalHistory.objects.filter(cancer=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': MedicalHistory.objects.filter(cancer=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

    cancer_gender = {
        'Male': MedicalHistory.objects.filter(cancer=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': MedicalHistory.objects.filter(cancer=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

    cough_2_weeks_age_groups = {
        '0-20': MedicalHistory.objects.filter(cough_2_weeks=True, user__userprofile__age__lte=20).values('user').distinct().count(),
        '20-40': MedicalHistory.objects.filter(cough_2_weeks=True, user__userprofile__age__gt=20, user__userprofile__age__lte=40).values('user').distinct().count(),
        '40-60': MedicalHistory.objects.filter(cough_2_weeks=True, user__userprofile__age__gt=40, user__userprofile__age__lte=60).values('user').distinct().count(),
        '60+': MedicalHistory.objects.filter(cough_2_weeks=True, user__userprofile__age__gt=60).values('user').distinct().count(),
    }

    cough_2_weeks_gender = {
        'Male': MedicalHistory.objects.filter(cough_2_weeks=True, user__userprofile__sex='Male').values('user').distinct().count(),
        'Female': MedicalHistory.objects.filter(cough_2_weeks=True, user__userprofile__sex='Female').values('user').distinct().count(),
    }

   
    
    diabetes_age_groups_json = json.dumps(diabetes_age_groups)
    diabetes_gender_json = json.dumps(diabetes_gender)
    asthma_age_groups_json = json.dumps(asthma_age_groups)
    asthma_gender_json = json.dumps(asthma_gender)
    hypertension_age_groups_json = json.dumps(hypertension_age_groups)
    hypertension_gender_json = json.dumps(hypertension_gender)
    pulmonary_tuberculosis_age_groups_json = json.dumps(pulmonary_tuberculosis_age_groups)
    pulmonary_tuberculosis_gender_json = json.dumps(pulmonary_tuberculosis_gender)
    cancer_age_groups_json = json.dumps(cancer_age_groups)
    cancer_gender_json = json.dumps(cancer_gender)
    cough_2_weeks_age_groups_json = json.dumps(cough_2_weeks_age_groups)
    cough_2_weeks_gender_json = json.dumps(cough_2_weeks_gender)

    context = {
        'diabetes_age_groups': diabetes_age_groups_json,
        'diabetes_gender': diabetes_gender_json,
        'asthma_age_groups': asthma_age_groups_json,
        'asthma_gender': asthma_gender_json,
        'hypertension_age_groups': hypertension_age_groups_json,
        'hypertension_gender': hypertension_gender_json,
        'pulmonary_tuberculosis_age_groups': pulmonary_tuberculosis_age_groups_json,
        'pulmonary_tuberculosis_gender': pulmonary_tuberculosis_gender_json,
        'cancer_age_groups': cancer_age_groups_json,
        'cancer_gender': cancer_gender_json,
        'cough_2_weeks_age_groups': cough_2_weeks_age_groups_json,
        'cough_2_weeks_gender': cough_2_weeks_gender_json,
    }


    return render(request, 'base\staff-section\medical_analysis.html', context)
