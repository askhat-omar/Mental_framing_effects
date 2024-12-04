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
    name_in_url = 'task3_tr13'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100
    probabilities = {"pr_1": 0.125, "pr_2": 0.125, "pr_3": 0.125, "pr_4": 0.125, "pr_5": 0.125, "pr_6": 0.125, "pr_7": 0.125, "pr_8": 0.125}
    payoff_a = {"pay_1": 233.93, "pay_2": 147.37, "pay_3": 147.37, "pay_4": 92.83, "pay_5": 147.37, "pay_6": 92.83, "pay_7": 92.83, "pay_8": 58.48}
    payoff_b = {"pay_1": 337.50, "pay_2": 168.75, "pay_3": 168.75, "pay_4": 84.38, "pay_5": 168.75, "pay_6": 84.38, "pay_7": 84.38, "pay_8": 42.19}
    payoff_d = {"pay_1": 800.00, "pay_2": 200.00, "pay_3": 200.00, "pay_4": 50.00, "pay_5": 200.00, "pay_6": 50.00, "pay_7": 50.00, "pay_8": 12.50}
    a = [233.93, 147.37, 147.37, 92.83, 147.37, 92.83, 92.83, 58.48]
    b = [337.50, 168.75, 168.75, 84.38, 168.75, 84.38, 84.38, 42.19]
    d = [800.00, 200.00, 200.00, 50.00, 200.00, 50.00, 50.00, 12.50]
    probs_for_payoff = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
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
        self.probabilities = json.dumps(Constants.probabilities)
        self.payoff_a = json.dumps(Constants.payoff_a)
        self.payoff_b = json.dumps(Constants.payoff_b)
        self.payoff_c = json.dumps(asset_c)
        self.payoff_d = json.dumps(Constants.payoff_d)

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


