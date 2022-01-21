import random
name="Sofia Silva"
question="Will I be lucky today?"
answer=" "
random_number=random.randint(1,9)
print(random_number)

#logic
if random_number==1:
  answer="Yes-definately."
elif random_number==2:
  answer="It is decidedly so."
elif random_number==3:
  answer="Without a doubt."
elif random_number==4:
  answer="Reply,hazy,try again."
elif random_number==5:
  answer="Ask again later."
elif random_number==6:
  answer="Better not tell you now."
elif random_number==7:
  answer="My sources say no."
elif random_number==8:
  answer="Outlook not so good."
elif random_number==9:
  answer="Very doubtful."
else:
  answer="Error, out of range."

#Output
print(name+" asks: "+question)
print("Magic 8-Ball's answer: "+ answer)

"""
OUTPUT SAMPLE (One of 9 possible):
4
Sofia Silva asks: Will I be lucky today?
Magic 8-Ball's answer: Reply,hazy,try again.

"""
