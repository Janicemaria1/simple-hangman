import random 

possibleAnswers = ['PYTHON', 'JAVASCRIPT', 'INFINITYWAR', 'ENDGAME', 'SUNFLOWER', 'HIBISCUS', 'HISTORICAL']

random.shuffle(possibleAnswers)
ans = list(possibleAnswers[1])

display = []
display.extend(ans)

for i in range(len(display)):
	display[i] = "_"

print('topic is random ')

print(' '.join(display))
print ("\n\n\n\n")

count = 0

while count < len(ans):
	guess = input('guess the letter: ')
	guess = guess.upper()
	
	for i in range(len(ans)):
		if ans[i] == guess:
			display[i] = guess
			count+=1
	
	print(' '.join(display))
	print('\n\n\n\n')
	
print('good job! well done')
