# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from emprekis_soap.lib.objects import MotorInsurance
from com_local.models import Car
from datetime import datetime


class Command(BaseCommand):
    help = "Launches excel import task"

    def handle(self, *args, **options):
        motor = MotorInsurance()
        #data = motor.GetCarOwnerData(PersonalCode='300012660', VehicleNumber="GGC683")
        data = motor.GetCarOwnerData(PersonalCode='38312030379', VehicleNumber="FCZ633")
        ins_car = data.Data.Contract.Car

        if ins_car:
            #print ins_car
            car = Car()
            car.car_reg = motor.decrypt(ins_car.RegistrationNumber)
            car.production_year = ins_car.ProductionYear
            car.brand = ins_car.BrandName
            car.model = ins_car.ModelName
            car.vin = motor.decrypt(ins_car.VinNumber)
            car.capicity = ins_car.Capacity
            car.power = int(ins_car.Power)
            #car.weight = ins_car.Power
            car.seats = ins_car.SeatsCount
            car.type_id = ins_car.TypeId
            car.type = ins_car.Type
            car.first_registration_date = ins_car.FirstRegistrationDate
            car.price = float(ins_car.Price)

            car.save()


        self.stdout.write('Finished excel import žiedų valdovas čia'.decode('utf-8'))