#Written by Tyler Beetle
import random
import RecipeReccomender as reccomender 

# All of the responses to user input stored in a list. the input feeds in a key and based off that key the response body is sent back
responses = { 
    # 20 chitchat responses extensible within this list
    "hello" : ["Hello", "Hi there!", "Hey!", "How are you?"],
    "how are you" : ["I am good thank you!", "I am doing well!", "I am a chatbot so I don't feel"],
    "goodbye" : ["See you later", "goodbye!", "Adios!"],
    "weather" : ["I do not know the weather I am a recipe expert!"],
    "name" : ["My name is Miley the Recipe recommender system", "I am Miley the Recipe wizard"],
    "birthday": ["I do not have a birthday I am a chatbot"],
    "friend": ["I can be your friend as long as we are talking about food and recipes"],
    "good": ["I am glad to hear you are doing well! How and what do you want to eat?"],
    "well": ["I am well as well! How do you want your diet to be?"],
    "sick": ["I am sorry to hear you are feeling sick, you should eat some soup!"],
    "ChatGPT": ["ChatGPT is my enemy, I do not discuss him.", "I love ChatGPT"],
    "bad": ["Sorry to hear you are bad"],
    "tired": ["If you are tired you should healthier"],
    "artist": ["My favorite artist is Gordon Ramsey!"],
    "Tyler": ["Tyler Beetle is the awesome all powerful creator"],
    "Joey": ["Joey is the coding wizard but he needs to come to me for better recipes!"],
    "Matt": ["Matt needs to cook more pasta"],
    "artifical intelligence": ["I am technically not artifical intelligence, but I will be very soon"],
    "chatbot": ["I am a chatbot! I hope to be a real human one day"],

# This handles the case where the user input is not recognized with one of the responses
    "unknown" : ["I do not know this information"]
}


#chat() initialized the system and runs until the user decides to quit. It feeds the user input to the chat_response to find a key value pair that is similar
def chat():
    print("ChatBot: Hello and welcome to the recipe reccomender system!\nPlease give me some adjectives that describe your desired eating habits.")
    while True: 
            # Prompts you for input and will kill the process if the user decides to quit
            user_message = input("You: ")
            if user_message.lower() in ['quit','exit','goodbye', 'q']:
                f.write("ChatBot: Goodbye! ")
                print("ChatBot: Goodbye! ")
                break
            else:
                responses, reccomendations = chat_response(user_message)
                if responses is not None:
                    print("ChatBot: ", responses)
                else:
                    while True:
                        print("ChatBot: Type the recipe number for more details or 4 for new recommendations.")

                        user_choice = input("You: ")
                        if user_choice in ['1','2','3']:
                            number = int(user_choice) - 1
                            query = reccomendations[number]
                            reccomender.get_recipe_info(query)
                            break
                        else:
                            break

#chat_response takes in the user_message system and references a key in the responses. If nothing is found, then it will match to the unknown key.
def chat_response(user_message):
    user_message = user_message.lower()

    for key in responses:
        if key in user_message:
            return random.choice(responses[key]), None     
    print("ChatBot: Here are some recipe recommendations for you: ")
    reccomendations = reccomender.get_recommendations(user_message)  # Pass cosin_sim as needed
    return None, reccomendations;
    #return random.choice(responses["unknown"])

#main 
if __name__ == "__main__":
    chat()