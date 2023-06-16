from django.shortcuts import render

# Create your views here.
from app.models import *


import csv
from django.http import HttpResponse


def CSVFile(request):
    file='C:\\Users\\Lenovo\\OneDrive\\Desktop\\django\\Achyuth\\Scripts\\CSVFiles\\templates\\bank.csv'
    
    with open(file,'r') as f:
        csv_file=csv.reader(f)
        next(csv_file)
        for row in csv_file:
            BN=row[0].strip()
            Instance=Bank(Bank=BN)
            Instance.save()
    return HttpResponse("data inserted successfully in bank")



def BranchCsv(request):
    path='C:\\Users\\Lenovo\\OneDrive\\Desktop\\django\\Achyuth\\Scripts\\CSVFiles\\templates\\branch1.csv' 
    with open(path,'r') as f:
        csv_file=csv.reader(f)
        next(csv_file)
        for row in csv_file:
            bn=row[0]
            bo=Bank.objects.get_or_create(Bank=bn)[0]
            Instance=Branch(Bank=bo,
                            IFSC=row[1],
                            Branches=row[2],
                            address=row[3],
                            contact=row[4],
                            City=row[5],
                            District=row[6],
                            state=row[7])
            
            
            
            Instance.save()
    return HttpResponse("sucessfully")