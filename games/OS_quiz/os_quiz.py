import sys

def answer(num):
	d = {
	
	}
	return d[num]

def questions(num):
	lst = [
		
	]
	return lst[num][0]

def main():
	wrong_ans = []

	print("This is a multiple choice quiz. Good Luck.\n")

	num = 0
	while num < 24:
		print("Question "+str(num+1)+":")
		print(questions(num))	#print question

		while True:		#check input if you input a b c or d
			ans = input()
			ans = ans.lower()
			if ans in "abcd":
				break
			print("please only input the letters a, b, c or d\n")
		print("")

		q_lst = questions(num).split("\n")
		q_ans = answer(num)
		print("")
		for a in q_lst:
			if a[0:2] == q_ans+".":
				q_ans = a


		if ans == answer(num):
			print("Correct!, The answer was")
		else:
			print("Wrong you Loser!, the answer was")
			wrong_ans.append("\n".join([("Question "+str(num)),q_lst[0],q_ans]))
		print(q_ans)
		print("")
		num +=1

	if len(wrong_ans) == 0:
		print("Congradulations, You got everything Correct")
	else:
		print("You got", 24-len(wrong_ans), "questions right\n")
		print("Your Wrong Answers Were-------------------------------------\n")

	for f in wrong_ans:
		print(f)
		print("")

	print("Tapos. Dale is awesome")

if __name__ == '__main__':
	main()
