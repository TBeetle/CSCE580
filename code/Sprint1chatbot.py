#Written by Tyler Beetle
import random
import subprocess 

# All of the responses to user input stored in a list. the input feeds in a key and based off that key the response body is sent back
responses = { 
    # 20 chitchat responses extensible within this list
    "hello" : ["Hello", "Hi there!", "Hey!", "How are you?"],
    "how are you" : ["I am good thank you!", "I am doing well!", "I am a chatbot so I don't feel"],
    "goodbye" : ["See you later", "goodbye!", "Adios!"],
    "weather" : ["I do not know the weather I am a recipe expert!"],
    "name" : ["My name is Miley the Recipe reccomender system", "I am Miley the Recipe wizard"],
    "birthday": ["I do not have a birthday I am a chatbot!"],
    "friend": ["I can be your friend as long as we are talking about food and recipes"],
    "hi": ["Hello there!", "Hey!"],
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

    #Coverage of known query types for recipe reccomender (25 responses)
    
    "easy": ["You should get hello fresh if you want easy recipes!"],
    "delicous": ["If you want some delicious recipes you should try cooking this homemade buffalo chicken dip! What meats do you like?"],
    "chicken": ["You should make my chicken salad recipe, it is quick, easy, and stores well"],
    "beef": ["You should try my beef tacos based on the Cantina 76 recipe"],
    "vegetarian": ["You should try my vegetable pasta recipe", "Try tofa stir fry recipe!"],
    "fish": ["What type of fish?"],
    "salmon": ["Try my lemon pepper salmon recipe"],
    "tilapia": ["Try my tilapia pasta dish"],
    "swordfish": "Try to swordfish steak recipe",
    "iron" : ["If you have low iron you should eat more red meat and tuna!"],
    "vitamin c" : ["Drink more orange juice", "Take some supplements"],
    "pottasium" : ["You need to eat more bananas"],
    "girlfriend": "If you are trying to impress a girlfriend, you should make a chicken pesto dish with some vegetables",
    "diabetic": "Low sugar is the move for you! I would focus on high protein meals like a chicken pot pie",
    "lose weight": "I would reccomend some of the weight watcher recipes I have",
    "gain weight": "You definetly need to carb load with things like pasta and rice",
    "quick" : ["Two quick recipes are making ramen and frozen meals!", "If you like quick food you probably don't have time to cook!"],
    "healthy" : ["You should definetly stock up on fruits and vegetables if you want to be healthy!", "Try the keto diet!"],
    "soup": ["Try my chicken noodle soup recipe", "Lentil soup is a healthy option"],
    "dessert": ["For dessert, you can try my chocolate lava cake recipe", "How about some apple pie?"],
    "breakfast": ["A classic breakfast choice is scrambled eggs with bacon", "Pancakes with maple syrup are a great breakfast option"],
    "vegetables": ["You should include more leafy greens like spinach and kale in your diet", "Roasted Brussels sprouts make for a delicious side dish"],
    "spaghetti": ["Spaghetti carbonara is a classic Italian dish you can try", "Make a simple tomato and basil pasta for a quick meal"],
    "grill": ["Grilled chicken with barbecue sauce is a fantastic choice for outdoor cooking", "Try grilling some vegetables for a healthy side dish"],
    "baking": ["Baking homemade bread can be a fun and rewarding experience", "Chocolate chip cookies are always a crowd-pleaser when baking"],
    "fancy": ["If you are making a fancy dish, it is all in the sauce and moisture!"],

# This handles the case where the user input is not recognized with one of the responses
    "unknown" : ["I do not know this information"]
}

#chat() initialized the system and runs until the user decides to quit. It feeds the user input to the chat_response to find a key value pair that is similar
def chat():
    file_path = "terminal_session.txt"
    script_process = subprocess.Popen(["script", "-q", file_path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print("ChatBot: Hello and welcome to the recipe reccomender system!\nPlease give me some adjetives that describe your desired eating habits.\nType quit to exit.")
    while True: 
            user_message = input("You: ")
            if user_message.lower in ['quit','exit','goodbye', 'q']:
                print("ChatBot: Goodbye! ")
                break
            responses = chat_response(user_message)
            print("ChatBot: ", responses)
            script_process.stdin.write(f"ChatBot: {responses}\n")
            script_process.stdin.flush
    script_process.stdin.close()

#chat_response takes in the user_message system and references a key in the responses. If nothing is found, then it will match to the unknown key.
def chat_response(user_message):
    user_message = user_message.lower()

    for key in responses:
        if key in user_message:
            return random.choice(responses[key])
    return random.choice(responses["unknown"])

#main 
if __name__ == "__main__":
    chat()