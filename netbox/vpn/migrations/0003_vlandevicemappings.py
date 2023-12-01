# Generated by Django 4.2.4 on 2023-11-30 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('vpn', '0002_move_l2vpn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='l2vpntermination',
            name='assigned_object_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(models.Q(('app_label', 'dcim'), ('model', 'interface')), models.Q(('app_label', 'ipam'), ('model', 'vlan')), models.Q(('app_label', 'virtualization'), ('model', 'vminterface')), models.Q(('app_label', 'ipam'), ('model', 'vlandevicemapping')), _connector='OR')), on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.contenttype'),
        ),
    ]