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
    timings_json = models.LongStringField(blank=True, null=True)

# PAGES
class Introduction(Page):
    pass

class Task(Page):
    @staticmethod
    def live_method(player: Player, data):
        rt = data.get('response_time')
        reactionT = data.get('leave_time')
        idx = str(data.get('trial_index'))

        if idx is None:
            return  # must have trial index

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        # Initialize if not present
        if idx not in existing:
            existing[idx] = {}

        if rt is not None:
            existing[idx]["response_time"] = rt
        if reactionT is not None:
            existing[idx]["reaction_time"] = reactionT

        player.timings_json = json.dumps(existing)

class TaskV2(Page):
    @staticmethod
    def live_method(player: Player, data):
        rt = data.get('response_time')
        reactionT = data.get('leave_time')
        idx = str(data.get('trial_index'))

        if idx is None:
            return  # must have trial index

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        # Initialize if not present
        if idx not in existing:
            existing[idx] = {}

        if rt is not None:
            existing[idx]["response_time"] = rt
        if reactionT is not None:
            existing[idx]["reaction_time"] = reactionT

        player.timings_json = json.dumps(existing)        


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass

page_sequence = [Introduction, TaskV2, ResultsWaitPage, Results]
