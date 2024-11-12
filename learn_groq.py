import os
from groq import Groq
import database


def main():

    values = guess_grocery("granny smith")
    
    print(values)

def guess_grocery(term: str) -> tuple[str]:
    
    groceries = database.get_availabe_groceries()

    client = Groq(
        api_key=os.getenv("API_KEY"),
    )


    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Tell me which of these terms {groceries} resembles {term}. Answer with the phrase: Did you  mean ...? Do not add parentheses to the answer."
            }
        ],
        model="llama3-8b-8192",
    )

    guess = chat_completion.choices[0].message.content
    
    list_of_words = guess.split()
    
    answer = list_of_words[-1]
    
    answer = answer[:-1]
    
    return guess, answer
    

if __name__ == "__main__":
    main()