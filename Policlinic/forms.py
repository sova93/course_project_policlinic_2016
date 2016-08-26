# -*- coding: utf-8 -*-
__author__ = 'S_o_va'
from django import forms

error_messages = {'required':'Поле должно быть заполнено!',
                'invalid':'Неверный формат!',
                'max_length':'Слишком длинный текст',
                'min_length':'Слишком короткий текст'}

class SearchNumForm(forms.Form):
    id = forms.CharField(label=u'ID ',widget=forms.NumberInput,max_length=40,error_messages=error_messages)

class SearchSurnameForm(forms.Form):
    surname = forms.CharField(label=u'Фамилия ',widget=forms.TextInput(attrs={'pattern':'^[-a-z,A-Z,А-Я,а-я,ё,Ё]+$'}),max_length=60,error_messages=error_messages)

class SearchSpecForm(forms.Form):
    specialization = forms.CharField(label=u'Название специализации ',max_length=255,error_messages=error_messages)

class ClientForm(forms.Form):
    SEX = (('м','м',),('ж','ж',),)
    id = forms.CharField(label=u'ID ',widget=forms.NumberInput,max_length=40,error_messages=error_messages)
    surname = forms.CharField(label=u'Фамилия ',widget=forms.TextInput(attrs={'pattern':'^[-a-z,A-Z,А-Я,а-я,ё,Ё]+$'}),max_length=45,error_messages=error_messages)
    name = forms.CharField(label=u'Имя ',max_length=45,error_messages=error_messages,widget=forms.TextInput(attrs={'pattern':'^[-a-z,A-Z,А-Я,а-я,ё,Ё]+$'}))
    patronymic = forms.CharField(label=u'Отчество ',max_length=45,error_messages=error_messages,required= False,widget=forms.TextInput(attrs={'pattern':'^[-a-z,A-Z,А-Я,а-я,ё,Ё]+$'}))
    sex = forms.ChoiceField(label=u'Пол ',widget=forms.Select, choices=SEX,error_messages=error_messages)
    birthday = forms.DateField(label=u'Дата рождения ',widget=forms.DateInput(format="%Y-%m-%d"),error_messages=error_messages)
    address_residence = forms.CharField(label=u'Адрес проживания ',max_length=300,error_messages=error_messages)
    address_registration = forms.CharField(label=u'Адрес прописки ',max_length=300,error_messages=error_messages)
    service = forms.CharField(label=u'Тип обслуживания ',max_length=300,error_messages=error_messages)
    n_passport = forms.CharField(label=u'Серия и номер паспорта ',max_length=9,required= False,error_messages=error_messages)
    phone_h = forms.CharField(label=u'Дом.тел. ',widget=forms.TextInput(attrs={'pattern':'[+][0-9]{12}'}),max_length=13, required= False,error_messages=error_messages)
    phone_m = forms.CharField(label=u'Моб.тел. ',widget=forms.TextInput(attrs={'pattern':'[+][0-9]{12}'}),max_length=13, required= False,error_messages=error_messages)
    n_plot = forms.CharField(label=u'Номер участка ',max_length=3,error_messages=error_messages)
    date_start = forms.DateField(label=u'Дата поступления в поликлинику ',widget=forms.DateInput(format="%Y-%m-%d"),error_messages=error_messages)
    date_end = forms.DateField(label=u'Дата выбытия из поликлиники ',widget=forms.DateInput(format="%Y-%m-%d"),required= False,error_messages=error_messages)
    reason = forms.CharField(label=u'Причина выбытия ',max_length=255,required= False,error_messages=error_messages)
    feature = forms.CharField(label=u'Примечания ',max_length=255,required= False,error_messages=error_messages)
