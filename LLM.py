import getpass
import os

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = "MY_API_KEY"


from langchain_groq import ChatGroq

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    # max_tokens=None,
    # reasoning_format="parsed",
    # timeout=None,
    # max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Spanish. Translate the user sentence.",
    ),
    ("human", "Good Morning! how are you ?."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)