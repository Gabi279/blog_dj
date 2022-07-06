from django.db import models
# apps terceros
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """modelo para datos de la pantalla home"""
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Título nosotros', max_length=50)
    about_text = models.TextField()
    contact_mail = models.EmailField(
        'Email de contacto', 
        max_length=254,
        blank=True,
        null=True
        )
    phone = models.CharField('Teléfono contacto', max_length=20)

    class Meta:
        verbose_name = 'Página principal'
        verbose_name_plural = 'Página principal'
        
    def __str__(self):
          return self.title
    
class Suscribers(TimeStampedModel):
    """suscriptores"""
    
    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
        
    def __str__(self):
          return self.email
      
class Contact(TimeStampedModel):
    """formulario de contacto"""

    
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
          return self.full_name