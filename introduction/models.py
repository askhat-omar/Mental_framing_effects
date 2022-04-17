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
        iid_probs = np.random.binomial(n=1, p=0.5, size=1)
        full_first = np.random.binomial(n=1, p=0.5, size=1)
        factor_three = np.random.binomial(n=1, p=0.5, size=1)
        self.iid_probs = int(iid_probs)
        self.full_first = int(full_first)
        self.factor_three = int(factor_three)
        self.participant.vars["iid_probs"] = self.iid_probs
        self.participant.vars["full_first"] = self.full_first
        self.participant.vars["factor_three"] = self.factor_three
