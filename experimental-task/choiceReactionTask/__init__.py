from otree.api import *
import json
import json


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
    @staticmethod
    def live_method(player: Player, data):
        idx = str(data.get('trial_index'))
        rt = data.get('reaction_time')
        is_correct = data.get('is_correct')
        clicked = data.get('clicked_index')

        if idx is None or rt is None:
            return

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        if idx not in existing:
            existing[idx] = {}

        existing[idx].update({
            'reaction_time': rt,
            'is_correct': is_correct,
            'clicked_index': clicked
        })

        player.timings_json = json.dumps(existing)

class CrtMultipleColors(Page):
    @staticmethod
    def live_method(player: Player, data):
        idx = str(data.get('trial_index'))
        rt = data.get('reaction_time')
        correct = data.get('is_correct')
        clicked = data.get('clicked_index')

        if idx is None or rt is None:
            return

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        if idx not in existing:
            existing[idx] = {}

        existing[idx].update({
            'reaction_time': rt,
            'is_correct': correct,
            'clicked_index': clicked
        })

        player.timings_json = json.dumps(existing)

class CrtRtSart(Page):
    @staticmethod
    def live_method(player: Player, data):
        idx = str(data.get('trial_index'))
        rt = data.get('reaction_time')
        correct = data.get('is_correct')
        clicked = data.get('clicked_index')

        if idx is None or rt is None:
            return

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        if idx not in existing:
            existing[idx] = {}

        existing[idx].update({
            'reaction_time': rt,
            'is_correct': correct,
            'clicked_index': clicked
        })

        player.timings_json = json.dumps(existing)

class ReactionTime(Page):
    @staticmethod
    def live_method(player: Player, data):
        idx = str(data.get('trial_index'))
        rt = data.get('reaction_time')

        if idx is None or rt is None:
            return

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        if idx not in existing:
            existing[idx] = {}

        existing[idx]['reaction_time'] = rt
        player.timings_json = json.dumps(existing)

class Sart(Page):
    @staticmethod
    def live_method(player: Player, data):
        idx = str(data.get('trial_index'))
        rt = data.get('reaction_time')
        correct = data.get('is_correct')

        if idx is None:
            return

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        if idx not in existing:
            existing[idx] = {}

        if rt is not None:
            existing[idx]['reaction_time'] = rt
        existing[idx]['is_correct'] = correct

        player.timings_json = json.dumps(existing)

class CrtSartDistractor(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class CrtOneColorMT(Page):
    @staticmethod
    def live_method(player: Player, data):
        idx = str(data.get('trial_index'))
        rt = data.get('reaction_time')
        mt = data.get('movement_time')
        correct = data.get('is_correct')
        clicked = data.get('clicked_index')

        if idx is None:
            return

        raw = player.field_maybe_none('timings_json')
        try:
            existing = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            existing = {}

        if idx not in existing:
            existing[idx] = {}

        if rt is not None:
            existing[idx]['reaction_time'] = rt
        if mt is not None:
            existing[idx]['movement_time'] = mt
        if correct is not None:
            existing[idx]['is_correct'] = correct
        if clicked is not None:
            existing[idx]['clicked_index'] = clicked

        player.timings_json = json.dumps(existing)

class CrtMultipleColorsMT(Page):
    pass

class CrtRtSartMT(Page):
    pass

class ReactionTimeMT(Page):
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
        
class SartMT(Page):
    pass


page_sequence = [ReactionTimeMT, ResultsWaitPage, Results]
