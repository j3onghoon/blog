"""
모든 pyinfra inventory에서 공통적으로 사용하는 변수들을 정의한다.
"""
import os
from dataclasses import asdict, dataclass

from django.utils.functional import SimpleLazyObject
from pyinfra.connectors.ssh import DATA_KEYS


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


data = AttrDict()
data.ssh_user = 'ubuntu'
data.ssh_key = '/Users/parkjeonghoon/Downloads/j3onghoon.pem'

for k, v in data.items():
    globals()[k] = v
