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
    name_in_url = 'static_portfolio_b_chp'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100
    probabilities = {"pr_1": 0.111, "pr_2": 0.361, "pr_3": 0.403, "pr_4": 0.125}
    payoff_a = {"pay_1": 435.00, "pay_2": 286.00, "pay_3": 43.00, "pay_4": 8.00}
    payoff_c = {"pay_1": 225.00, "pay_2": 167.00, "pay_3": 70.00, "pay_4": 32.00}
    payoff_d = {"pay_1": 164.00, "pay_2": 131.00, "pay_3": 75.00, "pay_4": 44.00}
    a = [435.00, 286.00, 43.00, 8.00]
    c = [225.00, 167.00, 70.00, 32.00]
    d = [164.00, 131.00, 75.00, 44.00]
    probs_for_payoff = [0.111, 0.361, 0.403, 0.125]
    states_for_payoff = [1, 2, 3, 4]


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

    w_1 = models.StringField()
    w_2 = models.StringField()
    w_3 = models.StringField()
    w_4 = models.StringField()
    pf_1 = models.StringField()
    pf_2 = models.StringField()
    pf_3 = models.StringField()
    pf_4 = models.StringField()
    payoff_a = models.StringField()
    payoff_b = models.StringField()
    payoff_c = models.StringField()
    payoff_d = models.StringField()
    static_realized_state = models.IntegerField()
    static_realized_pay = models.FloatField()
    probabilities = models.StringField()

    def set_wealth(self, w_1, w_2, w_3, w_4):
        self.w_1 = w_1
        self.w_2 = w_2
        self.w_3 = w_3
        self.w_4 = w_4
        asset_b = {"pay_1": self.w_1, "pay_2": self.w_2, "pay_3": self.w_3, "pay_4": self.w_4}
        self.probabilities = json.dumps(Constants.probabilities)
        self.payoff_a = json.dumps(Constants.payoff_a)
        self.payoff_b = json.dumps(asset_b)
        self.payoff_c = json.dumps(Constants.payoff_c)
        self.payoff_d = json.dumps(Constants.payoff_d)

    def for_payoff(self):
        self.static_realized_state = int(numpy.random.choice(Constants.states_for_payoff, p=Constants.probs_for_payoff))
        payoff_label = "pay_{}"
        asset_b = {"pay_1": self.w_1, "pay_2": self.w_2, "pay_3": self.w_3, "pay_4": self.w_4}
        if self.lottery == '1':
            k = Constants.payoff_a[payoff_label.format(self.static_realized_state)]
        elif self.lottery == '2':
            k = asset_b[payoff_label.format(self.static_realized_state)]
        elif self.lottery == '3':
            k = Constants.payoff_c[payoff_label.format(self.static_realized_state)]
        else:
            k = Constants.payoff_d[payoff_label.format(self.static_realized_state)]
        if (float(k) - numpy.floor(float(k))) >= 0.5:
            self.static_realized_pay = numpy.ceil(float(k))
        else:
            self.static_realized_pay = numpy.floor(float(k))
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
