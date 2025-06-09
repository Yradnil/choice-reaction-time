from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'choiceReactionTask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    timings_json = models.LongStringField(blank=True, null=True)


# PAGES
class CrtOneColor(Page):
    pass

class CrtMultipleColors(Page):
    pass

class CrtRtSart(Page):
    pass

class ReactionTime(Page):
    pass

class Sart(Page):
    pass

class CrtSartDistractor(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [ReactionTime, ResultsWaitPage, Results]
