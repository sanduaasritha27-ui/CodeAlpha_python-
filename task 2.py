def chatbot():
    print("================================")
    print("      BASIC CHATBOT")
    print("================================")
    print("Type 'hello', 'how are you', 'bye', etc.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks for asking!")

        elif user == "what is your name":
            print("Bot: I am a simple Python Chatbot.")

        elif user == "help":
            print("Bot: You can say 'hello', 'how are you', 'what is your name', or 'bye'.")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()