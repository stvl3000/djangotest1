from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
import datetime
 
@python_2_unicode_compatible # since we need to support Python2.x
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    # ...
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
        
@python_2_unicode_compatible  # support Python 2
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
        
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    