from django import forms
from .models import Fragmento

class FormularioFragmento(forms.ModelForm):
    class Meta:
        model = Fragmento
        fields = ('estratos','lenhosas','area_basal',
                  'altura_esp_dossel','med_ampli_diametros',
                  'dist_diametrica','cresc_dossel','vida_media',
                  'ampli_diametrica','ampli_altura','epifitas',
                  'lianas_herb','lianas_lenh','gramineas','regen_dossel')