from django.db import models
from django.conf import settings
from applications.entrada.models import Entry
#apps de terceros
from model_utils.models import TimeStampedModel

from applications.favoritos.managers import FavoritesManager

class Favorites(TimeStampedModel):
    """modelo para favoritos"""
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )
    
    objects = FavoritesManager()

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada favorita'
        verbose_name_plural = 'Entradas favoritas'
        
    def __str__(self):
          return self.entry.title