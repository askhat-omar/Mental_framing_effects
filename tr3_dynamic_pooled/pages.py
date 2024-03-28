from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['dyn_stock', 'dyn_bond', 'dyn_wealth', 'fill_history']

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


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return False


class Results(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [Results, MyPage]
