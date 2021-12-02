from otree.api import Currency as c, currency_range

from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants
import json

FORMAT_FLOAT = "{:.2f}"

class MyPage(Page):
    form_model = 'player'
    form_fields = ['lottery_chp']

    def vars_for_template(self):
        r = self.round_number
        p = self.player
        wealth = json.loads(p.participant.vars["dyn_wealth_round{}".format(r)])
        p.set_wealth(FORMAT_FLOAT.format(wealth["w_3_1"]),
                     FORMAT_FLOAT.format((wealth["w_3_2"] + wealth["w_3_3"] + wealth["w_3_5"]) / 3),
                     FORMAT_FLOAT.format((wealth["w_3_4"] + wealth["w_3_6"] + wealth["w_3_7"]) / 3),
                     FORMAT_FLOAT.format(wealth["w_3_8"]))
        return {
            'w_1': p.w_1,
            'w_2': p.w_2,
            'w_3': p.w_3,
            'w_4': p.w_4,
        }

    def before_next_page(self):
        p = self.player
        p.for_payoff()



    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage]
