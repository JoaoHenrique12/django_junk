from django.db import models
from django.contrib.auth.models import User

# Types

profile_connectivity = [
        ('U', 'Undefined'),
        ('B', 'Block'),
        ('F', 'Friend Request'),
        ('C', 'Cancel Friend Request '),
        ('R', 'Refuse Friend Request')]

profile_type = [
        ('+', 'Publico'),
        ('-', 'Privado')]
 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, models.RESTRICT, primary_key=True)

    profile_type = models.CharField(max_length=1, verbose_name='Tipo de perfil', choices=profile_type, default='+')

    like_read = models.BooleanField(verbose_name='Gosta de ler', default=False)
    birth = models.DateField(verbose_name='Data de nascimento', null=True, blank=False)


    def __str__(self):
        return self.user.username

class ProfileConnectProfile(models.Model):
    sender_id = models.ForeignKey(Profile,related_name='sent_connections', on_delete=models.RESTRICT)
    receiver_id = models.ForeignKey(Profile,related_name='received_connections', on_delete=models.RESTRICT)

    sender_status = models.CharField(max_length=1, choices=profile_connectivity, default='U')
    receiver_status = models.CharField(max_length=1, choices=profile_connectivity, default='U')

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=["sender_id", "receiver_id"], name="profile_connect_profile_pk"),
                models.UniqueConstraint(fields=["receiver_id", "sender_id"], name="reverse_profile_connect_profile_pk")
            ]

