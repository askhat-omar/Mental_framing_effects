from otree.api import Currency as c, currency_range

from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants


class Dynamic(Page):
    form_model = 'player'
    form_fields = ['dyn_stock', 'dyn_bond', 'dyn_wealth', 'dyn_realized_states']

    def before_next_page(self):
        self.player.dyn_get_outcome()

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Intro,
    Dynamic
]
