from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, default='')
    birth_date = models.DateField(default=timezone.now)

    REQUIRED_FIELDS = []

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    civil_status = models.CharField(max_length=50, blank=True, default='')
    religion = models.CharField(max_length=50, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    educational_attainment = models.CharField(max_length=100, blank=True, default='')
    occupation = models.CharField(max_length=100, blank=True, default='')

class EconomicNumbers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    philhealth_num = models.CharField(max_length=15, blank=True)
    nhts_num = models.CharField(max_length=50, blank=True)
    patient_4ps_member = models.BooleanField(default=False)
    brgy_num = models.CharField(max_length=50, blank=True)
    family_num = models.CharField(max_length=50, blank=True)

class SocialHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    smoker = models.BooleanField(default=False)
    alcohol_intake = models.BooleanField(default=False)
    prohibited_drug = models.BooleanField(default=False)
    cigarette_sticks = models.IntegerField(blank=True, null=True, default=0)

class MedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diabetes = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    hpn = models.BooleanField(default=False)
    ptb = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    other_medical_history = models.CharField(max_length=255, blank=True)
    medication_taken = models.CharField(max_length=255, blank=True)
    family_planning = models.BooleanField(default=False)
    adult_immunization = models.CharField(max_length=100, blank=True)
    immunization_date = models.DateField(blank=True, null=True, default="")

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    datetime_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10)
    record_type = models.CharField(max_length=50)

class PediatricDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_age = models.CharField(max_length=50)
    father_age = models.CharField(max_length=50)
    birth_order = models.CharField(max_length=5)

class ImmunizationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tetanus_toxoid_mother_status = models.CharField(max_length=50, blank=True, default="")
    bcg = models.BooleanField(default=False)
    hepa = models.BooleanField(default=False)
    pental_1 = models.BooleanField(default=False)
    pental_2 = models.BooleanField(default=False)
    pental_3 = models.BooleanField(default=False)
    opv_1 = models.BooleanField(default=False)
    opv_2 = models.BooleanField(default=False)
    opv_3 = models.BooleanField(default=False)
    rota_1 = models.BooleanField(default=False)
    rota_2 = models.BooleanField(default=False)
    rota_3 = models.BooleanField(default=False)
    amv = models.BooleanField(default=False)
    mr = models.BooleanField(default=False)
    mmr = models.BooleanField(default=False)
    other_immunization = models.CharField(max_length=50, blank=True, default="")
    vitamin_a = models.BooleanField(default=False)
    breastfeeding = models.BooleanField(default=False)
    deworming = models.BooleanField(default=False)
    deworm_date = models.DateField(blank=True, default=None, null=True)

class ChildDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_of_birth = models.CharField(max_length=50)
    birth_weight = models.FloatField()
    birth_order = models.CharField(max_length=5)
    mother_name = models.CharField(max_length=50)
    birth_length = models.FloatField()
    birth_time = models.CharField(max_length=50)
    del_type_nsd = models.BooleanField(default=False)
    del_type_cs = models.BooleanField(default=False)
    del_type_dos = models.BooleanField(default=False)
    exclusively_bf = models.BooleanField(default=False)
    exclusively_mixed = models.BooleanField(default=False)
    exclusively_milk = models.BooleanField(default=False)
    
class NewbornStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ns_place = models.CharField(max_length=50, blank=True, default='')
    ns_date = models.DateField(blank=True, null=True, default=None)
    bcg_date = models.DateField(blank=True, null=True, default=None)
    bcg_place = models.CharField(max_length=50, blank=True, default='')
    dpt_opv_date = models.DateField(blank=True, null=True, default=None)
    dpt_opv_place = models.CharField(max_length=60, blank=True, default='')
    pcv_date = models.DateField(blank=True, null=True, default=None)
    pcv_place = models.CharField(max_length=50, blank=True, default='')
    ipv_date = models.DateField(blank=True, null=True, default=None)
    ipv_place = models.CharField(max_length=50, blank=True, default='')
    hepa_date = models.DateField(blank=True, null=True, default=None)
    hepa_place = models.CharField(max_length=50, blank=True, default='')

class Adult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    economic_numbers = models.ForeignKey('EconomicNumbers', on_delete=models.CASCADE)
    social_history = models.ForeignKey('SocialHistory', on_delete=models.CASCADE)
    medical_history = models.ForeignKey('MedicalHistory', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class Pediatric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    economic_numbers = models.ForeignKey(EconomicNumbers, on_delete=models.CASCADE)
    social_history = models.ForeignKey(SocialHistory, on_delete=models.CASCADE)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)
    pediatric_details = models.ForeignKey(PediatricDetails, on_delete=models.CASCADE)
    immunization_history = models.ForeignKey(ImmunizationHistory, on_delete=models.CASCADE, related_name='pediatric_immunization_history')
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    economic_numbers = models.ForeignKey(EconomicNumbers, on_delete=models.CASCADE)
    child_details = models.ForeignKey(ChildDetails, on_delete=models.CASCADE)
    newborn_status = models.ForeignKey(NewbornStatus, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

# Comment out models.py line 9 and models.py line 12 and forms.py lines 15-17 before adding superuser
# Uncomment after creating superuser account
    
# Create custom superuser manager to include birthdate as a required field




