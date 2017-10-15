import random
import sys
import time

class Player:
	score = 0
	player_num = None
	
	def __init__(self, player_num = 1):
		self.player_num = player_num
	
	def update_score(self,score):
		self.score = self.score + score
	
	def get_score(self):
		return self.score
	
	def reset_score(self):
		self.score = 0



class pig:
	num_players = None
	game_state = True
	players = []
	game_limit = 100
	
	def __init__(self, num_players = 2):
		self.num_players = num_players
		for i in range(0, num_players):
			self.players.append(Player(i))
		
		play_status = 1
		while(play_status):			
			play_status = self.play()
			
	def play(self):
		current_player = 0
		random.seed(0)
		while(self.game_state):
			self.print_scores()
			current_player = current_player % self.num_players
			dice_rolls = self.roll(current_player)
			if dice_rolls == -1:
				return -1
			if self.players[current_player].get_score() >= self.game_limit:
				sys.stdout.write("\033[F\033[K")
				print "\n ***Game won by Player {} ***\n".format(current_player)
				time.sleep(1)
				sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")
				reset_status = -1
				while(reset_status == -1):
					reset_status = self.reset_game()	
					sys.stdout.write("\033[F\033[K")
				return reset_status
			current_player = current_player + 1
			
	
	def roll(self, player):
		sum_val = 0
		while(True):
			str_out =  "Current Player:{}\tRoll sum:{}\nEnter Choice(r/h):".format(player, sum_val)
			sys.stdout.write(str_out)
			s = raw_input()
			if s == 'r':
				dieroll = (random.randint(1, 100) % 6) + 1
				if dieroll == 1:
					str_out =  "Player {} Rolled a {}\tTurn Over\n".format(player, dieroll)
					sys.stdout.write(str_out)
					time.sleep(0.5)
					sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K")
					return 0
				else:
					sum_val = sum_val + dieroll
					str_out =  "Player {} Rolled a {}\n".format(player, dieroll)
					sys.stdout.write(str_out)
					time.sleep(0.5)
					sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")
					if (self.players[player].get_score() + sum_val) >= self.game_limit:
						self.players[player].update_score(sum_val)
						return sum_val
					
			
			elif s == 'h':
				self.players[player].update_score(sum_val)
				sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")
				return sum_val
			
			else:
				str_out =  "Invalid Command Entered.\n"
				sys.stdout.write(str_out)
				time.sleep(0.5)
				sys.stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")
	
	def print_scores(self):
		str_score = ''
		for i in range(0, self.num_players):
			str_score = str_score + "Player{}:{}\t".format(i, self.players[i].get_score())
		str_score = str_score + '\n'
		sys.stdout.write(str_score)
		
	def reset_game(self):
		sys.stdout.write("Continue the game?(Y/N):")
		cont = raw_input()
		if cont == "Y" or cont == "y":
			for player in self.players:
				player.reset_score()
			return 1
		elif cont == "N" or cont == "n":
			return 0
		else:
			sys.stdout.write("Invalid command.\n")
			time.sleep(0.5)
			sys.stdout.write("\033[F\033[K")
			return -1

if __name__ == "__main__":
	if len(sys.argv) == 3:
		if sys.argv[1] == '--numPlayers':
			pig(int(sys.argv[2]))
		else:
			print "Invalid Commmand"
	else:
		pig()

