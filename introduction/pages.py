import random
import numpy as np

from otree.api import Currency as c, currency_range

import settings
from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model = 'player'
    form_fields = ['data_priv']

    def before_next_page(self):
        self.player.get_booleans()

    def app_after_this_page(player, upcoming_apps):
        # generate and initialize step
        iid_probs = player.participant.vars["iid_probs"]
        full_first = player.participant.vars["full_first"]
        if (iid_probs == 1) & (full_first == 1):
            player.participant.vars["app_id"] = 1
        elif (iid_probs == 1) & (full_first == 0):
            player.participant.vars["app_id"] = 1
        elif (iid_probs == 0) & (full_first == 1):
            player.participant.vars["app_id"] = 1
        elif (iid_probs == 0) & (full_first == 0):
            player.participant.vars["app_id"] = 1

        player.participant.vars["step"] = 0

        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


class Results(Page):
    pass

page_sequence = [
    Page1
]
