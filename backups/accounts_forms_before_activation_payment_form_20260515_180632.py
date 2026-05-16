from django import forms
from django.contrib.auth import get_user_model
from .models import AdminRequest


User = get_user_model()


class PublicRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']

        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'phone': 'Teléfono',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.ROLE_USER
        user.admin_approved = False
        user.is_staff = False
        user.is_superuser = False
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class OwnerKYCRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellidos')
    user_phone = forms.CharField(label='Teléfono personal')

    class Meta:
        model = AdminRequest
        fields = [
            'owner_full_name',
            'phone',
            'city',
            'address',
            'identity_number',
            'identity_document',
            'selfie_photo',

            'company_name',
            'taxi_count',

            'main_taxi_brand',
            'main_taxi_model',
            'main_taxi_plate',
            'main_taxi_color',

            'taxi_registration_document',
            'taxi_license_document',
            'ownership_proof_document',

            'message',
        ]

        labels = {
            'owner_full_name': 'Nombre completo del propietario',
            'phone': 'Teléfono de contacto',
            'city': 'Ciudad',
            'address': 'Dirección',
            'identity_number': 'Número de documento de identidad',
            'identity_document': 'Documento de identidad',
            'selfie_photo': 'Selfie o foto del propietario',

            'company_name': 'Nombre de empresa o propietario',
            'taxi_count': 'Número de taxis',

            'main_taxi_brand': 'Marca del taxi principal',
            'main_taxi_model': 'Modelo del taxi principal',
            'main_taxi_plate': 'Matrícula del taxi principal',
            'main_taxi_color': 'Color del taxi principal',

            'taxi_registration_document': 'Documento/matrícula del taxi',
            'taxi_license_document': 'Licencia o permiso del taxi',
            'ownership_proof_document': 'Prueba de propiedad del taxi',

            'message': 'Mensaje adicional',
        }

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise forms.ValidationError('Las contraseñas no coinciden.')

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya existe.')

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya existe.')

        return cleaned_data

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone=self.cleaned_data['user_phone'],
            role=User.ROLE_USER,
            admin_approved=False,
            is_staff=False,
            is_superuser=False,
        )
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        admin_request = super().save(commit=False)
        admin_request.user = user
        admin_request.status = AdminRequest.STATUS_PENDING

        if commit:
            admin_request.save()

        return user, admin_request


class AdminRequestForm(forms.ModelForm):
    class Meta:
        model = AdminRequest
        fields = [
            'company_name',
            'owner_full_name',
            'phone',
            'city',
            'taxi_count',
            'message',
        ]

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
