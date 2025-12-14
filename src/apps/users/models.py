from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import phonenumber_field.modelfields as phone_number_fields



class CustomUser(AbstractUser):
    """
    Modèle utilisateur personnalisé étendant AbstractUser de Django.
    Ajoute des champs supplémentaires tels que le numéro de téléphone et la date de naissance.
    phone_number: Champ pour stocker le numéro de téléphone au format international.
    email: Champ pour stocker l'adresse e-mail de l'utilisateur.
    date_of_birth: Champ pour stocker la date de naissance de l'utilisateur.

    Méta:
        verbose_name: Nom lisible pour le modèle dans l'interface d'administration.
        verbose_name_plural: Nom pluriel lisible pour le modèle dans l'interface d'administration.
    Méthodes:
        __str__: Retourne une représentation lisible de l'utilisateur, incluant le nom complet ou le nom d'utilisateur et le numéro de téléphone ou l'e-mail.
    """

    phone_number = phone_number_fields.PhoneNumberField(
        unique=True,
        null=True,
        blank=True,
        help_text="Numéro de téléphone au format international. +2250107050000",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Adresse e-mail",
        help_text="Adresse e-mail de l'utilisateur.",
        )
    
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de naissance",
        help_text="Date de naissance de l'utilisateur.",
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        if self.phone_number:
            return f"{self.get_full_name() or self.get_username()} - {self.phone_number}"
        return f"{self.get_full_name() or self.get_username()} - {self.email}"