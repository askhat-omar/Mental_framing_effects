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
    name_in_url = 'dynamic_portfolio_3'
    players_per_group = None
    # Второй (Т=4) раунд я убрал, достаточно первого (Т=3)
    num_rounds = 1
    initial_wealth = 100
    # Начальная цена акции может быть случайной в диапазоне от 1 до 10
    initial_stock_price = 27
    # Вероятность того, что цена пойдет вверх. В dynamic_portfolio с одинаковыми вероятностями так и остается, в версии
    # с разными вероятностями при Т=2 вероятность меняется на 0.667, а при Т=3 вероятность меняется на 0.333. Думаю,
    # понятно, что вероятность того, что цена пойдет вниз равна 1 - up_prob
    up_prob = 0.5
    # Эти двое не меняются, это коэффициенты роста цены акции
    up_tick = 3
    down_tick = (1/3)


class Subsession(BaseSubsession):
    num_periods = models.IntegerField()
    dyn_prices = models.StringField()

# Здесь прописывается логика того, как меняется цена акции и как в зависимости от этого меняется богатство респондента
    def creating_session(self):
        num_rounds = Constants.num_rounds
        if self.round_number == 1:
            self.session.vars['num_rounds'] = num_rounds
            for r in range(1, num_rounds+1):
                t = self.session.config['round{}_T'.format(r)]
                self.in_round(r).num_periods = t
                price_label = "x_{}_{}"
                dyn_prices_list = {"x_0_1": Constants.initial_stock_price}
                for s in range(1, t+1, 1):
                    for i in range(1, 2**s+1, 1):
                        previous_i = int((i + 1)/2)
                        previous_price = dyn_prices_list[price_label.format(s-1, previous_i)]
                        if i % 2 == 0:
                            current_price = previous_price * Constants.down_tick
                        else:
                            current_price = previous_price * Constants.up_tick
                        dyn_prices_list[price_label.format(s, i)] = current_price
                self.in_round(r).dyn_prices = json.dumps(dyn_prices_list)
                self.session.vars["dyn_num_periods_round{}".format(r)] = self.in_round(r).num_periods
                self.session.vars["dyn_prices_round{}".format(r)] = self.in_round(r).dyn_prices


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    fill_history = models.StringField()
    dyn_wealth = models.StringField()
    dyn_stock = models.StringField()
    dyn_bond = models.StringField()
    dyn_realized_states = models.StringField()
    dyn_realized_wealth = models.FloatField()

# Здесь случайным образом выбираются результаты. Для dynamic_portfolio с одинаковыми вероятностями ничего не меняется,
# но для версии с меняющимися вероятностями возможно нужно через if поменять. Для dynamic_iterative нужно будет сделать
# то же самое, кроме того, что результат вычисляется и показывается респонденту сразу и пошагово (в dynamic_portfolio это
# делается в конце эксперимента)
    def dyn_get_outcome(self):
        upticks = numpy.random.binomial(1, Constants.up_prob, size=self.subsession.num_periods)
        downticks = 1 - upticks
        downticks = downticks.tolist()  # type: numpy.ndarray
        realized_states = {"0": 1}
        for t in range(1, self.subsession.num_periods+1, 1):
            state = 1
            for s in range(t):
                state = state + downticks[s] * 2**(t-s-1)
                realized_states[str(t)] = state
        self.dyn_realized_states = json.dumps(realized_states)
        wealth_list = json.loads(self.dyn_wealth)
        wealth_label = "w_{}_{}"
        final_t = self.subsession.num_periods
        final_state = realized_states[str(final_t)]
        self.dyn_realized_wealth = wealth_list[wealth_label.format(final_t, final_state)]
        self.payoff = self.dyn_realized_wealth
        r = self.round_number
        self.participant.vars["dyn_wealth_round{}".format(r)] = self.dyn_wealth
        self.participant.vars["dyn_stock_round{}".format(r)] = self.dyn_stock
        self.participant.vars["dyn_bond_round{}".format(r)] = self.dyn_bond
        self.participant.vars["dyn_realized_states_round{}".format(r)] = self.dyn_realized_states
        self.participant.vars["dyn_realized_wealth_round{}".format(r)] = self.dyn_realized_wealth
