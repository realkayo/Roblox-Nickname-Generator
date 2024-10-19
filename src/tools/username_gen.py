from src.functions.is_username_taken import is_username_taken
from src.functions.text_contains_profanity import contains_profanity
from faker import Faker

fake = Faker(['en_US'])

def gen(amount: int):
    if not amount:
        amount = 1
    generated_nicks = []
    
    while len(generated_nicks) < amount:
        nick = fake.user_name()
        
        if not contains_profanity(nick) and not is_username_taken(nick):
            generated_nicks.append(nick)
    
    return generated_nicks


