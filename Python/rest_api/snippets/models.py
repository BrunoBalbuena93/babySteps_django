from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

"""
Aquí tenemos el modelo Snippet, que es tal cual con lo que se trabajará para obtener información
Se hace una liga con los usuarios nativos de django.

Override (1): Dado que metemos el formato de html, se debe hacer el override para integrarlo al método
"""


class Snippet(models.Model):
    # Propietario
    owner = models.ForeignKey('auth.User', related_name="snippets", on_delete=models.CASCADE)
    # Campo "creado" de llenado automático
    created = models.DateTimeField(auto_now_add=True)
    # Campo "titulo"
    title = models.CharField(max_length=100, blank=True, default="")
    # Campo "code"
    code = models.TextField()
    # 
    linenos = models.BooleanField(default=False)
    # 
    highlighted = models.TextField()
    # Lenguaje
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=100)
    # Estilo
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    
    class Meta:
        ordering = ["created"]
    
    # Override (1)
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos = linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)