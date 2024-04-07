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

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 4, "x_3_4": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 200.00, "w_1_2": 50.00, "w_2_1": "X",
                       "w_2_2": 150.00, "w_2_3": 0.00, "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": ""
                       }
        stock_list = {"s_0_1": 100, "s_1_1": 100, "s_1_2": 100, "s_2_1": "",
                      "s_2_2": "", "s_2_3": ""
                      }
        bond_list = {"b_0_1": 0, "b_1_1": 100, "b_1_2": -50, "b_2_1": "",
                     "b_2_2": "", "b_2_3": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }

class Question2(Page):
    form_model = 'player'
    form_fields = ['answer2']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 4, "x_3_4": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 400.00, "w_1_2": "X", "w_2_1": "",
                       "w_2_2": "", "w_2_3": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": ""
                       }
        stock_list = {"s_0_1": 300, "s_1_1": "", "s_1_2": "", "s_2_1": "",
                      "s_2_2": "", "s_2_3": ""
                      }
        bond_list = {"b_0_1": -200, "b_1_1": "", "b_1_2": "X", "b_2_1": "",
                     "b_2_2": "", "b_2_3": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }

class Question3(Page):
    form_model = 'player'
    form_fields = ['answer3']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 4, "x_3_4": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": "Y", "w_1_2": "Z", "w_2_1": "",
                       "w_2_2": "", "w_2_3": "", "w_3_1": "",
                       "w_3_2": "", "w_3_3": "", "w_3_4": ""
                       }
        stock_list = {"s_0_1": "X", "s_1_1": "", "s_1_2": "", "s_2_1": "",
                      "s_2_2": "", "s_2_3": ""
                      }
        bond_list = {"b_0_1": "", "b_1_1": "", "b_1_2": "X", "b_2_1": "",
                     "b_2_2": "", "b_2_3": ""
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }

class Question4(Page):
    form_model = 'player'
    form_fields = ['answer4']

    def vars_for_template(self):
        prices_list = {"x_0_1": 8, "x_1_1": 16, "x_1_2": 4, "x_2_1": 32,
                       "x_2_2": 8, "x_2_3": 2, "x_3_1": 64,
                       "x_3_2": 16, "x_3_3": 4, "x_3_4": 1
                       }
        wealth_list = {"w_0_1": 100, "w_1_1": 120.00, "w_1_2": 90.00, "w_2_1": 200.00,
                       "w_2_2": 80.00, "w_2_3": 95.00, "w_3_1": 260.00,
                       "w_3_2": 170.00, "w_3_3": 35.00, "w_3_4": 125.00
                       }
        stock_list = {"s_0_1": 20, "s_1_1": 80, "s_1_2": -10, "s_2_1": 60,
                      "s_2_2": 90, "s_2_3": -60
                      }
        bond_list = {"b_0_1": 80, "b_1_1": 40, "b_1_2": 100, "b_2_1": 140,
                     "b_2_2": -10, "b_2_3": 155
                     }
        states_list = {"0": "", "1": "", "2": "", "3": ""}

        return {
            'num_periods': 3,
            'prices': json.dumps(prices_list),
            'wealth': json.dumps(wealth_list),
            'stock': json.dumps(stock_list),
            'bond': json.dumps(bond_list),
            'realized_states': json.dumps(states_list)
        }

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


page_sequence = [Introduction, Question1, Question2, Question3, Question4]
