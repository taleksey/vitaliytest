"""
Get all settings from file setting
"""

from django.conf import settings

def global_settings(request):
    return {'settings':settings}