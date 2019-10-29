from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DefaultModel(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Criador",
    )

    class Meta:
        abstract = True

