# -*- coding: utf-8 -*-
from __future__ import absolute_import

import djcelery
djcelery.setup_loader()

BROKER_URL = "amqp://guest:guest@localhost:5672//"