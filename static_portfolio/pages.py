from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Static(Page):
    form_model = 'player'
    form_fields = ['lottery']



page_sequence = [Static]
