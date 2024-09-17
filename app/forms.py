from django import forms
from .models import Sold, caption, Player,Team

class SoldForm(forms.ModelForm):
    player_name = forms.CharField(label='Player Name', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label='Select Team')
    price = forms.IntegerField(label='Price', min_value=0)

    class Meta:
        model = Sold
        fields = ['player_name', 'team', 'price']

    def __init__(self, *args, **kwargs):
        player = kwargs.pop('player', None)  # Get the player object passed when form is initialized
        super(SoldForm, self).__init__(*args, **kwargs)

        if player:
            self.fields['player_name'].initial = player.name
            self.player_instance = player  # Store player instance for use in save method
            self.fields['player_name'].widget.attrs['readonly'] = True

        # Optionally, filter teams based on their budget
        self.fields['team'].queryset = Team.objects.filter(budget__gte=0)

    def save(self, commit=True):
        instance = super(SoldForm, self).save(commit=False)
        instance.player = self.player_instance  # Associate the player with the sale

        if commit:
            instance.save()

        return instance

class PlayerIDSearchForm(forms.Form):
    player_id = forms.IntegerField(label="Enter Player ID", required=True)

class Loginform(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )