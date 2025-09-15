from otree.api import Currency as c, currency_range

from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants


class DynamicResults(Page):
    def vars_for_template(self):
        r = self.round_number
        return {
            'num_periods': self.session.vars["dyn_num_periods_round{}".format(r)],
            'prices': self.participant.vars["dyn_prices_round{}".format(r)],
            'wealth': self.participant.vars["dyn_wealth_round{}".format(r)],
            'stock': self.participant.vars["dyn_stock_round{}".format(r)],
            'bond': self.participant.vars["dyn_bond_round{}".format(r)],
            'realized_states': self.participant.vars["dyn_realized_states_round{}".format(r)],
            'realized_wealth': self.participant.vars["dyn_realized_wealth_round{}".format(r)]
        }

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


page_sequence = [
    DynamicResults
]
