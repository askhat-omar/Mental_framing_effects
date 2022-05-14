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
    name_in_url = 'new_task2_practice'
    players_per_group = None
    num_rounds = 1
    initial_wealth = 100
    probabilities = {"pr_1": 0.25, "pr_2": 0.50, "pr_3": 0.25}
    payoff_s1 = {"AD_1": 9.00, "AD_2": 0.00, "AD_3": 0.00}
    payoff_s2 = {"AD_1": 0.00, "AD_2": 2.25, "AD_3": 0.00}
    payoff_s3 = {"AD_1": 0.00, "AD_2": 0.00, "AD_3": 2.25}
    probs_for_payoff = [0.25, 0.50, 0.25]
    states_for_payoff = [1, 2, 3]


class Subsession(BaseSubsession):
    num_periods = models.IntegerField()
    probabilities = models.StringField()
    payoff_s1 = models.StringField()
    payoff_s2 = models.StringField()
    payoff_s3 = models.StringField()
    payoff_s4 = models.StringField()

    def creating_session(self):
        num_rounds = Constants.num_rounds
        if self.round_number == 1:
            self.session.vars['num_rounds'] = num_rounds
            for r in range(1, num_rounds+1):
                t = self.session.config['round{}_T'.format(r)]
                self.in_round(r).num_periods = t
                self.session.vars["newt2_num_periods_round{}".format(r)] = self.in_round(r).num_periods



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    newt2_weights = models.StringField()
    newt2_realized_state = models.IntegerField()
    newt2_portfolio = models.StringField()
    newt2_realized_pay = models.FloatField()
    probabilities = models.StringField()
    payoff_s1 = models.StringField()
    payoff_s2 = models.StringField()
    payoff_s3 = models.StringField()
    payoff_s4 = models.StringField()
    weights_temp = models.StringField()

    def for_template(self):
        self.probabilities = json.dumps(Constants.probabilities)
        self.payoff_s1 = json.dumps(Constants.payoff_s1)
        self.payoff_s2 = json.dumps(Constants.payoff_s2)
        self.payoff_s3 = json.dumps(Constants.payoff_s3)


    def newt2_get_outcome(self):
        self.newt2_realized_state = int(np.random.choice(Constants.states_for_payoff, p=Constants.probs_for_payoff))
        weights_list = json.loads(self.newt2_weights)
        payoff_label = "AD_{}"
        portfolio_label = "pf_{}"
        portfolio_payoffs = {"pf_1": 0}
        variables = [Constants.payoff_s1, Constants.payoff_s2, Constants.payoff_s3]
        payoff_matrix = np.zeros(shape=(3, 3))
        for i in range(1, 4):
            for j in range(1, 4):
                payoff_matrix[i - 1, j - 1] = variables[i - 1][payoff_label.format(j)]
        weights = np.array([weights_list["w_1"], weights_list["w_2"], weights_list["w_3"]])
        result = np.zeros(shape=(3, 3))
        for n in range(3):
            for k in range(3):
                result[n, k] = payoff_matrix[n, k] * weights[k]
        portfolio = np.round(result.sum(axis=1),1)
        for p in range(1, 4):
            portfolio_payoffs[portfolio_label.format(p)] = portfolio[p - 1]
        #
        self.newt2_realized_pay = portfolio_payoffs[portfolio_label.format(self.newt2_realized_state)]
        self.newt2_portfolio = json.dumps(portfolio_payoffs)
        self.weights_temp = json.dumps(weights_list)
