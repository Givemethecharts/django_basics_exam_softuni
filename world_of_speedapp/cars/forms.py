from django import forms

from world_of_speedapp.cars.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {'image_url': forms.URLInput(attrs={'placeholder': 'https://...'})}


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CarDeleteForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.attrs['disabled'] = True
        self.fields['model'].widget.attrs['readonly'] = True
        self.fields['year'].widget.attrs['readonly'] = True
        self.fields['image_url'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
