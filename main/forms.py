from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=[ 'username', 'email','password1','password2']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        

        self.fields['username'].widget.attrs.update({
            'type':'text',  
            'placeholder':'Username',
            'class':'form-control',
            
            'id':'inputUsername'
                    
        })

        

        self.fields['email'].widget.attrs.update({
            'type':'email',  
            'placeholder':'Email',
            'class':'form-control',
            
            'id':'inputEmail'
                    
        })

        self.fields['password1'].widget.attrs.update({
            'type':'password',  
            'placeholder':'password',
            'class':'form-control',
            
            'id':'inputPassword'
                    
        })

        self.fields['password2'].widget.attrs.update({
            'type':'password',  
            'placeholder':'Retype Password',
            'class':'form-control',
            
            'id':'inputPassword'
                    
        })