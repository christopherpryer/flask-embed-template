"""Review & Analysis Logic"""
from .callbacks.review import Initialize_Review_Callbacks
from .children.review import Get_Review_Children
import pandas as pd
import numpy as np

class Service:
    def __init__(self, service_type: str):
        self.service_type = service_type.upper()

    def init_callbacks(self, dash_app):
        return {
            'REVIEW': Initialize_Review_Callbacks
        }[self.service_type](dash_app)

    def get_dash_children(self):
        return {
            'REVIEW': Get_Review_Children
        }[self.service_type]()

