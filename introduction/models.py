from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    data_priv = models.BooleanField(
        label="If you agree with the consent stated above please choose 'Agree' and press 'Next' button, otherwise please close the tab",
        choices=[
            [True, "Agree"]
        ]
    )
