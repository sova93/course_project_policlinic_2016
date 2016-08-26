from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class TAddres(models.Model):
    id_t_address = models.IntegerField(primary_key=True)
    city = models.ForeignKey('TCities')
    area = models.ForeignKey('TArea')
    district = models.ForeignKey('TDistrict')
    street = models.ForeignKey('TStreets')
    house = models.IntegerField()
    flat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_addres'


class TArea(models.Model):
    id_t_area = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 't_area'


class TCities(models.Model):
    id_t_cities = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 't_cities'


class TClient(models.Model):
    id_t_client = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=1)
    birthday = models.DateField()
    address_residence = models.ForeignKey(TAddres, db_column='address_residence',related_name='residence')
    address_registration = models.ForeignKey(TAddres, db_column='address_registration',related_name='registration')
    service = models.ForeignKey('TService', db_column='service')
    n_passport = models.CharField(max_length=9, blank=True)
    h_number = models.CharField(max_length=13, blank=True)
    m_number = models.CharField(max_length=13, blank=True)
    n_plot_full = models.ForeignKey('TPlotFull', db_column='n_plot_full')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    reason = models.ForeignKey('TReasons', db_column='reason', blank=True, null=True)
    feature = models.ForeignKey('TFeature', db_column='feature', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_client'


class TDepartament(models.Model):
    id_t_departament = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_departament'


class TDisease(models.Model):
    id_t_disease = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    group = models.ForeignKey('TDiseaseGroup', db_column='group')

    class Meta:
        managed = False
        db_table = 't_disease'


class TDiseaseGroup(models.Model):
    id_t_disease_group = models.IntegerField(primary_key=True)
    group = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_disease_group'


class TDistrict(models.Model):
    id_t_district = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 't_district'


class TDocorVisit(models.Model):
    id_t_docor_visit = models.IntegerField(primary_key=True)
    docor = models.ForeignKey('TDoctor')
    visit = models.ForeignKey('TVisitList', unique=True)

    class Meta:
        managed = False
        db_table = 't_docor_visit'


class TDoctor(models.Model):
    id_t_doctor = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    speciality = models.ForeignKey('TSpeciality')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    plot = models.ForeignKey('TPlotFull', blank=True, null=True)
    cabinet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_doctor'


class TFeature(models.Model):
    id_t_feature = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_feature'


class TPlaceService(models.Model):
    id_t_place_service = models.IntegerField(primary_key=True)
    place = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_place_service'


class TPlot(models.Model):
    id_t_plot = models.IntegerField(primary_key=True)
    id_city = models.ForeignKey(TCities, db_column='id_city')
    id_area = models.ForeignKey(TArea, db_column='id_area')
    id_district = models.ForeignKey(TDistrict, db_column='id_district')
    id_street = models.ForeignKey('TStreets', db_column='id_street')
    house = models.IntegerField()
    plot = models.ForeignKey('TPlotFull', db_column='plot')

    class Meta:
        managed = False
        db_table = 't_plot'


class TPlotFull(models.Model):
    id_t_plot_full = models.IntegerField(primary_key=True)
    plot = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 't_plot_full'


class TPurpose(models.Model):
    id_t_purpose = models.IntegerField(primary_key=True)
    purpose = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_purpose'


class TReasons(models.Model):
    id_t_reasons = models.IntegerField(primary_key=True)
    reason = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_reasons'


class TService(models.Model):
    id_t_service = models.IntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 't_service'


class TSpeciality(models.Model):
    id_t_speciality = models.IntegerField(primary_key=True)
    departament = models.ForeignKey(TDepartament, db_column='departament')
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_speciality'


class TStreets(models.Model):
    id_t_streets = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 't_streets'


class TVisitList(models.Model):
    id_t_visit_list = models.IntegerField(primary_key=True)
    client = models.ForeignKey(TClient)
    date = models.DateField()
    plot = models.ForeignKey(TPlotFull, blank=True, null=True)
    place = models.ForeignKey(TPlaceService)
    purpose = models.ForeignKey(TPurpose)
    disease = models.ForeignKey(TDisease)
    form = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_visit_list'