def username_generator(first_name,last_name):
  if len(first_name)< 3 or len(last_name)<4:
    username=first_name+last_name
    return username
  else:
    username=first_name[:3]+last_name[:4]
    return username

def password_generator(username):
  password=""
  for letters in range(0,len(username)):
    password+=username[letters-1]
  return password

print(username_generator("Sofia","Silva"))
print(password_generator("sofiasilva0223"))

'''
OUTPUT:

SofSilv
3sofiasilva022
'''
