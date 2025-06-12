from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_campeonato

class CampeonatoEquipos(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.anio} - {self.equipo} - {self.campeonato}"
