#!/usr/bin/env python
import os
import sys
from sbomb.settings.utils import get_env_variable

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_env_variable("SBOMB_SETTINGS_MODULE"))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
