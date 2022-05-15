from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'new_task2_quiz3'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer1 = models.IntegerField(
        choices=[
            [1, '0.125'],
            [2, '0.375'],
            [3, '0.625'],
            [4, '0.875']
        ],
        widget=widgets.RadioSelect
    )

    def answer1_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'



    answer2 = models.IntegerField(
        choices=[
            [1, '16.59'],
            [2, '23.70'],
            [3, '71.10'],
            [4, '192.00']
        ],
        widget=widgets.RadioSelect
    )

    def answer2_error_message(self, value):
        if value != 1:
            return 'Wrong answer, try again.'


    answer3 = models.IntegerField(
        choices=[
            [1, 'X<142.2 and Y>71.1'],
            [2, 'X<177.75 and Y>59.25'],
            [3, 'X<355.5 and Y>118.5'],
            [4, 'X<213.3 and Y>47.4']
        ],
        widget=widgets.RadioSelect
    )

    def answer3_error_message(self, value):
        if value != 2:
            return 'Wrong answer, try again.'


    answer4 = models.IntegerField(
        choices=[
            [1, '982.91'],
            [2, '396.00'],
            [3, '737.18'],
            [4, '385.18']
        ],
        widget=widgets.RadioSelect
    )

    def answer4_error_message(self, value):
        if value != 4:
            return 'Wrong answer, try again.'
