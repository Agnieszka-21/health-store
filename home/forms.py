from django import forms
from .models import Carousel


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CarouselForm, self).__init__(*args, **kwargs)
        self.fields['banner_img1'].required = True
        self.fields['banner_img2'].required = True
        self.fields['banner_img3'].required = True
        self.fields['banner_img4'].required = True
