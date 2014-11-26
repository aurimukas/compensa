# -*- coding: utf-8 -*-
from __future__ import absolute_import
from compensa import celery_app

from celery import shared_task

@celery_app.task
def get_car_data(car=None):
    car.pull_data_from_soap()
    print "Status: %s, Vehicle: %s" % (car.get_status(), car)

