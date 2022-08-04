# Generated by Django 4.0.5 on 2022-08-04 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0003_user_userbookmarks_alter_recipes_recipe_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userbookmarks',
        ),
        migrations.AddField(
            model_name='user',
            name='userbookmarks',
            field=models.ManyToManyField(to='recipesite.recipes'),
        ),
    ]
