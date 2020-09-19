#-*- coding: utf-8 -*-
import tracery
from tracery.modifiers import base_english
import json

with open("bot_CD.json", "r") as f:
    rules = json.load(f)

grammar = tracery.Grammar(rules)
print(grammar.flatten("#origin#")[5:-1])


