from otree.api import Currency as c, currency_range

from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants
import json


class MyPage(Page):
    pass


class Results(Page):
    def vars_for_template(self):
        r = self.round_number
        p = self.player
        return {'num_states': 2 ** self.session.vars["static_b_num_periods_round{}".format(r)],
                'probabilities': p.participant.vars["static_b_probabilities_round{}".format(r)],
                'payoff_a': p.participant.vars["static_b_payoff_a_round{}".format(r)],
                'payoff_b': p.participant.vars["static_b_payoff_b_round{}".format(r)],
                'payoff_c': p.participant.vars["static_b_payoff_c_round{}".format(r)],
                'payoff_d': p.participant.vars["static_b_payoff_d_round{}".format(r)],
                'lottery': p.participant.vars["static_b_lottery_round{}".format(r)],
                'realized_state': p.participant.vars["static_b_realized_state_round{}".format(r)],
                'realized_pay': p.participant.vars["static_b_realized_pay_round{}".format(r)]
                }

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


page_sequence = [Results]
