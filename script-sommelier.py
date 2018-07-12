#!/usr/bin/env python

import yaml
import random

with open("./wines.yml", 'r') as wine_data:
    try:
        wines = yaml.load(wine_data)
        wine_len = (len(wines) -1)
        rand_wine = random.randint(0, wine_len)

        wine_name = wines[rand_wine]["name"]
        wine_orig = wines[rand_wine]["origin"]
        wine_label = wines[rand_wine]["label"]
        wine_cost = wines[rand_wine]["cost"]
        wine_grape = wines[rand_wine]["grape"]
        wine_year = wines[rand_wine]["year"]
        wine_desc = wines[rand_wine]["desc"]
        wine_times_used = wines[rand_wine]["meta"]["times_used"]

        print wine_name
        print wine_orig
        print wine_label
        print wine_cost
        print wine_grape
        print wine_year
        print wine_desc

    except yaml.YAMLError as exception:
        print(exception)