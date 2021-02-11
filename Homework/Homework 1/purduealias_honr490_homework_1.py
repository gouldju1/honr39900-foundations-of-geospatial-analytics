"""
Name: INSERT NAME
Date: INSERT DATE
"""

#Required Packages
import pandas as pd
import numpy as np
from pandasql import *

#Set up pandasql
pysqldf = lambda q: sqldf(q, globals())

#Load Datasets
meat = load_meat()
births = load_births()