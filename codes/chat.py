# Product and FAQ details
products = {
    "laptop": "We have laptops starting from ₹40,000 to ₹1,20,000. Brands: Dell, HP, Apple, Lenovo.",
    "phone": "We offer smartphones from ₹15,000 to ₹90,000. Brands: Apple, Samsung, Google, OnePlus.",
    "headphones": "Headphones range from ₹4,000 to ₹25,000. Brands: Bose, Sony, Sennheiser.",
    "tv": "TVs are available from ₹20,000 to ₹2,00,000. Brands: Samsung, LG, Sony, TCL."
}

faq_responses = {
    "return policy": "You can return products within 30 days with a receipt.",
    "warranty": "Most products come with a 1-year warranty. Extended warranties are also available.",
    "delivery": "Free delivery for purchases above ₹4,000. Delivery takes 3-5 business days.",
    "payment options": "We accept credit/debit cards, UPI, Paytm, and cash on delivery."
}

# Chatbot response logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "price" in user_input or "cost" in user_input:
        for product in products:
            if product in user_input:
                return products[product]
        return "Please specify the product (laptop, phone, headphones, or TV) you want details about."
    elif "products" in user_input or "items" in user_input:
        return "We offer laptops, phones, headphones, and TVs. Please ask for more details."
    elif "return policy" in user_input:
        return faq_responses["return policy"]
    elif "warranty" in user_input:
        return faq_responses["warranty"]
    elif "delivery" in user_input:
        return faq_responses["delivery"]
    elif "payment" in user_input:
        return faq_responses["payment options"]
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Let me know if there's anything else."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Chat function
def chat():
    print("Chatbot: Hello! Welcome to our store. How can I assist you?")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chat()
