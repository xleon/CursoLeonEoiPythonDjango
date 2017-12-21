from django.db import models

TOURNAMENT_CATEGORIES = (
    (0, 'Pluma'),
    (1, 'Medio'),
    (2, 'Pesado'),
)


class Fighter(models.Model):
    alias = models.CharField(max_length=15, primary_key=True)
    avatar = models.ImageField(upload_to='avatars')
    force = models.PositiveIntegerField('Fuerza', default=4)
    skill = models.PositiveIntegerField('Habilidad', default=3)
    resistance = models.PositiveIntegerField('Resistencia', default=3)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Luchador'
        verbose_name_plural = 'Luchadores'


class Tournament(models.Model):
    name = models.CharField('Nombre', max_length=150)
    start_date = models.DateTimeField('Hora de inicio')
    finish_date = models.DateTimeField('Hora final')
    fighter_count = models.PositiveIntegerField('Nº luchadores')
    category = models.IntegerField('Categoría', choices=TOURNAMENT_CATEGORIES, default=1)
    fighters = models.ManyToManyField(Fighter, verbose_name='Luchadores')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo'
        verbose_name_plural = 'Torneos'


class Combat(models.Model):
    date = models.DateTimeField('Fecha/hora', auto_now=True)
    fighter1 = models.ForeignKey(Fighter, verbose_name='Luchador 1', related_name='figher1', on_delete=models.CASCADE)
    fighter2 = models.ForeignKey(Fighter, verbose_name='Luchador 2', related_name='fither2', on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, verbose_name='Torneo', on_delete=models.CASCADE)

    def __str__(self):
        return '{} vs {}'.format(self.fighter1.alias, self.fighter2.alias)

    class Meta:
        verbose_name = 'Combate'
        verbose_name_plural = 'Combates'
