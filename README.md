# ELIZA - Virtual Therapist

ELIZA is a Python-based virtual therapist that engages users in text-based conversations using pattern matching. Inspired by the original ELIZA program created by Joseph Weizenbaum in the 1960s, this implementation serves as a modern, interactive chatbot for exploring thoughts and emotions.

---

## Features

- **Interactive Conversations**: Responds to user input with thoughtful, dynamic replies.
- **Pattern Matching**: Uses `re` (regular expressions) to identify patterns in user input.
- **Natural Interaction**: Provides varied responses to avoid repetition and encourage elaboration.
- **Short Input Handling**: Handles minimal or unclear inputs gracefully.
- **Continuous Engagement**: Keeps the conversation going until the user types `quit`.

---

## How to Run

### Prerequisites

- Python 3.7 or higher
- Basic knowledge of running Python scripts

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Real-J/eliza-virtual-therapist.git
   ```
2. Navigate to the project directory:
   ```bash
   cd eliza-virtual-therapist
   ```
3. Run the script:
   ```bash
   python eliza.py
   ```

4. Start chatting with ELIZA!

---

## Example Interaction

```
Hello, I am ELIZA, your virtual therapist. I'm here to listen. What would you like to talk about today?
If you're unsure where to start, you can say how you're feeling. Type 'quit' to end the session.

You: I feel stressed.
ELIZA: Do you often feel stressed?

You: Yes.
ELIZA: OK, but can you elaborate a bit?

You: I think work is overwhelming me.
ELIZA: Do you doubt work is overwhelming you?
```

---

## How It Works

The script uses regular expressions to match user input against predefined patterns. For each matched pattern, ELIZA provides one of several possible responses, dynamically substituting placeholders with user-provided details.

**Key Components**:
- **`responses`**: A list of patterns and their corresponding responses.
- **`match_response()`**: Matches user input with patterns and generates a response.
- **Dynamic Placeholder Replacement**: Captures parts of user input to customize responses.

---

## Future Enhancements

- **Memory Feature**: Retain context of previous interactions for deeper conversations.
- **Sentiment Analysis**: Adjust responses based on the user's emotional tone.
- **GUI Interface**: Create a graphical user interface for a more user-friendly experience.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Inspired by the original ELIZA program by **Joseph Weizenbaum**.
- Developed using Python's `re` module for pattern matching.

---

Feel free to share your thoughts and ideas for improving ELIZA. Enjoy chatting with your virtual therapist!

