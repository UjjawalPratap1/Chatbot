import openai

# Set your API key (replace with your actual key)
openai.api_key = 'your-api-key-here'

def chat_with_bot(prompt):
    try:
        # Make an API request to OpenAI's GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use other engines like 'gpt-4' or 'gpt-3.5-turbo'
            prompt=prompt,
            max_tokens=150,  # Limit the length of the response
            n=1,  # Get one response
            stop=None,  # You can specify stopping tokens if needed
            temperature=0.7  # Controls randomness of the output (0 to 1)
        )

        # Extract and return the response from the API
        return response.choices[0].text.strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get the chatbot's response
        bot_response = chat_with_bot(user_input)
        if bot_response:
            print(f"Bot: {bot_response}")
