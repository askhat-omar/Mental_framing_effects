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

    def app_after_this_page(player, upcoming_apps):
        # generate and initialize step
        iid_probs = np.random.binomial(n = 1, p = 0.5, size = 1)
        full_first = np.random.binomial(n = 1, p = 0.5, size = 1)
        if (full_first == 1) & (iid_probs == 1):
            player.participant.vars["app_id"] = 2
        elif (full_first == 1) & (iid_probs == 0):
            player.participant.vars["app_id"] = 0
        elif (full_first == 0) & (iid_probs == 1):
            player.participant.vars["app_id"] = 3
        elif (full_first == 0) & (iid_probs == 0):
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
