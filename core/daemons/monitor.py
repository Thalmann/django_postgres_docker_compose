#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
if sys.stdout.encoding is None:
    reload(sys)
    sys.setdefaultencoding('UTF-8')
sys.path += ["."]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
import django
django.setup()

import subprocess
from time import sleep

from core.models import Check, Monitor

while True:
        res = subprocess.call(['ping', '-c', '3', address])
    for monitor in Monitor.objects.all():
        if res == 0:
            Check.objects.create(monitor=monitor, up=True)
        else:
            Check.objects.create(monitor=monitor, up=False)
    sleep(5)
