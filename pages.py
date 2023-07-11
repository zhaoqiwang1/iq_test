from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class welcome(Page):
	pass
#	def before_next_page(self):
#		self.player.save()
class Question_1(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_1.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_1']

class Question_2(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_2.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_2']

class Question_3(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_3.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_3']
class Question_4(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_4.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_4']

class Question_5(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_5.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_5']

class Question_6(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_6.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_6']
class Question_7(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_7.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_7']

class Question_8(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_8.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_8']

class Question_9(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_9.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_9']

class Question_10(Page):
	def get_timeout_seconds(self):
		return 75
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.save()
	def vars_for_template(self):
		Q_url = '/static/iq_test/sample_{index}/sample_{index}/Q_10.PNG'.format(index = self.player.test_num)

		return {
			'Q': Q_url
		  }
	form_model = 'player'
	form_fields = ['Question_10']
class done(Page):
	pass
#	def before_next_page(self):
#		self.player.save()
		
class Wait_final(WaitPage):
    wait_for_all_groups = True
    
    after_all_players_arrive = 'set_rankings'
page_sequence = [welcome,Question_1,Question_2, Question_3, Question_4, Question_5, Question_6, Question_7, Question_8, Question_9, Question_10, done, Wait_final]
