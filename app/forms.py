from django import forms
from .models import Member,Contact


# creating a form
class MemberForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Member
        # specify fields to be used
        fields =['Name', 'Email', 'Mobile', 'Gender', 'Division', 'State', 'Society','Outreach', 'Initiative', 'City', 'Education', 'InstituteName', 'Std', 'Department', 'Position', 'WhyHire', 'WhyJoin', 'Timeslot', 'Resume']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","message"]
