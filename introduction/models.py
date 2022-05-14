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
    booleans = models.IntegerField()
    iid_probs = models.IntegerField()
    full_first = models.IntegerField()
    factor_three = models.IntegerField()

    data_priv = models.BooleanField(
        label="If you agree with the consent stated above, then please choose 'Agree' and press 'Next' button, otherwise please close the tab",
        choices=[
            [True, "Agree"]
        ]
    )

    def get_booleans(self):
        booleans = np.random.choice([1,2,3], p=[(1/3), (1/3), (1/3)])
        if booleans == 3:
            iid_probs = 1
            factor_three = 1
        elif booleans == 2:
            iid_probs = 1
            factor_three = 0
        else:
            iid_probs = 0
            factor_three = 0
        self.iid_probs = int(iid_probs)
        self.factor_three = int(factor_three)
        self.participant.vars["iid_probs"] = self.iid_probs
        self.participant.vars["factor_three"] = self.factor_three
