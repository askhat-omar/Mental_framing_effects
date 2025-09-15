from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy as np
import json


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'task4_tr2'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100
    probabilities = {"pr_1": 1/8, "pr_2": 1/8, "pr_3": 1/6, "pr_4": 1/12, "pr_5": 1/9, "pr_6": 1/18, "pr_7": 2/9, "pr_8": 1/9}
    probs_for_payoff = [1/8, 1/8, 1/6, 1/12, 1/9, 1/18, 2/9, 1/9]
    states_for_payoff = [1, 2, 3, 4, 5, 6, 7, 8]


class Subsession(BaseSubsession):
    num_periods = models.IntegerField()

    def creating_session(self):
        num_rounds = Constants.num_rounds
        if self.round_number == 1:
            self.session.vars['num_rounds'] = num_rounds
            for r in range(1, num_rounds + 1):
                t = self.session.config['round{}_T'.format(r)]
                self.in_round(r).num_periods = t
                self.session.vars["static_b_num_periods_round{}".format(r)] = self.in_round(r).num_periods


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery = models.StringField(
        choices=[[1, 'I prefer asset A'], [2, 'I prefer asset B'], [3, 'I prefer asset C'], [4, 'I prefer asset D']],
        widget=widgets.RadioSelect
    )

    w_1 = models.FloatField()
    w_2 = models.FloatField()
    w_3 = models.FloatField()
    w_4 = models.FloatField()
    w_5 = models.FloatField()
    w_6 = models.FloatField()
    w_7 = models.FloatField()
    w_8 = models.FloatField()
    payoff_a = models.StringField()
    payoff_b = models.StringField()
    payoff_c = models.StringField()
    payoff_d = models.StringField()
    static_realized_state = models.IntegerField()
    static_realized_pay = models.FloatField()
    probabilities = models.StringField()

    def set_wealth(self, w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8):
        self.w_1 = float(w_1)
        self.w_2 = float(w_2)
        self.w_3 = float(w_3)
        self.w_4 = float(w_4)
        self.w_5 = float(w_5)
        self.w_6 = float(w_6)
        self.w_7 = float(w_7)
        self.w_8 = float(w_8)

        asset_a = {"pay_1": max(self.w_8 - 5, 0), "pay_2": max(self.w_7 - 10, 0), "pay_3": max(self.w_6 - 10, 0),
                   "pay_4": max(self.w_5 - 15, 0), "pay_5": max(self.w_4 - 10, 0), "pay_6": max(self.w_3 - 15, 0),
                   "pay_7": max(self.w_2 - 15, 0), "pay_8": max(self.w_1 - 20, 0)}
        asset_b = {"pay_1": self.w_8, "pay_2": self.w_7, "pay_3": self.w_6, "pay_4": self.w_5, "pay_5": self.w_4,
                   "pay_6": self.w_3, "pay_7": self.w_2, "pay_8": self.w_1}
        asset_c = {"pay_1": max(self.w_8 - 20, 0), "pay_2": max(self.w_7 - 15, 0), "pay_3": max(self.w_6 - 15, 0),
                   "pay_4": max(self.w_5 - 10, 0), "pay_5": max(self.w_4 - 15, 0), "pay_6": max(self.w_3 - 10, 0),
                   "pay_7": max(self.w_2 - 10, 0), "pay_8": max(self.w_1 - 5, 0)}
        asset_d = {"pay_1": max(self.w_8 - 10, 0), "pay_2": max(self.w_7 - 20, 0), "pay_3": max(self.w_6 - 20, 0),
                   "pay_4": max(self.w_5 - 5, 0), "pay_5": max(self.w_4 - 20, 0), "pay_6": max(self.w_3 - 5, 0),
                   "pay_7": max(self.w_2 - 5, 0), "pay_8": max(self.w_1 - 15, 0)}

        self.probabilities = json.dumps(Constants.probabilities)
        self.payoff_a = json.dumps(asset_a)
        self.payoff_b = json.dumps(asset_b)
        self.payoff_c = json.dumps(asset_c)
        self.payoff_d = json.dumps(asset_d)

    def for_payoff(self):
        self.static_realized_state = int(np.random.choice(Constants.states_for_payoff, p=Constants.probs_for_payoff))
        payoff_label = "pay_{}"
        asset_a = {"pay_1": max(self.w_8 - 5, 0), "pay_2": max(self.w_7 - 10, 0), "pay_3": max(self.w_6 - 10, 0),
                   "pay_4": max(self.w_5 - 15, 0), "pay_5": max(self.w_4 - 10, 0), "pay_6": max(self.w_3 - 15, 0),
                   "pay_7": max(self.w_2 - 15, 0), "pay_8": max(self.w_1 - 20, 0)}
        asset_b = {"pay_1": self.w_8, "pay_2": self.w_7, "pay_3": self.w_6, "pay_4": self.w_5, "pay_5": self.w_4,
                   "pay_6": self.w_3, "pay_7": self.w_2, "pay_8": self.w_1}
        asset_c = {"pay_1": max(self.w_8 - 20, 0), "pay_2": max(self.w_7 - 15, 0), "pay_3": max(self.w_6 - 15, 0),
                   "pay_4": max(self.w_5 - 10, 0), "pay_5": max(self.w_4 - 15, 0), "pay_6": max(self.w_3 - 10, 0),
                   "pay_7": max(self.w_2 - 10, 0), "pay_8": max(self.w_1 - 5, 0)}
        asset_d = {"pay_1": max(self.w_8 - 10, 0), "pay_2": max(self.w_7 - 20, 0), "pay_3": max(self.w_6 - 20, 0),
                   "pay_4": max(self.w_5 - 5, 0), "pay_5": max(self.w_4 - 20, 0), "pay_6": max(self.w_3 - 5, 0),
                   "pay_7": max(self.w_2 - 5, 0), "pay_8": max(self.w_1 - 15, 0)}
        if self.lottery == '1':
            k = asset_a[payoff_label.format(self.static_realized_state)]
        elif self.lottery == '2':
            k = asset_b[payoff_label.format(self.static_realized_state)]
        elif self.lottery == '3':
            k = asset_c[payoff_label.format(self.static_realized_state)]
        else:
            k = asset_d[payoff_label.format(self.static_realized_state)]
        self.static_realized_pay = float(k)
        self.payoff = self.static_realized_pay
        r = self.round_number
        self.participant.vars["static_b_lottery_round{}".format(r)] = self.lottery
        self.participant.vars["static_b_probabilities_round{}".format(r)] = self.probabilities
        self.participant.vars["static_b_payoff_a_round{}".format(r)] = self.payoff_a
        self.participant.vars["static_b_payoff_b_round{}".format(r)] = self.payoff_b
        self.participant.vars["static_b_payoff_c_round{}".format(r)] = self.payoff_c
        self.participant.vars["static_b_payoff_d_round{}".format(r)] = self.payoff_d
        self.participant.vars["static_b_realized_state_round{}".format(r)] = self.static_realized_state
        self.participant.vars["static_b_realized_pay_round{}".format(r)] = self.static_realized_pay
