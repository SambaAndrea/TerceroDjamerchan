from django.db import models

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    class Meta: db_table = 'usuario'


class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ci = models.IntegerField(10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono= models.IntegerField(10)
    email = models.EmailField(max_length=100)


    class Meta: db_table = 'clientes'


class manicure(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=60)
    detalle = models.CharField(max_length=100)

    class Meta: db_table = 'manicure'


class peicure(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario =models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha = models.CharField(max_length=60)
    detalle = models.CharField(max_length=100)


    class Meta: db_table = 'pedicure'