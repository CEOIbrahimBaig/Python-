
blocked_words = {"winner", "free", "money", "claim"}



email = {
    "sender": "lottery-bot@scam.com",
    "subject": "You won a prize!",
    "body": "Congratulations, you are the lucky winner of a brand new car! Click here to claim your money."
}

# 3. Clean up the email text to check for spam
# We convert the body to lowercase and split it into individual words
email_words = email["body"].lower().split()

# 4. Check if any word in the email matches our blocked words list
is_spam = False
for word in email_words:
   
    cleaned_word = word.strip(".,!?") 
    
    if cleaned_word in blocked_words:
        print(f"🚨 ALERT: Found blocked word '{cleaned_word}'")
        is_spam = True



if is_spam:
    print("STATUS: Email sent to SPAM folder.")
else:
    print("STATUS: Email is safe.")