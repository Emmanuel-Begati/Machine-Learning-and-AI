from django.db import models

# Create your models here.
class approvals(models.Model):
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes','Yes'),
        ('No', 'No')
    )
    GRADUATED_CHOICES = (
        ('Graduate','Graduate'),
        ('Not_Graduate', 'Not_Graduate')
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes','Yes'),
        ('No', 'No')
    )
    AREA_CHOICES = (
        ('Urban','Urban'),
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban')
    )
    
        
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.IntegerField()
    applicantincome = models.FloatField()
    coapplicantincome = models.FloatField()
    loanamount = models.FloatField()
    loanterm = models.IntegerField()
    credithistory = models.FloatField(default=0)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    married=models.CharField(max_length=10, choices=MARRIED_CHOICES)
    graduatededucation=models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    selfemployed=models.CharField(max_length=10, choices=SELFEMPLOYED_CHOICES)
    area=models.CharField(max_length=10, choices=AREA_CHOICES)
    
    def __str__(self):
        return self.firstname