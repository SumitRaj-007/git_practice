email_one = open("/home/sumit/Desktop/git_practice/PYTHON/Resources/email_one.txt","r").read()
email_two = open("/home/sumit/Desktop/git_practice/PYTHON/Resources/email_two.txt","r").read()
email_three = open("/home/sumit/Desktop/git_practice/PYTHON/Resources/email_three.txt","r").read()
email_four = open("/home/sumit/Desktop/git_practice/PYTHON/Resources/email_four.txt","r").read()
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
def censor(email,word1):
	email_lower=email.lower()
	torepla_lower=word1.lower()
	censored_mail=email_lower.replace(torepla_lower,"#####")
	return censored_mail
#print(censor(email_one,"learning algorithms"))
def censor2(email,word_list=proprietary_terms):
	a=email
	for words in word_list:
		a=censor(a,words)
	return a

#print(censor2(email_two,proprietary_terms))
def censor3(email, negative_list=negative_words):
	a=censor2(email)

	a=censor2(a,negative_list)
	return a


#print(censor3(email_three, negative_words))
def censor4(email):
	