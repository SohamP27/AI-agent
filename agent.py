def chatbot():
    print("=== Simple AI Chatbot ===")
    print("Type 'bye' to exit.")

    responses = {
        "hello": "Hello! Nice to meet you.",
        "hi": "Hi! How can I help you?",
        "name": "I am a simple AI agent.",
        "help": "You can say hello, ask my name, or say bye."
    }

    while True:
        user = input("You: ").lower().strip()

        if user == "bye":
            print("Agent: Goodbye!")
            break

        found = False

        for keyword in responses:
            if keyword in user:
                print("Agent:", responses[keyword])
                found = True
                break

        if not found:
            print("Agent: Sorry, I don't understand.")


chatbot()
