from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json


class Static(Page):
    form_model = 'player'
    form_fields = ['lottery']

    def vars_for_template(self):
        r = self.round_number
        p = self.player
        wealth = json.loads(p.participant.vars["dyn_wealth_round{}".format(r)])
        return {
            'w_1': wealth["w_3_1"],
            'w_2': (wealth["w_3_2"] + wealth["w_3_3"] + wealth["w_3_5"]) / 3,
            'w_3': (wealth["w_3_4"] + wealth["w_3_6"] + wealth["w_3_7"]) / 3,
            'w_4': wealth["w_3_8"],
        }


page_sequence = [Static]
