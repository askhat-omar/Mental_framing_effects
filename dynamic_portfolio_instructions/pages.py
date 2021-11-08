from otree.api import Currency as c, currency_range

from helpers import get_next_app
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])


page_sequence = [
    Page1
]
