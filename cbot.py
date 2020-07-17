import re
import random
import mysql.connector
import pandas as pd
class text:
    class Chat(object):

        def __init__(self, pairs, reflections={}):
            self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
            self._reflections = reflections
            self._regex = self._compile_reflections()

        def _compile_reflections(self):
            sorted_refl = sorted(self._reflections, key=len, reverse=True)
            return re.compile(r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE)

        def _substitute(self, str):
            return self._regex.sub(lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower())

        def _wildcards(self, response, match):
            pos = response.find("%")
            while pos >= 0:
                num = int(response[pos + 1 : pos + 2])
                response = (response[:pos]+ self._substitute(match.group(num))+ response[pos + 2 :])
                pos = response.find("%")
            return response

        def respond(self, str):
            for (pattern, response) in self._pairs:
                match = pattern.match(str)
                if match:
                    resp = random.choice(response)  # pick a random response
                    resp = self._wildcards(resp, match)  # process wildcards
                    return resp
                    

        def converse(self, str):
            return self.respond(str)

    li=[""]
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="test")
    df = pd.read_sql("SELECT Context, Answer FROM faq", con = mydb)
    list = df.values.tolist()
    for x in range(85):
        li[0]=list[x][1]
        list[x][1]=li
        li=[""]
    chat=Chat(list)
