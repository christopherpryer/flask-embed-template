import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import logging, sys


# logging configuration
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def get_hello_world():
    logging.info('Getting Hello World Div.')
    return html.Div('Hello World')

def Get_Review_Children():
    children = []
    children += [get_hello_world()]
    logging.info('Getting Children (type: {}, len: {}).' \
                 .format(type(children), len(children)))
    return children