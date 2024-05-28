from django.shortcuts import render
from . forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import approval
from . serializers import approvalSerializer
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class ApprovalsView(viewsets.ModelViewSet):
	queryset = approval.objects.all()
	serializer_class = approvalSerializer
		
@api_view(["POST"])
def approvereject(request):
	try:
		mdl=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		scalers=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl .predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def cxcontact(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
			First_Name=form.cleaned_data['First_Name']
			Last_Name=form.cleaned_data['Last_Name']
			Dependents=form.cleaned_data['Dependents']
			ApplicantIncome=form.cleaned_data['ApplicantIncome']
			CoapplicantIncome=form.cleaned_data['CoapplicantIncome']
			LoanAmount=form.cleaned_data['LoanAmount']
			Loan_Amount_Term=form.cleaned_data['Loan_Amount_Term']
			Credit_History=form.cleaned_data['Credit_History']
			Gender=form.cleaned_data['Gender']
			Marrige=form.cleaned_data['Marrige']
			Education=form.cleaned_data['Education']
			Self_Employed=form.cleaned_data['Self_Employed']
			Property_Area=form.cleaned_data['Property_Area']
			# print(First_Name, Last_Name, Dependents, Marrige, Property_Area)
			print(f"""
         
         
				First Name: {First_Name}
    
    
         		""")
			return render(request, 'theAPI/cxform.html', {'form':form})	
	else:
		form = ApprovalForm()
		return render(request, 'theAPI/cxform.html', {'form':form})