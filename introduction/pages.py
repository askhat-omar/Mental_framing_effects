from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model = 'player'
    form_fields = ['data_priv']

class Results(Page):
    pass

page_sequence = [
    Page1
]
