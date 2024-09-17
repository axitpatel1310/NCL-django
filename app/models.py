from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    caption = models.ForeignKey("app.caption", null=True, blank=True, on_delete=models.CASCADE, related_name='captained_teams')
    description = RichTextField()
    budget = models.BigIntegerField(default=300000)
    
    def __str__(self):
        return self.team_name +' | '+ self.caption.user.username

class Player(models.Model):
    gameplay_choice = (
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All-Rounder', 'All-Rounder'),
    )
    name = models.CharField(max_length=50)
    description = RichTextField()
    sold = models.BooleanField(default=False)
    gameplay = models.CharField(max_length=50, default='Batsman', choices=gameplay_choice)
    img = models.URLField(max_length=200)
    from_class = models.CharField(max_length=50)
    team = models.ForeignKey("app.Team", on_delete=models.CASCADE, related_name='players', null=True, blank=True)
    def __str__(self):
        return self.name 
    
class caption(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)  # Link to Django User
    name = models.CharField(max_length=150)
    team = models.ForeignKey("app.Team", on_delete=models.CASCADE, null=True, blank=True,related_name='captioned_teams')
    def __str__(self):
        return self.user.username + ' | ' + self.name

class Sold(models.Model):
    player = models.ForeignKey("app.Player", on_delete=models.CASCADE, null=True, blank=True, related_name='sales')
    price = models.IntegerField()
    caption = models.ForeignKey("app.caption", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.caption} | {self.player} | {self.price}'
    def save(self, *args, **kwargs):
        if self.team and self.team.budget >= self.price:
            self.team.budget -= self.price
            self.team.save()
            self.player.team = self.team
            self.player.sold = True
            self.player.save()
        else:
            raise ValueError("Not enough budget to buy this player.")
        super(Sold, self).save(*args, **kwargs)  # Call the original save method
