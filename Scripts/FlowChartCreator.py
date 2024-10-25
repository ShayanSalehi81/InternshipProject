import pandas as pd

max_length = 16

def pad_list(lst, length):
    return lst + [""] * (length - len(lst))

state_name_padded = pad_list([
    "Greet user", 
    "Ask user how they are feeling", 
    "Verify if user prefers a friendly or formal conversation", 
    "Emotion recognition",  
    "Ask user to select correct emotion",
    "Is the predicted emotion correct?", 
    "Ask if the emotion is negative, positive, or antisocial",
    "Ask if an event caused the negative emotion", 
    "Ask if the event was recent", 
    "Ask if user found exercise 10 distressing", 
    "Ask user if it is ok to ask additional questions", 
    "Check if advanced exercises are appropriate for user",  
    "Choose an additional question",  
    "Invite user to project negative emotions onto their childhood self", 
    "Suggest exercise",
    "Invite user to attempt selected exercise",  
    "Ask user how they feel after the exercise", 
    "Ask if they would like another exercise", 
    "Thank user and end session", 
    "Offer restart"
], max_length)

condition_question_padded = pad_list([
    "Ask how they are feeling", 
    "Verify if user prefers a friendly or formal conversation", 
    "Switch to desired tone", 
    "Ask if the predicted emotion is correct",  
    "Ask user to select correct emotion", 
    "Is the predicted emotion correct?", 
    "Is the emotion negative, positive or antisocial?",
    "Ask if an event caused the negative emotion", 
    "Ask if the event was recent", 
    "Ask if user found exercise 10 distressing", 
    "Ask user if it is ok to ask additional questions", 
    "Check if advanced exercises are appropriate for user", 
    "Choose an additional question", 
    "Invite user to project negative emotions onto their childhood self", 
    "Suggest exercise", 
    "Invite user to attempt selected exercise", 
    "Ask user how they feel after the exercise", 
    "Ask if they would like another exercise", 
    "Thank user and end session", 
    "Offer restart"
], max_length)

next_state_yes_padded = pad_list([
    "Ask user to select correct emotion", 
    "Switch to desired tone", 
    "Emotion recognition",  
    "Is the predicted emotion correct?", 
    "Is the predicted emotion correct?", 
    "Is the emotion negative, positive or antisocial?", 
    "Ask if an event caused the negative emotion", 
    "Ask if the event was recent", 
    "Ask if user found exercise 10 distressing", 
    "Check if advanced exercises are appropriate", 
    "Check if advanced exercises are appropriate", 
    "Choose an additional question", 
    "Invite user to project negative emotions onto their childhood self", 
    "Suggest exercise", 
    "Invite user to attempt selected exercise", 
    "Ask if they would like another exercise", 
    "Ask if they would like another exercise", 
    "Thank user and end session", 
    "Offer restart"
], max_length)

next_state_no_padded = pad_list([
    "", 
    "", 
    "", 
    "Invite user to project negative emotions onto their childhood self", 
    "Invite user to project negative emotions onto their childhood self", 
    "Exercise 9", 
    "Exercise 9", 
    "Exercise 9", 
    "Exercise 10", 
    "Exercise 15", 
    "Exercise 15", 
    "", 
    "", 
    "", 
    "", 
    "", 
    "", 
    "", 
    ""
], max_length)

exercises_padded = pad_list([
    "", 
    "", 
    "", 
    "", 
    "", 
    "Exercises 7, 15, 16", 
    "Exercise 9", 
    "Exercise 9", 
    "Exercise 15", 
    "Add relevant exercises", 
    "Add relevant exercises", 
    "Add relevant exercises", 
    "", 
    "Add relevant exercises", 
    "", 
    "", 
    "", 
    ""
], max_length)

user_input_padded = pad_list([
    "", 
    "", 
    "", 
    "", 
    "User selection", 
    "Yes/No", 
    "Yes/No", 
    "Yes/No", 
    "Yes/No", 
    "Yes/No", 
    "Yes/No", 
    "", 
    "Yes/No", 
    "", 
    "", 
    "", 
    "", 
    "", 
    ""
], max_length)

df_final_corrected = pd.DataFrame({
    "State Name": state_name_padded,
    "Condition/Question": condition_question_padded,
    "Next State/Yes Path": next_state_yes_padded,
    "Next State/No Path": next_state_no_padded,
    "Exercise(s)": exercises_padded,
    "User Input": user_input_padded
})

output_file_final_corrected = "chatbot_flowchart_final_corrected.xlsx"
df_final_corrected.to_excel(output_file_final_corrected, index=False)