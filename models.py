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

import random
import numpy as np

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'iq_test' 
    players_per_group = None
    num_rounds = 1
    config = {
            'test_number': 3,
            '1' : [2, 3, 3, 7, 5, 6, 4, 1, 7, 6] , 
            '2' : [6, 1, 2, 1, 7, 3, 4, 6, 5, 2],
            '3' : [3, 1, 3, 8, 2, 8, 8, 8, 5, 2], 
            '4' : [4, 2, 5, 6, 4, 3, 4, 2, 1, 6],
            'points': [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5]
     }
class Subsession(markets_models.Subsession):

    def creating_session(self):
        for player in self.get_players():
            player.test_num = Constants.config['test_number']
            player.Q1_ans = Constants.config[str(player.test_num)][0]
            player.Q2_ans = Constants.config[str(player.test_num)][1]
            player.Q3_ans = Constants.config[str(player.test_num)][2]
            player.Q4_ans = Constants.config[str(player.test_num)][3]
            player.Q5_ans = Constants.config[str(player.test_num)][4]
            player.Q6_ans = Constants.config[str(player.test_num)][5]
            player.Q7_ans = Constants.config[str(player.test_num)][6]
            player.Q8_ans = Constants.config[str(player.test_num)][7]
            player.Q9_ans = Constants.config[str(player.test_num)][8]
            player.Q10_ans = Constants.config[str(player.test_num)][9]

    def set_rankings(self):
        ## get score
        for p in self.get_players():
            p.get_score()
        ##sort score to get ranking 
        rank = []
        for player in self.get_players():
            rank.append(player)
        i = 0
        rand_num = np.random.choice(len(rank),size=(len(rank)),replace=False )
        for player in self.get_players():
            player.rand_id = rand_num[i]
            i=i+1
        
        rank.sort(reverse = True, key = lambda x: (x.score, x.rand_id))
        print(rank)

        n=1
        for i in range(len(rank)):
            rank[i].ranking = n
            n=n+1
            print(rank[i].score)
        for p in self.get_players():
            p.set_global_rankings()
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    rand_id = models.IntegerField(initial=0)
    test_num = models.IntegerField(initial=0)
    score = models.FloatField(initial=0)
    ranking = models.IntegerField(initial=0)
    Q1_ans = models.IntegerField(initial=0)
    Q2_ans = models.IntegerField(initial=0)
    Q3_ans = models.IntegerField(initial=0)
    Q4_ans = models.IntegerField(initial=0)
    Q5_ans = models.IntegerField(initial=0)
    Q6_ans = models.IntegerField(initial=0)
    Q7_ans = models.IntegerField(initial=0)
    Q8_ans = models.IntegerField(initial=0)
    Q9_ans = models.IntegerField(initial=0)
    Q10_ans = models.IntegerField(initial=0)
   
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
    def get_score(self):
        question_ans = [self.Q1_ans, self.Q2_ans, self.Q3_ans,self. Q4_ans, self.Q5_ans, self.Q6_ans, self.Q7_ans, self.Q8_ans, self.Q9_ans, self.Q10_ans]
        questions = [self.Question_1, self.Question_2, self.Question_3, self.Question_4, self.Question_5, self.Question_6, self.Question_7, self.Question_8, self.Question_9, self.Question_10]
        i = 0 
        for x in question_ans:
            if questions[i] == x:
                self.score += Constants.config['points'][i]
            i =i+1
        return self.score
    def set_global_rankings(self):
        self.participant.vars['ranking'] = self.ranking