from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from otree_markets import models as markets_models
from .configmanager import ConfigManager


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'iq_test' 
    players_per_group = None
    num_rounds = 1
    config = {
            'test_number': 1,
            '1' : [2, 3, 3, 7, 5, 6, 4, 1, 7, 6] , 
            '2' : [6, 1, 2, 1, 7, 3, 4, 6, 5, 2],
            '3' : [3, 1, 3, 8, 2, 8, 8, 8, 5, 2], 
            '4' : [4, 5, 5, 6, 4, 3, 5, 2, 1, 1]
     }
class Subsession(markets_models.Subsession):

    def creating_session(self):
        for player in self.get_players():
            player.test_num = Constants.config['test_number']
            player.Q1_ans = Constants.config[str(player.test_num)][1]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    test_num = models.IntegerField(initial=0)
    Q1_ans = models.IntegerField(initial=0)
    Question_1 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_2 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_3 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_4 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_5 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_6 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_7 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_8 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_9 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )
    Question_10 = models.IntegerField(
        choices=[1,2,3,4,5,6,7,8],
        label = '''
            Your Choice 
            '''
                )