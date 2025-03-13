from django import forms
from backend.core.models import CustomUser, Country

CURRENCY_CHOICES = [
    ('', '-- None --'),
    ('USD', 'USD'),
    ('MYR', 'MYR'),
    ('EUR', 'EUR'),
]

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if CustomUser.objects.filter(username__iexact=username).exists() or CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This username or email is already taken.")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class AdvancedSearchForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        required=True,
        label="Country"
    )
    days = forms.IntegerField(min_value=1, label="Number of Days")
    pax = forms.IntegerField(min_value=1, label="Number of People")
    budget = forms.DecimalField(required=False, min_value=0, label="Budget")
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, required=False, label="Currency")
    visa_enabled = forms.BooleanField(required=False, label="Visa Feature")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        for field_name in ['country', 'days', 'pax', 'budget', 'currency']:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['class'] = 'input-field'

        if not user or not user.is_authenticated:
            self.fields['budget'].widget = forms.HiddenInput()
            self.fields['currency'].widget = forms.HiddenInput()
            self.fields['visa_enabled'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        budget = cleaned_data.get('budget')
        currency = cleaned_data.get('currency')

        if budget and not currency:
            self.add_error('currency', "Please select a currency if you specify a budget.")

        return cleaned_data