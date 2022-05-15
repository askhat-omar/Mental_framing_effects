from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'new_task2_quiz'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer2 = models.IntegerField(
        choices=[
            [1, '0.125'],
            [2, '0.375'],
            [3, '0.625'],
            [4, '0.875']
        ],
        widget=widgets.RadioSelect
    )

    def answer2_error_message(self, value):
        if value != 3:
            return 'Wrong answer, try again.'

    answer1 = models.IntegerField(
        choices=[
            [1, '0.111'],
            [2, '0.125'],
            [3, '0.639'],
            [4, '0.597']
        ],
        widget=widgets.RadioSelect
    )

    def answer1_error_message(self, value):
        if value != 4:
            return 'Wrong answer, try again.'

    answer3 = models.IntegerField(
        choices=[
            [1, '15.75'],
            [2, '23.66'],
            [3, '45.00'],
            [4, '22.50']
        ],
        widget=widgets.RadioSelect
    )

    def answer3_error_message(self, value):
        if value != 1:
            return 'Wrong answer, try again.'


    answer4 = models.IntegerField(
        choices=[
            [1, 'X<135 and Y>45'],
            [2, 'X<112.5 and Y>56.25'],
            [3, 'X<225 and Y>112.5'],
            [4, 'X<90 and Y>67.5']
        ],
        widget=widgets.RadioSelect
    )

    def answer4_error_message(self, value):
        if value != 2:
            return 'Wrong answer, try again.'


    answer6 = models.IntegerField(
        choices=[
            [1, '336.41'],
            [2, '396.00'],
            [3, '448.55'],
            [4, '183.96']
        ],
        widget=widgets.RadioSelect
    )

    def answer6_error_message(self, value):
        if value != 4:
            return 'Wrong answer, try again.'

    answer5 = models.IntegerField(
        choices=[
            [1, '336.41'],
            [2, '396.00'],
            [3, '448.55'],
            [4, '169.09']
        ],
        widget=widgets.RadioSelect
    )

    def answer5_error_message(self, value):
        if value != 4:
            return 'Wrong answer, try again.'
