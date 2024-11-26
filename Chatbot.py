import nltk
from nltk.chat.util import Chat, reflections

# Ensure required NLTK packages are downloaded
nltk.download('punkt')

# Define chatbot pairs (patterns and responses)
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?"]],
    [r"what is your name\??", ["I'm a chatbot created using NLTK."]],
    [r"how are you\??", ["I'm just a program, but I'm here to help you!"]],
    [r"tell me about (.*)", ["Sure! What would you like to know about %1?"]],
    [r"quit", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Can you rephrase?"]],
]

# Create chatbot with reflections for better conversational flow
chatbot = Chat(pairs, reflections)

# Start the chatbot
def start_chatbot():
    print("Hi, I'm your chatbot! Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chatbot()
