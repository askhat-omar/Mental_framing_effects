import json
import numpy as np
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
    treatment = models.IntegerField()

    id_label = models.StringField(label='Please enter your matriculation number:')

    data_priv = models.BooleanField(
        label="If you agree with the consent stated above, then please choose 'Agree' and press 'Next' button, otherwise please close the tab",
        choices=[
            [True, "Agree"]
        ]
    )

    def get_booleans(self):
        treatment = int(np.random.choice([1,2,3], p=[(1/4), (1/2), (1/4)]))
        self.treatment = treatment
        self.participant.vars["treatment"] = self.treatment
        self.participant.label = self.id_label
