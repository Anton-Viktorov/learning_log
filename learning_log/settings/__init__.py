# -*- coding: utf-8 -*-

from .base import *

try:
    from .local import *
except ImportError:
    print("Can't find 'local' in settings. Make your file from local_template")
