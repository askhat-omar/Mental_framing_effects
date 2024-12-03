from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy as np
import json


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'task2_results_tr2'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
