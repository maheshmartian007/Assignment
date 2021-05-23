from django import forms
from testapp.models import Player

class PlayerForm(forms.ModelForm):

	def clean_age(self):
		input_age = self.cleaned_data['age']
		# teams = ['Delhi Capitals', 'Sunrisers Hyderabad', 'Royal Challengers Bangalore', 'Rajasthan Royals', 'Chennai Super Kings', 
		# 'Kolkata Knight Riders', 'Punjab Kings', 'Mumbai Indians']

		if input_age > 100:
			raise forms.ValidationError('Age Should be less than 100')

		return input_age

	
	class Meta:
		model = Player
		fields = '__all__'