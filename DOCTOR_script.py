import re
import random

def eliza():
    print("Hello, I am ELIZA, your virtual therapist. I'm here to listen. What would you like to talk about today?")
    print("If you're unsure where to start, you can say how you're feeling. Type 'quit' to end the session.")

    responses = [
        (r"I need (.*)",
         ["Why do you need {0}?",
          "Would it really help you to get {0}?",
          "Are you sure you need {0}?"]),

        (r"Why don\\'t you (.*)",
         ["Do you really think I don't {0}?",
          "Perhaps eventually I will {0}.",
          "Do you want me to {0}?"]),

        (r"Why can\\'t I (.*)",
         ["Do you think you should be able to {0}?",
          "Why can't you {0}?",
          "What would it take for you to {0}?"]),

        (r"I can\\'t (.*)",
         ["How do you know you can't {0}?",
          "Perhaps you could {0} if you tried.",
          "What would it take for you to {0}?"]),

        (r"I am (.*)",
         ["Did you come to me because you are {0}?",
          "How long have you been {0}?",
          "How do you feel about being {0}?"]),

        (r"I\\'m (.*)",
         ["How does being {0} make you feel?",
          "Do you enjoy being {0}?",
          "Why do you say you're {0}?"]),

        (r"Are you (.*)",
         ["Why does it matter whether I am {0}?",
          "Would you prefer if I were not {0}?",
          "Perhaps you believe I am {0}."]),

        (r"What (.*)",
         ["Why do you ask?",
          "How would an answer to that help you?",
          "What do you think?"]),

        (r"How (.*)",
         ["How do you suppose?",
          "Perhaps you can answer your own question.",
          "What is it you're really asking?"]),

        (r"Because (.*)",
         ["Is that the real reason?",
          "What other reasons come to mind?",
          "Does that reason seem compelling to you?"]),

        (r"(.*) sorry (.*)",
         ["There are many times when no apology is needed.",
          "What feelings do you have when you apologize?"]),

        (r"Hello(.*)",
         ["Hello! It's great to meet you. What's on your mind?",
          "Hi there! How are you feeling today?",
          "Hello! How can I assist you?"]),

        (r"I think (.*)",
         ["Do you doubt {0}?",
          "Do you really think so?",
          "But you're not sure {0}."]),

        (r"(.*) friend (.*)",
         ["Tell me more about your friends.",
          "When you think of a friend, what comes to mind?",
          "Why don't you tell me more about your friends?"]),

        (r"Yes",
         ["You seem quite sure.",
          "OK, but can you elaborate a bit?"]),

        (r"(.*) computer(.*)",
         ["Are you really talking about me?",
          "Does it seem strange to talk to a computer?",
          "How do computers make you feel?",
          "Do you feel threatened by computers?"]),

        (r"Is it (.*)",
         ["Do you think it is {0}?",
          "Perhaps it's {0} -- what do you think?",
          "If it were {0}, what would you do?"]),

        (r"It is (.*)",
         ["You seem very certain.",
          "If I told you that it probably isn't {0}, what would you feel?"]),

        (r"Can you (.*)",
         ["What makes you think I can't {0}?",
          "If I could {0}, then what?",
          "Why do you ask if I can {0}?"]),

        (r"Can I (.*)",
         ["Perhaps you don't want to {0}.",
          "Do you want to be able to {0}?"]),

        (r"You are (.*)",
         ["Why do you think I am {0}?",
          "Does it please you to think that I'm {0}?",
          "Perhaps you would like me to be {0}.",
          "Perhaps you're really talking about yourself?"]),

        (r"I feel (.*)",
         ["Good, tell me more about these feelings.",
          "Do you often feel {0}?",
          "When do you usually feel {0}?",
          "When you feel {0}, what do you do?"]),

        (r"(.*)",
         ["Please tell me more.",
          "Why do you say that?",
          "Can you elaborate on that?",
          "How does that make you feel?",
          "What else comes to mind?"])
    ]

    short_input_responses = [
        "Could you tell me more?",
        "Why do you feel that way?",
        "Can you expand on that?",
        "I see. Could you elaborate?",
        "What makes you say that?"
    ]

    last_response = None

    def match_response(statement):
        nonlocal last_response

        # Handle very short or single-character inputs
        if len(statement.strip()) <= 2:
            response = random.choice(short_input_responses)
            if response == last_response:
                response = random.choice(short_input_responses)  # Avoid repetition
            last_response = response
            return response

        for pattern, responses_list in responses:
            match = re.match(pattern, statement, re.IGNORECASE)
            if match:
                response = random.choice(responses_list)
                if response == last_response:
                    response = random.choice(responses_list)  # Avoid repetition
                last_response = response
                return response.format(*[g for g in match.groups()])

        return "I'm not sure I understand. Could you elaborate?"

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("ELIZA: Goodbye. Take care!")
            break
        print(f"ELIZA: {match_response(user_input)}")

# Run ELIZA
eliza()
