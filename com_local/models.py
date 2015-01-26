from __future__ import absolute_import

import string
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

import re

from suds import WebFault

from emprekis_soap.lib.objects import MotorInsurance

SEPARATOR = re.compile(r'[,;\r\n]+')

class Request(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), blank=True)
    code = models.CharField(verbose_name=_('Code'), max_length=32, default=None)
    requested_reg_numbers = TaggableManager(verbose_name=_('Car Reg. Number'), help_text=_("A comma-separated list of reg. numbers."))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'), default=timezone.now())
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'), default=timezone.now())

    def __unicode__(self):
        return unicode(_("User: %s, Requested for code: %s" % (self.user, self.code)))



    def get_absolute_url(self):
        """
            return and absolute url to object
        """
        return reverse('com_local:request_cars', kwargs={ 'pk': self.id })

    @property
    def absolute_url(self):
        return self.get_absolute_url()

    def get_requested_cars(self):
        reg_numbers = self.requested_reg_numbers.all()
        motor = MotorInsurance()
        if len(reg_numbers) and self.code:
            #print reg_numbers
            for nr in reg_numbers:
                new_car = Car()
                new_car.car_reg = nr

                data = motor.GetCarOwnerData(PersonalCode=self.code, VehicleNumber=str(nr))
                car = data.Data.Contract.Car
                if car:
                    new_car.car_reg = motor.decrypt(car.RegistrationNumber)
                    new_car.production_year = car.ProductionYear
                    new_car.brand = car.BrandName
                    new_car.model = car.ModelName
                    new_car.vin = motor.decrypt(car.VinNumber)
                    new_car.capicity = car.Capacity
                    new_car.power = int(car.Power)
                    #new_car.weight = ins_car.Power
                    new_car.seats = car.SeatsCount
                    new_car.type_id = car.TypeId
                    new_car.type = car.Type
                    new_car.first_registration_date = car.FirstRegistrationDate
                    new_car.price = float(car.Price)
                self.car_set.add(new_car)


class Car(models.Model):
    STATUS_STARTED = 1
    STATUS_SUCCESS = 2
    STATUS_ERROR = 3
    STATUSES = {
        STATUS_STARTED: _(u'Started to synchronize'),
        STATUS_SUCCESS: _(u'Successfully synchronized'),
        STATUS_ERROR: _(u'Error in synchronization'),
    }

    STATUS_CHOICES = lambda data: list((key, unicode(data[key])) for key in data.keys())

    def create_choices_list(data={}):
        return list((key, unicode(data[key])) for key in data.keys())

    request = models.ForeignKey(Request)
    brand = models.CharField(verbose_name=_('Brand'), max_length=256, default='', blank=True, null=True)
    model = models.CharField(verbose_name=_('Model'), max_length=256, default='', null=True, blank=True)
    car_reg = models.CharField(verbose_name=_('Car reg. number'), max_length=16, default=None, null=True, blank=True)
    vin = models.CharField(verbose_name=_('VIN number'), max_length=32, default=None, null=True, blank=True)
    production_year = models.SmallIntegerField(verbose_name=_('Construction year'), max_length=8, default=None, null=True, blank=True)
    first_registration_date = models.DateTimeField(verbose_name=_('First Registration'), default=None, null=True, blank=True)
    capicity = models.IntegerField(verbose_name=_('cm3'), max_length=8, default=None, null=True, blank=True)
    power = models.IntegerField(verbose_name=_('KW'), max_length=8, default=None, null=True, blank=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    type = models.CharField(verbose_name=_('Vehicle Category Name'), max_length=16, default='', blank=True, null=True)
    type_id = models.CharField(verbose_name=_('Vehicle Category id'), max_length=32, default='', blank=True, null=True)
    weight = models.DecimalField(verbose_name=_('Weight'), max_digits=8, decimal_places=3, default=None, null=True, blank=True)
    seats = models.SmallIntegerField(verbose_name=_('Seats'), max_length=4, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'), default=timezone.now())
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'), default=timezone.now())
    status = models.SmallIntegerField(
        verbose_name=_('Status'),
        max_length=4,
        default=STATUS_STARTED,
        blank=True,
        null=False,
        choices=STATUS_CHOICES(STATUSES)
    )

    def __unicode__(self):
        return unicode(_(u"Brand: {0}, Model: {1}, Reg. Number: {2}".format(self.brand, self.model, self.car_reg)))

    def __iter__(self):
        for f_name in self._meta.get_all_field_names():
            try:
                val = getattr(self, f_name)
            except:
                val = None
            yield (f_name, val)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def get_status_choices(self):
        return self.STATUS_CHOICES(self.STATUSES)

    def get_status(self):
        return unicode(self.STATUSES[self.status])

    def pull_data_from_soap(self):
        motor = MotorInsurance()
        car = None
        try:
            data = motor.GetCarOwnerData(PersonalCode=self.request.code, VehicleNumber=self.car_reg)
            #print data
            if 'ErrorMessage' in data:
                print "Error in SOAP request,", data.ErrorMessage
                self.status = self.STATUS_ERROR
            else:
                car = data.Data.Contract.Car

        except WebFault as w:
            print "Error in fetching data", w
            self.status = self.STATUS_ERROR
        #car = data.Data.Contract.Car

        if car:
            self.car_reg = motor.decrypt(car.RegistrationNumber)
            self.production_year = car.ProductionYear
            self.brand = car.BrandName
            self.model = car.ModelName
            self.vin = motor.decrypt(car.VinNumber)
            self.capicity = car.Capacity
            self.power = int(car.Power)
            #car.weight = ins_car.Power
            self.seats = car.SeatsCount
            self.type_id = car.TypeId
            self.type = car.Type
            self.first_registration_date = car.FirstRegistrationDate
            self.price = float(car.Price)

            self.status = self.STATUS_SUCCESS

        self.save()
