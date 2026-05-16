from django import forms
from vehicles.models import Vehicle
from drivers.models import Driver
from payments.models import DriverPayment
from damages.models import VehicleDamage


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'internal_code',
            'plate_number',
            'brand',
            'model',
            'color',
            'year',
            'daily_target_amount',
            'status',
            'photo',
            'registration_document',
            'insurance_document',
            'notes',
        ]

        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'assigned_vehicle',
            'full_name',
            'phone',
            'email',
            'identity_number',
            'license_number',
            'address',
            'photo',
            'identity_document',
            'license_document',
            'start_date',
            'daily_payment_amount',
            'payment_day',
            'status',
            'notes',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        if company:
            self.fields['assigned_vehicle'].queryset = Vehicle.objects.filter(company=company)
        else:
            self.fields['assigned_vehicle'].queryset = Vehicle.objects.none()


class DriverPaymentForm(forms.ModelForm):
    class Meta:
        model = DriverPayment
        fields = [
            'driver',
            'vehicle',
            'payment_date',
            'expected_amount',
            'paid_amount',
            'notes',
        ]

        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        if company:
            self.fields['driver'].queryset = Driver.objects.filter(company=company, status='active')
            self.fields['vehicle'].queryset = Vehicle.objects.filter(company=company)
        else:
            self.fields['driver'].queryset = Driver.objects.none()
            self.fields['vehicle'].queryset = Vehicle.objects.none()


class VehicleDamageForm(forms.ModelForm):
    class Meta:
        model = VehicleDamage
        fields = [
            'vehicle',
            'driver',
            'title',
            'description',
            'estimated_cost',
            'final_cost',
            'photo',
            'damage_date',
            'repaired_date',
            'status',
        ]

        widgets = {
            'damage_date': forms.DateInput(attrs={'type': 'date'}),
            'repaired_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        if company:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(company=company)
            self.fields['driver'].queryset = Driver.objects.filter(company=company)
        else:
            self.fields['vehicle'].queryset = Vehicle.objects.none()
            self.fields['driver'].queryset = Driver.objects.none()
