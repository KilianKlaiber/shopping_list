import os
from groq import Groq
import database


def main():
    groceries = database.get_availabe_groceries()
    values = guess_grocery(groceries, term="Brie")

    print(values)


def guess_grocery(groceries: str, term: str) -> tuple[str]:

    client = Groq(
        api_key=os.getenv("API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Tell me which of these terms {groceries} is identical with or most closely resembles {term}. Answer with the phrase: Did you  mean ...? Do not add parentheses to the answer. Only return one of the suggested terms, nothing else. ",
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
