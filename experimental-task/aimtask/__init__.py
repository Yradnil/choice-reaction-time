from otree.api import *
import json

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'aimtask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # store a JSON‐encoded list of all reaction times (in milliseconds)
    response_times_json = models.LongStringField(blank=True, null=True)

# PAGES
class Introduction(Page):
    pass

class Task(Page):
    @staticmethod
    def live_method(player: Player, data):
        rt = data.get('response_time')
        if rt is None:
            return

        # Safely get the current value of the field
        raw_json = player.field_maybe_none('response_times_json')

        try:
            existing = json.loads(raw_json) if raw_json else []
        except json.JSONDecodeError:
            existing = []

        existing.append(rt)
        player.response_times_json = json.dumps(existing)


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass

page_sequence = [Introduction, Task, ResultsWaitPage, Results]
