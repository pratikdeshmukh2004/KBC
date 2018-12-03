question_list = ["1. what is the full form of MP?","2. what is the full form of MH","3. what is the full form of UP","4. what is the full form of HP","5. How many day in april?","6. how many day in octomber?","7. what is the full form of C.P.U.","8. who is p.m.?","9. when do we celebrate ghandhi's birthday?","10.when we celebrate maharashtra day?","11. when we celebrate teachar day?","12. which is the red planet?","13. who is our precident?","14. how many state in india?","15. what is the full form of w.H.O.?"]
first_option = ["1. madhya pradesh","1. my party","1. moon price","1. uttar pradesh","1. 31","1. 30","1. central unit","1. narendra modi","1. 3 octomber ","1. 1 may ","1. 9 june ","1. sun","1. Ram Nath Kovind","1. 28","1. World Wrestling Entertainment "]
second_option = ["2. himachal pradesh","2. maharashtra","2. him pradesh","2. maharashtra","2. 29","2. 31","2. cem party udya","1. nokiya mobile","2. 15 august ","2. 2 may ","2. 5 September","2. earth","2. Ram Nath govind","2. 29","2. World Wide Web"]
third_option = ["3. my home","3. up down","3. uttar pradesh","3.himachal pradesh","3. 32","3. 32","3. central procesing unit","3. india","3. 2 October ","3. 4 april ","3. 2 octomber","3. venus","3. m k ghandhi","3. 36","3.World Health Organization"]
fourth_option = ["4. himachal pradesh","4. tree","4. america","4. india","4. 30","4. 29","4. center","4. google","4. 8 july 2004","4. 1 january ","4. 5 january","4. Mars","4. narendra modi","4. 40","4. World Wildlife Fund"]
ans_key =[0,1,2,3,3,4,2,3,1,3,1,2,4,1,2,3]
index=0
price = [000,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
while True:
	c=0
	print ("welcome to KBC")
	while index<len(question_list) and index<len(first_option) and index<len(price) and index<len(ans_key):
		print ("						")
		print (question_list[index])
		print ("											")
		print (first_option [index])
		print (second_option[index])
		print (third_option[index])
		print (fourth_option[index])
		index=index+1
		print ("		")
		a=int(input("sahi option daalo?  "))
		print ("							")
		if a==(ans_key[index]):
			print ("@@ Congrats! You win " + str(price[index]) + " RS. ,play next")
			print ("												")
		else:
			print("you loose,please try again.")
			z=input("you want to play again(y or n)")
			if z=="y":
				index=0
				continue
			else:
				break
	else:
		print ("game over you win RS.100000000..")
		z=input("you want to play again(y or n")
		if z=="y":
			continue
		else:
			break
