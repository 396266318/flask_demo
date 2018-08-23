# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/8/20 18:00
"""
from flask import Blueprint

bp = Blueprint('errors', '__name__')

from app.errors import handlers