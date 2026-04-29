import random

def evaluate_answer(answer):

    if len(answer) < 20:
        return 4,"Answer is too short."

    elif len(answer) < 60:
        return 6,"Good answer but add more details."

    elif len(answer) < 120:
        return 8,"Good explanation."

    else:
        return 9,"Excellent detailed answer."