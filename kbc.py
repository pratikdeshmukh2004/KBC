question_list = ["1. Which country will host the 45th G7 summit 2019?","2. India's first-ever national police museum will establish in which city?","3. Which country's women cricket team has clinched the Asia Cup Twenty-20 tournament 2018?","4.  Who has won the men's singles French Open tennis tournament 2018?","5. How many day in april?","6. how many day in octomber?","7. what is the full form of C.P.U.","8. who is p.m. in india?","9. when do we celebrate ghandhi's birthday?","10.when we celebrate maharashtra day?","11. when we celebrate teachar day?","12. which is the red planet?","13. who is our precident?","14. how many state in india?","15. what is the full form of w.H.O.?"]
first_option = ["1. Italy ","1. Chennai","1. SouthKorea ","1. NovakDjokovic","1. 31","1. 30","1. central unit","1. narendra modi","1. 3 octomber ","1. 1 may ","1. 9 june ","1. sun","1. Ram Nath Kovind","1. 28","1. World Wrestling Entertainment "]
second_option = ["2. Canada","2. Delhi","2. Bangladesh","2. DominicThiem","2. 29","2. 31","2. cem party udya","1. nokiya mobile","2. 15 august ","2. 2 may ","2. 5 September","2. earth","2. Ram Nath govind","2. 29","2. World Wide Web"]
third_option = ["3. Germany","3. Nagpur","3. India","3.RogerFederer","3. 32","3. 32","3. central procesing unit","3. india","3. 2 October ","3. 4 april ","3. 2 octomber","3. venus","3. m k ghandhi","3. 36","3.World Health Organization"]
fourth_option = ["4. France","4. Kolkata","4. Pakistan","4. Rafael Nadal","4. 30","4. 29","4. center","4. google","4. 8 july 2004","4. 1 january ","4. 5 january","4. Mars","4. narendra modi","4. 40","4. World Wildlife Fund"]
ans_key =[4,2,2,3,4,2,3,1,3,1,2,4,1,2,3]
index=0
price = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
checker=False
while True:
	while index<len(question_list):
		print (question_list[index])
		print ()
		print(first_option[index])
		print (second_option[index])
		print (third_option[index])
		print (first_option[index])
		user=int(input("Enter your answer (1,2,3,4) only one"))
		if user==ans_key[index]:
			print ("congrats ! you win %sRs play next question"%price[index])
		else:
			print ("you loose your answer is wrong you win %sRs."%price[index-1])
			checker=True
			break
			print ("")
		index+=1
	if checker:
		play_again=str(input("you wnt to play again(y or n): "))
		if play_again.lower().startswith("n"):
			break
	index=0
