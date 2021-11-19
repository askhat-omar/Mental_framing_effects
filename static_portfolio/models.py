from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy
import json


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_portfolio'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery = models.StringField(
        choices=['I prefer asset A', 'I prefer asset B', 'I prefer asset C', 'I prefer asset D (not to invest)']
    )
