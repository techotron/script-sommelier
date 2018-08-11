#!/usr/bin/env python

#pip install pyyaml
import yaml
import random
#from collections import Counter
import json

with open(".././conf/recommendations.yml", 'r') as recommend_data:
    try:

        wines_to_suggest = []
        recommends = yaml.load(recommend_data)
        recommends_len = (len(recommends) -1)
        rand_recommend = random.randint(0, recommends_len)
        recommend_desc = recommends[rand_recommend]["description"]
        recommend_tags = recommends[rand_recommend]["tags"]

        suggestion_dict = {
            'sommelier': {'Suggestion': recommend_desc}
        }

        wines_to_suggest.append(suggestion_dict)

        with open(".././conf/wines.yml", 'r') as wine_data:
            try:
                wines_to_return = set([])
                wines = yaml.load(wine_data)

                for wine in wines:
                    for tag in wine["tags"]:
                        if tag in recommend_tags:
                            wines_to_return.add(wine["index"])

                for wine_suggestion in list(wines_to_return):

                    wine_dict = {'wines': {
                        'Name': wines[wine_suggestion]["name"],
                        'Origin': wines[wine_suggestion]["origin"],
                        'Label': wines[wine_suggestion]["label"],
                        'Cost': wines[wine_suggestion]["cost"],
                        'Grape': wines[wine_suggestion]["grape"],
                        'Year': wines[wine_suggestion]["year"],
                        'Description': wines[wine_suggestion]["desc"],
                        'ImageUrl': wines[wine_suggestion]["url"]
                    }}

                    wines_to_suggest.append(wine_dict)

                json_return = (json.dumps(wines_to_suggest))
                print json_return

            except yaml.YAMLError as wine_exception:
                print(wine_exception)

    except yaml.YAMLError as rec_exception:
        print(rec_exception)