# -*- coding: utf-8 -*-
from __future__ import absolute_import
from compensa import celery_app
from .models import Car

from celery import shared_task

@celery_app.task
def get_car_data(carId=None):
    if carId:
        car = Car.objects.get(id=carId)
        if car:
            print('Requesting info for a car:', car)
            car.pull_data_from_soap()
            print("Status: %s, Vehicle: %s" % (car.get_status(), car))
        else:
            print("Car wasn't found. CarId:", carId)
    else:
        print("No CarId was passed")