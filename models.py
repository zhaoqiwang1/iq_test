from otree.api import (
    models, BaseConstants
)
from otree_markets import models as markets_models
from otree_markets.exchange.base import Order
from .configmanager import ConfigManager


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'iq_test' 
    players_per_group = None
    num_rounds = 1

    config_fields = {
            'test_number': int,
            'answers_1': int , 
            'answers_2': int,
            'answers_3': int, 
            'answers_4': int 
     }
class Subsession(markets_models.Subsession):
    def config(self):
        config_addr = Constants.name_in_url + '/configs/' + self.session.config['config_file']
        return ConfigManager(config_addr, self.round_number, Constants.config_fields)

    def creating_session(self):
        for player in self.get_players():
            player.test_number = self.config.test_number

class Group(markets_models.Group):
    pass


class Player(markets_models.Player):
    
    test_number = models.IntegerField()
    Question_1 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
                )
