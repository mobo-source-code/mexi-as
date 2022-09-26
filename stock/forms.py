from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Article, Feeding, Fournisseur, Taking

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ('br', 'fournisseur')
    
class AddFourniForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('ref','single_value')

class TakingForm(ModelForm):
    class Meta:
        model = Taking
        exclude = ('ref', 'user', 'made_on', 'total_value')
    

    
