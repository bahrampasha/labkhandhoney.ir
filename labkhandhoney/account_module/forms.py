from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        label= 'کلمه عبور',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput()
    )
