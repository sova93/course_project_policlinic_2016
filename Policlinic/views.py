# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from  django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import *
from django.core.exceptions import *
from Policlinic.forms import *
from numpy import *
from Policlinic.models import *

@csrf_exempt
def index(request):
    return render_to_response('index.html')

def contacts(request):
    return render_to_response('contacts.html')

def view_clients(request):
    model = TClient.objects.all()
    return render(request,'view_client.html',{'listClients':model})

def view_doctors(request):
    model = TDoctor.objects.all()
    return render(request,'view_doctor.html',{'listDoctor':model})

def view_disease(request):
    model = TDocorVisit.objects.all()
    return render(request, 'view_visits.html',{'listVisit':model})

@csrf_exempt
def search_client_id(request):
    attr = "/search_client_id/"
    tab_name = "Поиск пациента по ID"
    try:
        err = ""
        form = SearchNumForm(request.POST or None)
        if form.is_valid():
            model = TClient.objects.get(id_t_client =request.POST['id'])
            address_res = model.address_residence.city.name + ' ' + model.address_residence.area.name + ' '+ model.address_residence.district.name + ' ' + model.address_residence.street.name + ' ' + str(model.address_residence.house) + ' ' + str(model.address_residence.flat)
            address_reg = model.address_registration.city.name + ' ' + model.address_registration.area.name +' ' + model.address_registration.district.name + ' ' + model.address_registration.street.name + ' ' + str(model.address_registration.house) + ' ' + str(model.address_registration.flat)
            if model.reason == None: reason = ''
            else:reason = model.reason.reason
            if model.feature == None: name_f = ''
            else: name_f = model.feature.name
            data = {'id':model.id_t_client,'surname':model.surname,
                  'name':model.name, 'patronymic':model.patronymic,'sex':model.sex,
                  'birthday':model.birthday,'address_residence':address_res,
                  'address_registration':address_reg, 'service':model.service.type,
                  'n_passport':model.n_passport,'phone_h':model.h_number,
                  'phone_m':model.m_number, 'n_plot':model.n_plot_full_id,
                  'date_start':model.date_start,'date_end':model.date_end,
                  'reason':reason, 'feature':name_f
                   }
            form1 = ClientForm(data)
            attr = "http://127.0.0.1:8000/"
            return render(request, 'forms_page.html',{'form': form1,'attr':attr,'tab_name':tab_name,'err':err,'n_size':'2','align':'left'})
    except Error:
       err = "Ошибка интергации с БД: проверьте данные!"
    except ObjectDoesNotExist: err = "Ошибка интергации с БД: объект не найден!"
    return render(request, 'forms_page.html',{'form':form,'attr':attr,'tab_name':tab_name,'err':err,'n_size':'1','align':'center'})

@csrf_exempt
def search_client_surename(request):
    attr = "/search_client_surename/"
    tab_name = "Поиск пациента по фамилии"
    try:
        err = ""
        form = SearchSurnameForm(request.POST or None)
        if form.is_valid():
            model = TClient.objects.filter(surname=request.POST['surname'])
            return render(request,'view_client.html',{'listClients':model})
    except Error:
       err = "Ошибка интергации с БД: проверьте данные!"
    except ObjectDoesNotExist: err="Ошибка интергации с БД: объект не найден!"
    return render(request, 'forms_page.html',{'form':form,'attr':attr,'tab_name':tab_name,'err':err,'n_size':'1','align':'center'})

@csrf_exempt
def search_plot_client(request):
    attr = "/search_plot_client/"
    tab_name = "Пациенты на участке"
    try:
        err = ""
        form = SearchNumForm(request.POST or None)
        if form.is_valid():
            model = TClient.objects.filter(n_plot_full=request.POST['id'])
            return render(request,'view_client.html',{'listClients':model})
    except Error:
       err = "Ошибка интергации с БД: проверьте данные!"
    except ObjectDoesNotExist: err = "Ошибка интергации с БД: объект не найден!"
    return render(request, 'forms_page.html',{'form':form,'attr':attr,'tab_name':tab_name,'err':err,'n_size':'1','align':'center'})

@csrf_exempt
def search_doctor_spec(request):
    attr = "/search_doctor_spec/"
    tab_name = "Врачи по специализации"
    try:
        err = ""
        form = SearchSpecForm(request.POST or None)
        if form.is_valid():
            spec = TSpeciality.objects.get(name =request.POST['specialization'])
            model = TDoctor.objects.filter(speciality =spec,date_end =None)
            return render(request,'view_doctor.html',{'listDoctor':model})
    except Error:
       err = "Ошибка интергации с БД: проверьте данные!"
    except ObjectDoesNotExist: err = "Ошибка интергации с БД: объект не найден!"
    return render(request, 'forms_page.html',{'form':form,'attr':attr,'tab_name':tab_name,'err':err,'n_size':'1','align':'center'})

def statistics_view(request):
    tab_name = 'Статистика участков'
    return render(request,'statistics.html',{'tab_name':tab_name,'plot1':TClient.objects.filter(n_plot_full=1).count(),
                                             'plot2':TClient.objects.filter(n_plot_full=2).count(),
                                             'plot3':TClient.objects.filter(n_plot_full=3).count(),
                                             'plot4':TClient.objects.filter(n_plot_full=4).count()})

def statistics_group_view(request):
    tab_name = 'Статистика участков'
    group = TDiseaseGroup.objects.order_by('id_t_disease_group')
    list_group = []
    list_count = []
    list_num = []
    for i in group: list_group.append(i.group)
    for j in list_group:
        group=TDiseaseGroup.objects.get(group=j)
        desease=TDisease.objects.filter(group =group)
        list_count.append(TVisitList.objects.filter(disease__in=desease).count())
    print(list_group)
    for a in range(len(list_group)): list_num.append(a)
    print(list_count)
    return render(request,'statistics_group.html',{'tab_name':tab_name,'group':list_group,
                                                   'list_count':list_count,'count':len(list_group),'list_num':list_num})