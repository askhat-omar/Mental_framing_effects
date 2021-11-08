import random

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
        player.participant.vars["app_id"] = random.randrange(len(settings.APP_KITS))
        player.participant.vars["step"] = 0

        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


class Results(Page):
    pass

page_sequence = [
    Page1
]
