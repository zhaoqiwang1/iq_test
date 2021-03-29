from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question_1(Page):
  
	def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_1.png'.format(index = self.player.test_num)

	    return {
	      	'Q': Q_url
	      }
	form_model = 'player'
	form_fields = ['Question_1']

class Question_2(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_2.png'

	    return {
	      	'Q': Q_url
	      }

class Question_3(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_3.png'

	    return {
	      	'Q': Q_url
	      }

class Question_4(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_4.png'

	    return {
	      	'Q': Q_url
	      }

class Question_5(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_5.png'

	    return {
	      	'Q': Q_url
	      }

class Question_6(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_6.png'

	    return {
	      	'Q': Q_url
	      }

class Question_7(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_7.png'

	    return {
	      	'Q': Q_url
	      }

class Question_8(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_8.png'

	    return {
	      	'Q': Q_url
	      }

class Question_9(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_9.png'

	    return {
	      	'Q': Q_url
	      }

class Question_10(Page):
    def vars_for_template(self):
	    Q_url = '/static/iq_test/sample_1/sample_1/Q_10.png'

	    return {
	      	'Q': Q_url
	      }

page_sequence = [Question_1]
