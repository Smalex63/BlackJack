import random
import time


money_pl1 = 1000
money_pl2 = 1000
bet = 0

def cards():
	nums = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
	random.shuffle(nums)
	return nums


class Player:
	def __init__(self, name, count):
		self.name = name
		self.count = count
		

pl_name = input('Здравствуйте! Введите Ваше имя: ')
pl1 = Player('Крупье', 0)
pl2 = Player(pl_name, 0)

def playGame(nums):
	global money_pl1
	global money_pl2
	global bet
	num = nums.pop()
	print(f'\nСчёт: \n\n {pl1.name}: {money_pl1} | {pl2.name}: {money_pl2}\n')
	print(f'{pl2.name}, добро пожаловать в игру "BlackJack"!')
	print(f'На вашем счёте {money_pl2} рублей.')
	while True:
		try:
			bet = int(input(f'Какую ставку вы хотите сделать? Введите число от 1 до {money_pl2}: '))
			if bet < 1 or bet > money_pl2:
				print('Введите корректную сумму.')
			elif bet > money_pl1:
				print(f'У {pl1.name} только {money_pl1} рублей. Введите сумму, не превышающую {money_pl1}.')
			else:
				break
		except ValueError:
			print(f'{pl2.name}, пожалуйста, введите ЧИСЛО.')
	money_pl1 -= bet
	money_pl2 -= bet
	
	print(f'\nСчёт: \n\n {pl1.name}: {money_pl1} | {pl2.name}: {money_pl2}\n')
	print(f'На кону {bet * 2}.')
	print(f'{pl1.name} тянет карту. Ему выпадает {num}.')
	num = nums.pop()
	print(f'Вам, {pl2.name}, достаётся {num}.')
	pl1.count += num
	pl2.count += num
	while True:
		num = nums.pop()
		choise = input(f'{pl2.name}, Вы будете тянуть карту? (д/н): ')
		if choise == 'д':
			pl2.count += num
			if pl2.count > 21:
				print(' ')
				print(f'{pl2.name}, Вы вытянули {num}. У вас {pl2.count} очков. Это перебор. К сожалению, Вы проиграли.')
				money_pl1 += bet * 2
				bet = 0
				gameAgain()
			elif pl2.count == 21:
				print(' ')
				print(f'{pl2.name}, Вы вытянули {num}. У вас {pl2.count} очков. Поздравляем! Вы выиграли!')
				money_pl2 += bet * 2
				bet = 0
				gameAgain()
			else:
				print(' ')
				print(f'{pl2.name}, Вы вытянули {num}. У вас {pl2.count} очков.')
		else:
			counting(cards())
			break
	
	
def counting(nums):
	global money_pl1
	global money_pl2
	global bet
	while True:
		num = nums.pop()
		if pl1.count < 17:
			print(' ')
			print(f'У {pl1.name} {pl1.count} очков. {pl1.name} тянет карту. Это карта {num}.')
			pl1.count += num
			time.sleep(3)
		elif pl1.count >= 17 and pl1.count <= 21:
			if pl1.count >= pl2.count:
				print(' ')
				print(f'У {pl1.name} {pl1.count} очков. {pl1.name} выиграл!')
				money_pl1 += bet * 2
				bet = 0
				gameAgain()
			else:
				print(' ')
				print(f'У {pl1.name} {pl1.count} очков. {pl1.name} тянет карту. Это карта {num}.')
				pl1.count += num
		else:
			print(' ')
			print(f'У {pl1.name} {pl1.count}. Это перебор. {pl2.name}, поздравляем! Вы выиграли!')
			money_pl2 += bet * 2
			bet = 0
			gameAgain()
		
def gameAgain():
	print(' ')
	if money_pl2 > 0 and money_pl1 > 0:
		newGame = input('Хотите сыграть ещё? (д/н): ')
		if newGame == 'д':
			pl1.count = 0
			pl2.count = 0
			playGame(cards())
		else:
			print(f'\nСчёт: \n\n {pl1.name}: {money_pl1} | {pl2.name}: {money_pl2}\n')
			quit()
	elif money_pl1 == 0:
		print(f'{pl2.name}, у {pl1.name} закончились деньги. Поздравляем, вы выиграли!')
		quit()
	else:
		print('У вас закончились деньги. Игра окончена.')
		quit()
	
	
if __name__ == '__main__':
	playGame(cards())





