from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import numpy
import json

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_portfolio_chp'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_chp = models.StringField(
        choices=['I prefer lottery A', 'I prefer lottery B', 'I prefer lottery C']
    )
