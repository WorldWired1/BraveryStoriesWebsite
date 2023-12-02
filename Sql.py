import sqlalchemy
from flask import *
import pandas as pd
import numpy as np

@app.route('/getDbTable')
def getDbTable():
    engine = sqlalchemy.create_engine()