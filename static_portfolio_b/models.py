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
    name_in_url = 'static_portfolio_b'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100
    probabilities = {"pr_1": 0.125, "pr_2": 0.375, "pr_3": 0.375, "pr_4": 0.125}
    probs_for_payoff = [0.125, 0.375, 0.375, 0.125]
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

    a_w_1 = models.FloatField()
    a_w_2 = models.FloatField()
    a_w_3 = models.FloatField()
    a_w_4 = models.FloatField()
    b_w_1 = models.FloatField()
    b_w_2 = models.FloatField()
    b_w_3 = models.FloatField()
    b_w_4 = models.FloatField()
    c_w_1 = models.FloatField()
    c_w_2 = models.FloatField()
    c_w_3 = models.FloatField()
    c_w_4 = models.FloatField()
    d_w_1 = models.FloatField()
    d_w_2 = models.FloatField()
    d_w_3 = models.FloatField()
    d_w_4 = models.FloatField()
    payoff_a = models.StringField()
    payoff_b = models.StringField()
    payoff_c = models.StringField()
    payoff_d = models.StringField()
    static_realized_state = models.IntegerField()
    static_realized_pay = models.FloatField()
    probabilities = models.StringField()

    def set_wealth(self, b_w_1, b_w_2, b_w_3, b_w_4):
        self.b_w_1 = float(b_w_1)
        self.b_w_2 = float(b_w_2)
        self.b_w_3 = float(b_w_3)
        self.b_w_4 = float(b_w_4)
        asset_b = {"pay_1": self.b_w_4, "pay_2": self.b_w_3, "pay_3": self.b_w_2, "pay_4": self.b_w_1}

        choice = np.array([self.b_w_1, self.b_w_2, self.b_w_3, self.b_w_4])
        w_3U = choice[0]
        w_2U = choice[1]
        w_1U = choice[2]
        w_0U = choice[3]
        if np.all(choice[1:] == 0):
            a1 = np.array([680, 170, 43, 10])
            a2 = np.array([287, 144, 71, 36])
            a3 = np.array([199, 125, 79, 49])

        elif np.all(choice[2:] == 0):
            diff = round(choice[1] - choice[1]/2, 2)
            a1_w2U = choice[1] - diff
            a1_w3U = choice[0] + round(1.5 * diff, 2)
            a1 = np.array([a1_w3U, a1_w2U, w_1U, w_0U])

            diff = round(choice[1] - choice[1]/2.5, 2)
            a2_w2U = choice[1] - diff
            a2_w3U = choice[0] + round(1.5 * diff, 2)
            a2 = np.array([a2_w3U, a2_w2U, w_1U, w_0U])

            diff = round(choice[1] - choice[1]/1.5, 2)
            a3_w2U = choice[1] - diff
            a3_w3U = choice[0] + round(1.5 * diff, 2)
            a3 = np.array([a3_w3U, a3_w2U, w_1U, w_0U])

        elif choice[2] == 0:
            diff = round(choice[1] - choice[1]/2, 2)
            a1_w2U = choice[1] - diff
            a1_w3U = choice[0] + round(0.75 * diff, 2)
            a1_w0U = choice[3] + round(0.75 * diff, 2)
            a1 = np.array([a1_w3U, a1_w2U, w_1U, a1_w0U])

            diff = round(choice[1] - choice[1]/2.5, 2)
            a2_w2U = choice[1] - diff
            a2_w3U = choice[0] + round(0.75 * diff, 2)
            a2_w0U = choice[3] + round(0.75 * diff, 2)
            a2 = np.array([a2_w3U, a2_w2U, w_1U, a2_w0U])

            diff = round(choice[1] - choice[1]/1.5, 2)
            a3_w2U = choice[1] - diff
            a3_w3U = choice[0] + round(0.75 * diff, 2)
            a3_w0U = choice[3] + round(0.75 * diff, 2)
            a3 = np.array([a3_w3U, a3_w2U, w_1U, a3_w0U])

        else:
            diff1 = round(choice[1] - choice[1]/2, 2)
            diff2 = round(choice[2] - choice[2]/3, 2)
            a1_w2U = choice[1] - diff1
            a1_w1U = choice[2] - diff2
            a1_w3U = choice[0] + round(1.5 * diff1, 2)
            a1_w0U = choice[3] + round(1.5 * diff2, 2)
            a1 = np.array([a1_w3U, a1_w2U, a1_w1U, a1_w0U])

            diff1 = round(choice[1] - choice[1]/2.5, 2)
            diff2 = round(choice[2] - choice[2]/3.5, 2)
            a2_w2U = choice[1] - diff1
            a2_w1U = choice[2] - diff2
            a2_w3U = choice[0] + round(1.5 * diff1, 2)
            a2_w0U = choice[3] + round(1.5 * diff2, 2)
            a2 = np.array([a2_w3U, a2_w2U, a2_w1U, a2_w0U])

            diff1 = round(choice[1] - choice[1]/1.5, 2)
            diff2 = round(choice[2] - choice[2]/2.5, 2)
            a3_w2U = choice[1] - diff1
            a3_w1U = choice[2] - diff2
            a3_w3U = choice[0] + round(1.5 * diff1, 2)
            a3_w0U = choice[3] + round(1.5 * diff2, 2)
            a3 = np.array([a3_w3U, a3_w2U, a3_w1U, a3_w0U])

        asset_a = {"pay_1": a1[3], "pay_2": a1[2], "pay_3": a1[1], "pay_4": a1[0]}
        asset_c = {"pay_1": a2[3], "pay_2": a2[2], "pay_3": a2[1], "pay_4": a2[0]}
        asset_d = {"pay_1": a3[3], "pay_2": a3[2], "pay_3": a3[1], "pay_4": a3[0]}

        self.a_w_1 = a1[0]
        self.a_w_2 = a1[1]
        self.a_w_3 = a1[2]
        self.a_w_4 = a1[3]
        self.c_w_1 = a2[0]
        self.c_w_2 = a2[1]
        self.c_w_3 = a2[2]
        self.c_w_4 = a2[3]
        self.d_w_1 = a3[0]
        self.d_w_2 = a3[1]
        self.d_w_3 = a3[2]
        self.d_w_4 = a3[3]

        self.probabilities = json.dumps(Constants.probabilities)
        self.payoff_a = json.dumps(asset_a)
        self.payoff_b = json.dumps(asset_b)
        self.payoff_c = json.dumps(asset_c)
        self.payoff_d = json.dumps(asset_d)

    def for_payoff(self):
        self.static_realized_state = int(np.random.choice(Constants.states_for_payoff, p=Constants.probs_for_payoff))
        payoff_label = "pay_{}"
        asset_a = {"pay_1": self.a_w_4, "pay_2": self.a_w_3, "pay_3": self.a_w_2, "pay_4": self.a_w_1}
        asset_b = {"pay_1": self.b_w_4, "pay_2": self.b_w_3, "pay_3": self.b_w_2, "pay_4": self.b_w_1}
        asset_c = {"pay_1": self.c_w_4, "pay_2": self.c_w_3, "pay_3": self.c_w_2, "pay_4": self.c_w_1}
        asset_d = {"pay_1": self.d_w_4, "pay_2": self.d_w_3, "pay_3": self.d_w_2, "pay_4": self.d_w_1}
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
