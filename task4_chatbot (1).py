
# Task 4: Basic Chatbot 🤖
# Key Concepts Used: if-elif, functions, loops, input/output

def tiny_chatbot():
    print("Type something to start chatting (type 'bye' to exit)")
    while True:
        msg = input("You: ").lower()
        if msg == "hello":
            print("Bot: Hey there!")
        elif msg == "how are you":
            print("Bot: I'm doing fine, thanks!")
        elif msg == "bye":
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Hmm... I didn't get that.")

tiny_chatbot()
