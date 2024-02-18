import spacy
from nltk.chat.util import Chat, reflections

# Load the English language model for spacy
nlp = spacy.load("en_core_web_sm")

patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I\'m doing well, how about you?']),
    (r'(.*) your name', ['I am a chatbot created with NLTK and Spacy.', 'You can call me Chatbot.']),
    (r'(.*) (good|well|fine)', ['That\'s great!', 'I\'m glad to hear that.']),
    (r'(.*) (help|assist|support)', ['Sure, I can help you. Just ask me anything.']),
    (r'bye|quit', ['Goodbye!', 'Bye. Have a great day!']),

    # Additional dummy patterns and responses
    (r'(.*) age', ['I am a computer program, so I don\'t have an age.']),
    (r'(.*) weather', ['I don\'t have real-time weather information, but you can check a weather website.']),
    (r'(.*) (favorite color|favourite colour)', ['I don\'t have a favorite color.']),
    (r'(.*) (joke|funny)', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'(.*) (movie|film)', ['I don\'t watch movies, but I can recommend a good book!']),
    (r'(.*) (sport|game)', ['I\'m not into sports, but I can help you find information about your favorite team.']),
    (r'(.*) (news|latest news)', ['I don\'t have real-time news, but you can check a news website for the latest updates.']),
    (r'(.*) (tell me about yourself)', ['I am a chatbot designed to assist with basic questions and engage in conversations.']),
]


class AdvancedChatbot:
    def __init__(self, patterns, reflections):
        self.chatbot = Chat(patterns, reflections)

    def process_entities(self, user_input):
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def respond(self, user_input):
        entities = self.process_entities(user_input)
        response = ""

        chatbot_response = self.chatbot.respond(user_input)
        if chatbot_response is not None:
            response += chatbot_response

        if entities:
            entity_str = ', '.join([f"{text} ({label})" for text, label in entities])
            if response:
                response += f" I detected the following entities: {entity_str}."
            else:
                response = f"I detected the following entities: {entity_str}."

        print(f"Final response: {response}")  # Add this line for debugging
        return response



# Instantiate the chatbot
advanced_chatbot = AdvancedChatbot(patterns, reflections)
