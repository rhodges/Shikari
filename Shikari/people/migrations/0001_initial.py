# Generated by Django 2.0 on 2018-01-15 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Primary Contact')),
                ('display_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.TextField(verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_home', models.BooleanField(default=False, verbose_name='Home Organization')),
                ('name', models.TextField(verbose_name='Org. Name')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(max_length=254, verbose_name='URL')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, default=None, null=True, verbose_name='First Name')),
                ('last_name', models.TextField(verbose_name='Last Name')),
                ('middle_name', models.TextField(blank=True, default=None, null=True, verbose_name='Middle Name')),
                ('name_prefix', models.TextField(blank=True, default=None, null=True, verbose_name='Name Prefix')),
                ('name_suffix', models.TextField(blank=True, default=None, null=True, verbose_name='Name Suffix')),
                ('job_title', models.TextField(blank=True, default=None, null=True, verbose_name='Job Title')),
                ('job_class', models.TextField(blank=True, default=None, null=True, verbose_name='Job Class')),
                ('notes', models.TextField(blank=True, default=None, null=True, verbose_name='Additional Notes')),
                ('manager', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Person', verbose_name='Reports To')),
                ('organization', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Organization')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.TextField(verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_type', models.TextField(verbose_name='Site Type')),
                ('display_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('contactmethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.ContactMethod')),
                ('email', models.TextField(blank=True, default=None, null=True, verbose_name='Email Address')),
                ('contact_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.EmailContactType')),
            ],
            bases=('people.contactmethod',),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('contactmethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.ContactMethod')),
                ('number', models.TextField(blank=True, default=None, null=True, verbose_name='Phone Number')),
                ('contact_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.PhoneContactType')),
            ],
            bases=('people.contactmethod',),
        ),
        migrations.AddField(
            model_name='organizationwebsite',
            name='site_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.WebsiteType'),
        ),
        migrations.AddField(
            model_name='contactmethod',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
    ]
