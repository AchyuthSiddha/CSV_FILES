from django.db import models

# Create your models here.


class Bank(models.Model):
    Bank=models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.Bank
    
    
class Branch(models.Model):
    Bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
    IFSC=models.CharField(max_length=100,primary_key=True)
    Branches=models.CharField(max_length=100)
    address=models.TextField()
    contact=models.IntegerField()
    City=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    
    # BANK,IFSC,BRANCH,ADDRESS,CONTACT,CITY,DISTRICT,STATE
    
    
    def __str__(self):
        return self.Branches