from django.db import models

class State(models.TextChoices):
    enabled = 'enabled'
    disabled = 'disabled'


class FeatureToggle(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=200)
    state = models.CharField(choices=State.choices, max_length=20)
    # when extendending function we can use below fields
    
    # user = models.ForeignKey(User)
    # created_at = models.DateTimeField(auto_now_add=True)
    # last_modified_at = models.DateTimeField(audo_now=True)
    # note = models.TextField()
    # env = models.CharField(max_length=20)
    # app = models.CharField(max_length=50)

    
    def toggle_state(self):
        self.state = State.disabled if self.state == State.enabled else State.enabled
        self.save()