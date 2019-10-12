from django import forms


class FeedBackForm(forms.Form):
    Name = forms.CharField(
        label="Name: ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    MailId = forms.EmailField(
        label="Email Id: ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mail Id'
            }
        )

    )
    Profession = forms.CharField(
        label="Profession: ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Student/Teacher/etc'
            }
        )
    )
    Sub = forms.CharField(
        label="Subject",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Help/suggestion/etc'
            }
        )
    )
    Msg = forms.CharField(
        label="Feedback: ",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Message Here!'
            }
        )
    )