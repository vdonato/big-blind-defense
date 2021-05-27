import random

import streamlit as st
from poker import Card

from strategies import Action, GameState, Player


# If not enough time, just do UTG vs BB
VILLAIN_POSITIONS = (
    "UTG",
    # "HJ", "CO", "BU", "SB"
)

state = st.session_state


def deal_hands():
    deck = [str(c) for c in list(Card)]
    random.shuffle(deck)
    hand1 = f"{deck.pop()} {deck.pop()}"
    hand2 = f"{deck.pop()} {deck.pop()}"
    return hand1, hand2


def new_hand():
    state.actions_this_hand = []
    state.game_state = GameState.START
    state.current_player = Player.VILLAIN
    if "hands_played" in state:
        state.hands_played += 1
    else:
        state.hands_played = 0


if "initialized" not in state:
    state.initialized = True
    new_hand()
    state.mistakes_made = 0


st.write("# Poker Big Blind Defense Preflop Trainer")
st.write(deal_hands())

# TODO: Pick villain position at random (maybe just do BB vs UTG for now)
# TODO: Draw two hands (force villain to have a playable one) and have villain open raise
# TODO: Give player choice to respond (also providing an RNG for convenience)
# TODO: Have villain follow strategy table
# TODO: Repeat until end of hand or player makes a mistake
# TODO: If mistake, tell player how they screwed up
# TODO: Keep track of stats for the practice session
