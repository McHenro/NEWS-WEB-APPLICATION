from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    by = models.CharField(_('Author'), max_length=100)
    score = models.IntegerField(_('Score'), default=0)
    title = models.CharField(_('Title'), max_length=255, unique=True)
    type = models.CharField(_('Type'), max_length=50)
    url = models.URLField(_('Url'), unique=True)
    text = models.TextField(_('Text'))
    
    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
    
    def __str__(self):
        self.title
    
    
