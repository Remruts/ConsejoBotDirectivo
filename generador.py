#-*- coding: utf-8 -*-
import tracery
import json

with open("bot_CD.json", "r") as f:
    rules = json.load(f)

grammar = tracery.Grammar(rules)
print(grammar.flatten("#origin#")[5:-1])


