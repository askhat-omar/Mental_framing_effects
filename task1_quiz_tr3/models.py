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
    name_in_url = 'task1_quiz_tr3'
    players_per_group = None
    num_rounds = 1
    terminal_probs = [0.125, 0.375, 0.375, 0.125]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer1 = models.IntegerField(
        choices=[
            [1, '150'],
            [2, '200'],
            [3, '250'],
            [4, '300']
        ],
        widget=widgets.RadioSelect
    )

    def answer1_error_message(self, value):
        if value != 4:
            return 'Wrong answer, try again.'

    answer2 = models.IntegerField(
        choices=[
            [1, '-75'],
            [2, '-50'],
            [3, '75'],
            [4, '50']
        ],
        widget=widgets.RadioSelect
    )

    def answer2_error_message(self, value):
        if value != 2:
            return 'Wrong answer, try again.'

    answer3 = models.IntegerField(
        choices=[
            [1, 'Y>100 and Z>100'],
            [2, 'Y>100 and Z<100'],
            [3, 'Y<100 and Z>100'],
            [4, 'Y<100 and Z<100']
        ],
        widget=widgets.RadioSelect
    )

    def answer3_error_message(self, value):
        if value != 2:
            return 'Wrong answer, try again.'

    answer4 = models.IntegerField(
        choices=[
            [1, 'The one at the top.'],
            [2, 'The one at the bottom.'],
            [3, 'A randomly selected one.'],
            [4, 'All of them.']
        ],
        widget=widgets.RadioSelect
    )

    def answer4_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'
