from otree.api import Currency as c, currency_range
from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants
import json


class Introduction(Page):
    pass


class Question1(Page):
    form_model = 'player'
    form_fields = ['answer1']

    def is_displayed(self):
        player = self.player
        return player.participant.vars["treatment"] == 2

    def vars_for_template(self):
        probability_list = {"pr_1": 0.111, "pr_2": 0.361, "pr_3": 0.403, "pr_4": 0.125
                       }
        payoff_s1 = {"AD_1": 27.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s2 = {"AD_1": 0.00, "AD_2": 4.50, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25, "AD_4": 0.00}
        payoff_s4 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 3.38}
        portfolio = {"pf_1": "", "pf_2": "", "pf_3": "", "pf_4": ""}
        weights = {"w_1": "", "w_2": "", "w_3": "", "w_4": ""}
        realized_state = ""

        return {
            'num_states': 4,
            'probabilities': json.dumps(probability_list),
            'payoff_s1': json.dumps(payoff_s1),
            'payoff_s2': json.dumps(payoff_s2),
            'payoff_s3': json.dumps(payoff_s3),
            'payoff_s4': json.dumps(payoff_s4),
            'portfolio': json.dumps(portfolio),
            'weights': json.dumps(weights),
            'realized_state': realized_state
        }


class Question2(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def is_displayed(self):
        player = self.player
        return player.participant.vars["treatment"] == 1

    def vars_for_template(self):
        probability_list = {"pr_1": 0.125, "pr_2": 0.375, "pr_3": 0.375, "pr_4": 0.125
                            }
        payoff_s1 = {"AD_1": 27.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s2 = {"AD_1": 0.00, "AD_2": 4.50, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25, "AD_4": 0.00}
        payoff_s4 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 3.38}
        portfolio = {"pf_1": "", "pf_2": "", "pf_3": "", "pf_4": ""}
        weights = {"w_1": "", "w_2": "", "w_3": "", "w_4": ""}
        realized_state = ""

        return {
            'num_states': 4,
            'probabilities': json.dumps(probability_list),
            'payoff_s1': json.dumps(payoff_s1),
            'payoff_s2': json.dumps(payoff_s2),
            'payoff_s3': json.dumps(payoff_s3),
            'payoff_s4': json.dumps(payoff_s4),
            'portfolio': json.dumps(portfolio),
            'weights': json.dumps(weights),
            'realized_state': realized_state
        }


class Question3(Page):
    form_model = 'player'
    form_fields = ['answer3']

    def vars_for_template(self):
        probability_list = {"pr_1": "", "pr_2": "", "pr_3": "", "pr_4": ""
                            }
        payoff_s1 = {"AD_1": 27.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s2 = {"AD_1": 0.00, "AD_2": 4.50, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25, "AD_4": 0.00}
        payoff_s4 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 3.38}
        portfolio = {"pf_1": 2160.00, "pf_2": 45.00, "pf_3": "?", "pf_4": 10.14}
        weights = {"w_1": 80, "w_2": 10, "w_3": 7, "w_4": 3}
        realized_state = ""

        return {
            'num_states': 4,
            'probabilities': json.dumps(probability_list),
            'payoff_s1': json.dumps(payoff_s1),
            'payoff_s2': json.dumps(payoff_s2),
            'payoff_s3': json.dumps(payoff_s3),
            'payoff_s4': json.dumps(payoff_s4),
            'portfolio': json.dumps(portfolio),
            'weights': json.dumps(weights),
            'realized_state': realized_state
        }



class Question4(Page):
    form_model = 'player'
    form_fields = ['answer4']

    def vars_for_template(self):
        probability_list = {"pr_1": "", "pr_2": "", "pr_3": "", "pr_4": ""
                            }
        payoff_s1 = {"AD_1": 27.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s2 = {"AD_1": 0.00, "AD_2": 4.50, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25, "AD_4": 0.00}
        payoff_s4 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 3.38}
        portfolio = {"pf_1": 324.00, "pf_2": "X", "pf_3": "Y", "pf_4": 128.44}
        weights = {"w_1": 12, "w_2": "A", "w_3": "B", "w_4": 38}
        realized_state = ""

        return {
            'num_states': 4,
            'probabilities': json.dumps(probability_list),
            'payoff_s1': json.dumps(payoff_s1),
            'payoff_s2': json.dumps(payoff_s2),
            'payoff_s3': json.dumps(payoff_s3),
            'payoff_s4': json.dumps(payoff_s4),
            'portfolio': json.dumps(portfolio),
            'weights': json.dumps(weights),
            'realized_state': realized_state
        }


class Question5(Page):
    form_model = 'player'
    form_fields = ['answer5']

    def is_displayed(self):
        player = self.player
        return player.participant.vars["treatment"] == 2

    def vars_for_template(self):
        probability_list = {"pr_1": 0.111, "pr_2": 0.361, "pr_3": 0.403, "pr_4": 0.125
                            }
        payoff_s1 = {"AD_1": 27.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s2 = {"AD_1": 0.00, "AD_2": 4.50, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25, "AD_4": 0.00}
        payoff_s4 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 3.38}
        portfolio = {"pf_1": 1188.00, "pf_2": 0.00, "pf_3": 63.00, "pf_4": 94.64}
        weights = {"w_1": 44, "w_2": 0, "w_3": 28, "w_4": 28}
        realized_state = ""

        return {
            'num_states': 4,
            'probabilities': json.dumps(probability_list),
            'payoff_s1': json.dumps(payoff_s1),
            'payoff_s2': json.dumps(payoff_s2),
            'payoff_s3': json.dumps(payoff_s3),
            'payoff_s4': json.dumps(payoff_s4),
            'portfolio': json.dumps(portfolio),
            'weights': json.dumps(weights),
            'realized_state': realized_state
        }
    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


class Question6(Page):
    form_model = 'player'
    form_fields = ['answer6']

    def is_displayed(self):
        player = self.player
        return player.participant.vars["treatment"] == 1

    def vars_for_template(self):
        probability_list = {"pr_1": 0.125, "pr_2": 0.375, "pr_3": 0.375, "pr_4": 0.125
                            }
        payoff_s1 = {"AD_1": 27.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s2 = {"AD_1": 0.00, "AD_2": 4.50, "AD_3": 0.00, "AD_4": 0.00}
        payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25, "AD_4": 0.00}
        payoff_s4 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 0.00, "AD_4": 3.38}
        portfolio = {"pf_1": 1188.00, "pf_2": 0.00, "pf_3": 63.00, "pf_4": 94.64}
        weights = {"w_1": 44, "w_2": 0, "w_3": 28, "w_4": 28}
        realized_state = ""

        return {
            'num_states': 4,
            'probabilities': json.dumps(probability_list),
            'payoff_s1': json.dumps(payoff_s1),
            'payoff_s2': json.dumps(payoff_s2),
            'payoff_s3': json.dumps(payoff_s3),
            'payoff_s4': json.dumps(payoff_s4),
            'portfolio': json.dumps(portfolio),
            'weights': json.dumps(weights),
            'realized_state': realized_state
        }
    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


page_sequence = [
    Introduction,
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6
]
