from flask import Flask
from main import views, engine

app = Flask(__name__)

#import routes
from views import basic
from engine import engine
