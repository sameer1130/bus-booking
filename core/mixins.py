from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractTrack(models.Model):

    uuid = models.UUIDField(
        _("UUID"),
        default=uuid4,
        editable=False,
        unique=True,
        primary_key=True,
    )
    created_at = models.DateTimeField(_("created_at"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"),auto_now=True)

    class Meta:
        abstract = True
    
