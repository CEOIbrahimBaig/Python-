# Spam messages are Buy Now , Make a lot of money , Subscribe now , Click this 

s1 = "Buy now "
s2= "Make a lot of money"
s3="Subscribe now"
s4="Click this"

message=input("\t Please Enter your Message \n")

if (s1 in message or s2 in message or s3 in message or s4 in message ):
    print("This message is spam ")
else :
    print("This message does not contain any spam words \n")

    