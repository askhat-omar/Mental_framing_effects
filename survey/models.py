from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prev_participation = models.StringField(
        choices=['No', 'Yes'],
        widget=widgets.RadioSelectHorizontal
    )

    sex = models.StringField(
        choices=['Female', 'Male'],
        widget=widgets.RadioSelectHorizontal
    )

    year = models.StringField(
        choices=['1st year Bachelor', '2nd year Bachelor', '3rd year Bachelor', '4th year Bachelor', 'Master student',
                 'Doctoral Student', 'Faculty', 'Staff']
    )

    major = models.StringField(
        choices=['STEM',
                 'Economics & Finance',
                 'Business & Management',
                 'Social Sciences',
                 'Art & Humanities',
                 'Medicine',
                 'Other'
                 ]
    )
