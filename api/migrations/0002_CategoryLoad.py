from django.db import migrations, models
import django.db.models.deletion

def load_categories(apps, schema_editor):
    Category = apps.get_model("api", "Category")
    cat = Category(NAME='Politics and Society',COLOR='#7bed9f')
    cat.save()
    cat = Category(NAME='Health and Medicine',COLOR='#158215')
    cat.save()
    cat = Category(NAME='Sports and Entertainment',COLOR='#ddd267')
    cat.save()
    cat = Category(NAME='Education',COLOR='#a367dc')
    cat.save()
    cat = Category(NAME='Sex and Gender',COLOR='#1c58b8')
    cat.save()
    cat = Category(NAME='Religion and Ethics',COLOR='#ff6b81')
    cat.save()
    cat = Category(NAME='International Conflicts',COLOR='#76c9f5')
    cat.save()
    cat = Category(NAME='Elections',COLOR='#e83535')
    cat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=60)),
                ('COLOR', models.CharField(max_length=60)),
            ],
        ),
        migrations.RunPython(load_categories),
        migrations.AddField(
            model_name='debate',
            name='CATEGORY_ID',
            field=models.ForeignKey(default=1, null=False, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]
