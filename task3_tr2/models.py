from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy
import json


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'task3_tr2'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100
    probabilities = {"pr_1": 1/9, "pr_2": 2/9, "pr_3": 1/18, "pr_4": 1/9, "pr_5": 1/12, "pr_6": 1/6, "pr_7": 1/8, "pr_8": 1/8}
    payoff_a = {"pay_1": 218.06, "pay_2": 218.06, "pay_3": 86.54, "pay_4": 86.54, "pay_5": 113.40, "pay_6": 113.40, "pay_7": 93.61, "pay_8": 58.97}
    payoff_b = {"pay_1": 300.00, "pay_2": 300.00, "pay_3": 75.00, "pay_4": 75.00, "pay_5": 112.50, "pay_6": 112.50, "pay_7": 84.38, "pay_8": 42.19}
    payoff_d = {"pay_1": 575.28, "pay_2": 575.28, "pay_3": 35.96, "pay_4": 35.96, "pay_5": 80.90, "pay_6": 80.90, "pay_7": 45.51, "pay_8": 11.38}
    a = [218.06, 218.06, 86.54, 86.54, 113.40, 113.40, 93.61, 58.97]
    b = [300.00, 300.00, 75.00, 75.00, 112.50, 112.50, 84.38, 42.19]
    d = [575.29, 575.29, 35.96, 35.96, 80.90, 80.90, 45.51, 11.38]
    probs_for_payoff = [1/9, 2/9, 1/18, 1/9, 1/12, 1/6, 1/8, 1/8]
    states_for_payoff = [1, 2, 3, 4, 5, 6, 7, 8]




class Subsession(BaseSubsession):
    num_periods = models.IntegerField()

    def creating_session(self):
        num_rounds = Constants.num_rounds
        if self.round_number == 1:
            self.session.vars['num_rounds'] = num_rounds
            for r in range(1, num_rounds+1):
                t = self.session.config['round{}_T'.format(r)]
                self.in_round(r).num_periods = t
                self.session.vars["static_num_periods_round{}".format(r)] = self.in_round(r).num_periods



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery = models.StringField(
        choices=[[1,'I prefer asset A'], [2, 'I prefer asset B'], [3, 'I prefer asset C'], [4, 'I prefer asset D']], widget=widgets.RadioSelect
    )

    w_1 = models.StringField()
    w_2 = models.StringField()
    w_3 = models.StringField()
    w_4 = models.StringField()
    w_5 = models.StringField()
    w_6 = models.StringField()
    w_7 = models.StringField()
    w_8 = models.StringField()
    payoff_a = models.StringField()
    payoff_b = models.StringField()
    payoff_c = models.StringField()
    payoff_d = models.StringField()
    static_realized_state = models.IntegerField()
    static_realized_pay = models.FloatField()
    probabilities = models.StringField()



    def set_wealth(self, w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8):
        self.w_1 = w_1
        self.w_2 = w_2
        self.w_3 = w_3
        self.w_4 = w_4
        self.w_5 = w_5
        self.w_6 = w_6
        self.w_7 = w_7
        self.w_8 = w_8
        asset_c = {"pay_1": self.w_1, "pay_2": self.w_2, "pay_3": self.w_3, "pay_4": self.w_4, "pay_5": self.w_5, "pay_6": self.w_6, "pay_7": self.w_7, "pay_8": self.w_8}
        self.payoff_a = json.dumps(Constants.payoff_a)
        self.payoff_b = json.dumps(Constants.payoff_b)
        self.payoff_c = json.dumps(asset_c)
        self.payoff_d = json.dumps(Constants.payoff_d)
        self.probabilities = json.dumps(Constants.probabilities)



    def for_payoff(self):
        self.static_realized_state = int(numpy.random.choice(Constants.states_for_payoff, p=Constants.probs_for_payoff))
        payoff_label = "pay_{}"
        asset_c = {"pay_1": self.w_1, "pay_2": self.w_2, "pay_3": self.w_3, "pay_4": self.w_4, "pay_5": self.w_5, "pay_6": self.w_6, "pay_7": self.w_7, "pay_8": self.w_8}
        if self.lottery == '1':
            k = Constants.payoff_a[payoff_label.format(self.static_realized_state)]
        elif self.lottery == '2':
            k = Constants.payoff_b[payoff_label.format(self.static_realized_state)]
        elif self.lottery == '3':
            k = asset_c[payoff_label.format(self.static_realized_state)]
        else:
            k = Constants.payoff_d[payoff_label.format(self.static_realized_state)]
        self.static_realized_pay = float(k)
        self.payoff = self.static_realized_pay
        r = self.round_number
        self.participant.vars["static_lottery_round{}".format(r)] = self.lottery
        self.participant.vars["static_probabilities_round{}".format(r)] = self.probabilities
        self.participant.vars["static_payoff_a_round{}".format(r)] = self.payoff_a
        self.participant.vars["static_payoff_b_round{}".format(r)] = self.payoff_b
        self.participant.vars["static_payoff_c_round{}".format(r)] = self.payoff_c
        self.participant.vars["static_payoff_d_round{}".format(r)] = self.payoff_d
        self.participant.vars["static_realized_state_round{}".format(r)] = self.static_realized_state
        self.participant.vars["static_realized_pay_round{}".format(r)] = self.static_realized_pay


