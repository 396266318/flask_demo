# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/8/20 18:05
"""
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
