# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Farmer(models.Model):
    uid = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sec = models.CharField(max_length=1, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    village = models.CharField(max_length=30, blank=True, null=True)
    glocation = models.CharField(max_length=100, blank=True, null=True)
    profilelink1 = models.CharField(max_length=100, blank=True, null=True)
    profiilelink2 = models.CharField(max_length=100, blank=True, null=True)
    landref = models.CharField(max_length=100, blank=True, null=True)
    markref = models.CharField(max_length=30, blank=True, null=True)
    farmerid = models.CharField(max_length=30, blank=True, null=True)
    lastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer'


class Identity(models.Model):
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    lastlogin = models.DateField(blank=True, null=True)
    idattr1 = models.CharField(db_column='idAttr1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idattr2 = models.CharField(db_column='idAttr2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idattr3 = models.CharField(db_column='idAttr3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identity'


class Landinfo(models.Model):
    farmerid = models.CharField(max_length=30, blank=True, null=True)
    soiltype = models.CharField(max_length=20, blank=True, null=True)
    watersource = models.CharField(max_length=20, blank=True, null=True)
    landsize = models.FloatField(blank=True, null=True)
    sizetype = models.CharField(max_length=10, blank=True, null=True)
    cattletype = models.CharField(max_length=10, blank=True, null=True)
    cattlenumber = models.IntegerField(blank=True, null=True)
    cattlebreed = models.CharField(max_length=20, blank=True, null=True)
    corpinfo1 = models.CharField(max_length=50, blank=True, null=True)
    cropinfo2 = models.CharField(max_length=50, blank=True, null=True)
    cropinfo3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'landinfo'


class Markinfo(models.Model):
    farmerid = models.CharField(max_length=30, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    trend = models.IntegerField(blank=True, null=True)
    market = models.CharField(max_length=30, blank=True, null=True)
    minfo1 = models.CharField(max_length=30, blank=True, null=True)
    minfo3 = models.CharField(max_length=30, blank=True, null=True)
    minfo2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markinfo'
