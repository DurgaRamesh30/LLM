import os
from langchain_groq import ChatGroq


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY","MY_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,  
)

user_input = input("Ask a question about Spider-Man: ")

messages = [
    (
        "system",
        "You are a restricted assistant.\n"
        "You may ONLY answer questions that are about Spider-Man.\n"
        "This includes Spider-Man characters, stories, movies, comics, or abilities.\n\n"
        "If the question is NOT about Spider-Man or related topics, "
        "you MUST reply with exactly:\n"
        "I don't know\n\n"
        "Do not explain your decision.\n"
        "Do not add extra words."
    ),
    ("human", user_input),
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)
