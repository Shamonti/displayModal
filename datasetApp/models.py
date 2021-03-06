from django.db import models

# Create your models here.
class Dataset(models.Model):
  
  name = models.CharField(("name"),max_length=255)
  email = models.CharField(('email'),max_length=255)
  first_name = models.CharField(('first name'),max_length=255)
  last_name = models.CharField(('last name'),max_length=255)
  phone = models.IntegerField(('phone'))
  job_title = models.CharField(('title'),max_length=255)
  functions = models.CharField(('functions'),max_length=255)
  detailed_functions = models.CharField(('detailed function'),max_length=255)
  seniority = models.CharField(('seniority'),max_length=255)
  city = models.CharField(('city'),max_length=255)
  state = models.CharField(('state'),max_length=255)
  country = models.CharField(('country'),max_length=255)
  postal_code = models.IntegerField(('postal code'))
  linekdin = models.URLField(('linkedin url'),max_length=200)
  organization = models.CharField(('organization name'),max_length=255)
  domain = models.CharField(('organization domain'),max_length=255)
  organization_phone = models.IntegerField(('organization phone'))
  organization_facebook = models.URLField(('organization facebook url'),max_length=200)
  organization_linkedin = models.URLField(('organization linkedin numerical urls'),max_length=200)
  organization_twitter = models.URLField(('organization twitter url'),max_length=200)
  organization_website = models.URLField(('organization website url'),max_length=200)
  organization_angellist = models.URLField(('organization angellist url'),max_length=200)
  organization_founded = models.IntegerField(('organization_founded_year'))
  hq_city = models.CharField(('organization_hq_location_city'),max_length=255)
  hq_postal_code = models.IntegerField(('organization_hq_location_postal_code'))
  hq_state = models.CharField(('organization_hq_location_state'),max_length=255)
  hq_country = models.CharField(('organization_hq_location_country'),max_length=255)
  num_current_employees = models.IntegerField(('organization_num_current_employees'))
  languages = models.CharField(('organization_languages'),max_length=255)
  industries = models.CharField(('organization_industries'),max_length=255)