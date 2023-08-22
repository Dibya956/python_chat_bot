import random


R_EATING = "I don't like to eating anything because I', a bot obviously!"
R_ADVISE = "Practice more to become pro"


def unknown():
    response = ['Could you please re-phrase that?',
                ".....",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response