from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from helpers import get_next_app


class MyPage(Page):
    pass


class Results(Page):
    def vars_for_template(self):
        r = self.round_number
        p = self.player
        return {'num_states': self.session.vars["newt2_num_periods_round{}".format(r)] + 2,
                'probabilities': p.participant.vars["newt2_probabilities_round{}".format(r)],
                'payoff_s1': p.participant.vars["newt2_payoff_s1_round{}".format(r)],
                'payoff_s2': p.participant.vars["newt2_payoff_s2_round{}".format(r)],
                'payoff_s3': p.participant.vars["newt2_payoff_s3_round{}".format(r)],
                'payoff_s4': p.participant.vars["newt2_payoff_s4_round{}".format(r)],
                'payoff_s5': p.participant.vars["newt2_payoff_s5_round{}".format(r)],
                'portfolio': p.participant.vars["newt2_portfolio_round{}".format(r)],
                'weights': p.participant.vars["newt2_weights_round{}".format(r)],
                'realized_state': p.participant.vars["newt2_realized_state_round{}".format(r)],
                'realized_pay': p.participant.vars["newt2_realized_pay_round{}".format(r)]
                }

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


page_sequence = [Results]
