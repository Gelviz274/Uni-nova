from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0003_alter_proyecto_colaboradores_alter_proyecto_creador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(on_delete=models.CASCADE, related_name='proyectos_creados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProyectoColaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.ForeignKey(on_delete=models.CASCADE, to='Proyectos.Proyecto')),
                ('usuario', models.ForeignKey(on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='colaboradores',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='colaboradores',
            field=models.ManyToManyField(related_name='proyectos_colaborados', through='Proyectos.ProyectoColaborador', to=settings.AUTH_USER_MODEL),
        ),
    ]
