import re
import responses as res
import calculations as cal
import webbrowser as web

def message_probability(user_message , recongnised_words,single_response = False , required_words = []):
    message__certanity = 0
    has_required_words = True

    for word in user_message:
        if word in recongnised_words:
            message__certanity += 1
    
    # calculate the percent of recognize words in a user message
    percentage = float(message__certanity)/float(len(recongnised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words == True or single_response:
        return(int(percentage*100))
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response , list_of_words , single_response = False , required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words ,  single_response , required_words)
    
    # Responses
    response('Hello!!',['hello','sup','hey','heyo','hi','hii','heyy','yo','heyoo'], single_response=True)
    response(res.insulin,['insulin','what','is'],single_response=True)
    response(res.type_of_diabetes,['what','are','different','types','type','diabetes','diabities'],single_response=True)
    response(res.blood_sugar_level,['glucose','sugar'],single_response=True)
    response(res.vision,['vision','normal','eye'],single_response=True)
    response(res.nutrition,['what','nutrition'],single_response=True)
    response(res.thanks(),['thanks','thank','you','bye','ok'],single_response=True)
    best_match = max(highest_prob_list , key=highest_prob_list.get)
    # print(highest_prob_list)
    return res.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    # To check all responses
    response = check_all_messages(split_message)
    return response


if __name__ == "__main__":
    # For responses
    print("Dia-bit-bot : Hello, I am Dia-bit-bot I am here to help you up with all your Queries.")
    # print("")
    while(True):
        ques = str(input('You: ')).lower()
        try:
            if 'nutrition' in ques or 'fact' in ques:
                print("Hi!! there what nutrition facts of food you want to know about??")
                print(">> ",end="")
                query = str(input()).lower()
                web.open(f"https://en.wikipedia.org/wiki/{query}")

            elif 'bmi' in ques:
                cal.bmi()

            elif 'symptoms' in ques:
                if(ques == "symptoms"):
                    res.symptoms_input()
                else:
                    query = re.split(r'\s+|[,;?!.-]\s*', ques.lower())
                    res.symptoms(query)

            else:
                print('Dia-bit-bot : '+ get_response(ques))
                
        except Exception as e:
            print("Sorry!! Invalid values")    

