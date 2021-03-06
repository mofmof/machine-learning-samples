# -*- coding: utf-8 -
from tinydb import TinyDB, Query

def seed():
    db = TinyDB('db/dataset.json')
    db.purge()
    db.insert({'employee_id': 6, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 0, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 6, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 6, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 0, 'day_of_week':1, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':1, 'attend': 0})
    db.insert({'employee_id': 6, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 6, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 0, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':2, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':2, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 3, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 6, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':3, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':3, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 0, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 2, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 4, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 5, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 0, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 1, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 2, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 3, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 4, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 5, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 6, 'day_of_week':4, 'attend': 1})
    db.insert({'employee_id': 0, 'day_of_week':4, 'attend': 0})
    db.insert({'employee_id': 1, 'day_of_week':4, 'attend': 0})
