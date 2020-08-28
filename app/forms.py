from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def validate_name(name):
    if len(name)>10:
        raise ValidationError("Name is not valid")
    return name

class SampleForm(forms.Form):
    name=forms.CharField(max_length=200,required=True,label="Name :",
    validators=[validate_name])

    email=forms.EmailField(max_length=100,required=True,label="Email :",
    validators=[validators.MinLengthValidator(10)])
    
    confirm_email=forms.EmailField(max_length=200,required=True,label="Confirm Email :")
    pwd=forms.CharField(min_length=8,max_length=15,required=True,label="Password :",widget=forms.PasswordInput(attrs={'placeholder':"password"}))
    profile_pic=forms.ImageField(max_length=200,required=True,label="Profile Picture :")
    botcacher=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)

    def clean(self,*args, **kwargs):
        clean_data=super().clean()  #getting all the data that is filled in the form
        email=clean_data.get('email')
        cemail=clean_data.get('confirm_email')
        if email==cemail:
            return cleaned_data
        self.add_error('email',"Both the Email are not same")  #this method will decide to which field we need to show the error
        #self.add_error("fieldname",error message)
        self.add_error('confirm_email',"Both the Email are not same")

    def clean_name(self):
        name=self.cleaned_data.get('name')  #is used to get the name that we have filled in the form
        if i in name:
            if i not in ('a'<=i<='z' or 'A'<=i<='Z'):
                raise ValidationError("Name must contain only alphabets")
        return name

    #Hint: Botcacher is like a Google captcha.  Helps to find who is filling the form by Bot or human.
    def clean_botcacher(self):
        data=self.cleaned_data.get('botcacher')
        if len(data)==0:
            return data
        self.add_error('name',"Hey kalla computer, I got you")  