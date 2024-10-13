from django.db import models

class Usuario(models.Model):
    NIVEL_USUARIO = [
        ( "Cliente" , "Cliente" ),
        ( "Administrador" , "Administrador" ),
     ]
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)

    nivel_usuario = models.CharField(max_length=15, choices=NIVEL_USUARIO, default="Cliente") # Adicionando o nível de conta

    def save(self, *args, **kwargs):
        if Usuario.objects.filter(nome=self.nome, email=self.email, senha=self.senha).exists():
            pass
        else:
            super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome
    

class Epis(models.Model):
    id_epi = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False, blank=False)
    quantidade = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
