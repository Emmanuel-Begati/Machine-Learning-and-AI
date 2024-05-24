from django.forms import ModelForm
from . models import approval

class ApprovalForm(ModelForm):
	class Meta:
		model=approval
		fields = '__all__'
		#exclude = 'firstname'