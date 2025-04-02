from flask import Flask, Blueprint, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import firebase_admin
from firebase_admin import credentials, auth
import json
import os
import pyrebase


migrate = Migrate()

#認証csrfオブジェクトの作成
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('application.config')
    # 初期化
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    return app