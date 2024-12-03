from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from helpers import get_next_app


class Task_1(Page):
    form_model = 'player'
    form_fields = ['dyn_stock', 'dyn_bond', 'dyn_wealth']

    def vars_for_template(self):
        r = self.round_number
        p = self.player
        p.create_prices()
        return {
            'dyn_prices': p.participant.vars["dyn_prices_round{}".format(r)]
        }

    def before_next_page(self):
        self.player.dyn_get_outcome()

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


class MyPage(Page):
    pass


class Results(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [Results, Task_1]
