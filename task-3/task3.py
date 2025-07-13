import nltk
import random
import string

# Download required NLTK packages
nltk.download('punkt')

# Sample chatbot responses and keywords
chat_pairs = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, how about you?"],
    "what is your name": ["I'm CodTechBot, your internship assistant."],
    "what can you do": ["I can answer basic questions using NLP!", "I'm here to help you with simple queries."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."]
}

# Function to preprocess and clean user input
def preprocess(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

# Function to get a response from the chatbot
def get_response(user_input):
    user_input = preprocess(user_input)
    for key in chat_pairs:
        if key in user_input:
            return random.choice(chat_pairs[key])
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Chat loop
def chatbot():
    print("CodTechBot: Hello! I am your AI Chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("CodTechBot:", random.choice(chat_pairs["bye"]))
            break
        response = get_response(user_input)
        print("CodTechBot:", response)

# Run the chatbot
chatbot()
