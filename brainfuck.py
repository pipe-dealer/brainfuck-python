#BRAINFUCK COMPILER IN PYTHON

import os
import time

c = [0,0,0,0,0]
empty = [0]
final = []

count = 0
value = 0

def clear():
    os.system('cls')

clear()

print(c)
print(f"NO. of containers: {len(c)}")
print(f"CURRENT BLOCK {count+1}")
print(*final, sep="")



while True:
	user = str(input("ENTER: "))
	#reset data
	if user == "cls":
		c = [0,0,0,0,0]
		final = []
		count = 0
	#refer to commands
	if user == "help":
		print("""">" = moves pointer one block to the right
	"<" = moves pointer one block to the left
	"+" = increases the value stored in the block by one
	"-" = decreases the value stored in the block by one
	"[" = while current_block != 0
	"]" = if current_block != 0, jump back to [
	"," = inputs one character
	"." = prints one character""")

	#self-explanatory
	if user == "exit":
		exit()

	for i in user:
		#loops
		if i == "[":
			pos1 = user.find("[")
			pos2 = user.find("]")
			loop_pos = count
			while c[count] != 1:
				#only runs the commands inside the brackets
				for x in range(pos1, pos2+1):
					#if current container is zero, remove all commands and exit the loop
					if c[count] == 1:
						for u in range(pos1, pos2+1):
							user.replace(user[u],"")
						break

					if user[x] == ">":
						loop_pos += 1
						if loop_pos >= len(c):
							c.extend(empty * ((loop_pos) - (len(c) - 1)))
					elif user[x] == "<":
						loop_pos -= 1
					elif user[x] == "+":
						c[loop_pos] += 1
					elif user[x] == "-":
						c[loop_pos] -= 1
						if c[loop_pos] < 0:
							print("ERROR: VALUE DOES NOT FIT IN CONTAINER")
							c[loop_pos] = 0
							time.sleep(1)
					elif user[x] == ",":
						try:
							get_input = int(input("ENTER VALUE: "))
							c[loop_pos] = get_input
						except ValueError:
							print("ERROR: UNACCEPTED VALUE")

		#moves pointer to the right
		elif i == ">":
			count += 1
			#adds more containers if pointer position is outside the number of current containers
			if count >= len(c):
				c.extend(empty * ((count) - (len(c) - 1)))
		#moves pointer to the left
		elif i == "<":
			count -= 1
		#adds one to the current container
		elif i == "+":
			c[count] += 1
		#subtracts one from the current container
		elif i == "-":
			c[count] -= 1
			#if value is below zero, set it to zero
			if c[count] < 0:
				print("ERROR: VALUE DOES NOT FIT IN CONTAINER")
				c[count] = 0
				time.sleep(1)
		#displays the ASCII value in the current container
		elif i == ".":
			final.append(chr(c[count]))
		#gets input from user and add it to current container
		elif i == ",":
			try:
				get_input = int(input("ENTER VALUE: "))
				c[count] = get_input
			except ValueError:
				print("ERROR: UNACCEPTED VALUE")



	clear()
	
	print(c)			
	print(f"NO. of containers: {len(c)}")
	print(f"BLOCK {count+1}")
	print(*final, sep = "")
	final = []


