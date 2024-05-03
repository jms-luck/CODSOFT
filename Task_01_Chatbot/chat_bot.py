exit={"bye","quit","end","stop","terminate"}
def response(chat):    
        if "hi" in chat:
            return "Hello! How can I'm here to help you today?"
        elif "how are you" in chat:
            return "I'm just a chatbot, but doing well What about you!"
        elif "help" in chat:
            return "Sure, I'm here to help. What do you need assistance with?"
        elif "welcome" in chat:
            return "Welcome! How can I assist you today?"
        elif "hey" in chat:
            return "Hey there! What can I do for you?"
        elif "greetings" in chat:
            return "Greetings! How may I be of service?"
        elif "what brings you here" in chat:
            return "Hello! What brings you here?"
        elif "need a hand" in chat:
            return "Hi! Need a hand with something?"
        elif "ready to tackle" in chat:
            return "Hi! Let's see how I can assist you today."
        else:
            return "I'm sorry, I didn't understand that. Can you please try again?"
try:    
    print("Welcome to the Chatbot!!!")
    while True:
        user_input =input("You: ")
        chat=user_input.lower()
        if chat in exit:
            print("Chat Ended Thank you, Have a Great Day!!")
            break
        else:
            responsed= response(chat)
            print("Bot:", responsed)

except:
    print("Bot: I may be out of servise???")
