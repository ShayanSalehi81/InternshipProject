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

translations = {
    "Greet user": "کاربر را خوش آمد بگو",
    "Ask user how they are feeling": "از کاربر بپرسید که چه احساسی دارد",
    "Verify if user prefers a friendly or formal conversation": "بررسی کنید که آیا کاربر مکالمه دوستانه یا رسمی را ترجیح می‌دهد",
    "Emotion recognition": "تشخیص احساسات",
    "Ask user to select correct emotion": "از کاربر بخواهید احساس درست را انتخاب کند",
    "Ask how they are feeling": "از او بپرسید که چه احساسی دارد",
    "Switch to desired tone": "به لحن مورد نظر تغییر دهید",
    "Is the predicted emotion correct?": "آیا احساس پیش‌بینی شده درست است؟",
    "Invite user to project negative emotions onto a neutral object": "از کاربر بخواهید احساسات منفی را بر روی یک شیء خنثی منتقل کند",
    "User selection": "انتخاب کاربر",
    "Exercise(s)": "تمرین(ها)",
    "State Name": "نام حالت",
    "Condition/Question": "شرط/سوال",
    "Next State/Yes Path": "مسیر بله/وضعیت بعدی",
    "Next State/No Path": "مسیر خیر/وضعیت بعدی",
    "User Input": "ورودی کاربر"
}

translations.update({
    "Greet user": "کاربر را خوش آمد بگو",
    "Ask user how they are feeling": "از کاربر بپرسید که چه احساسی دارد",
    "Verify if user prefers a friendly or formal conversation": "بررسی کنید که آیا کاربر مکالمه دوستانه یا رسمی را ترجیح می‌دهد",
    "Emotion recognition": "تشخیص احساسات",
    "Ask user to select correct emotion": "از کاربر بخواهید احساس درست را انتخاب کند",
    "Is the predicted emotion correct?": "آیا احساس پیش‌بینی شده درست است؟",
    "Ask if the emotion is negative, positive, or antisocial": "بپرسید که آیا احساس منفی، مثبت یا ضد اجتماعی است",
    "Ask if an event caused the negative emotion": "بپرسید که آیا رویدادی باعث احساس منفی شده است",
    "Ask if the event was recent": "بپرسید که آیا این رویداد اخیر بوده است",
    "Ask if user found exercise 10 distressing": "بپرسید که آیا کاربر تمرین 10 را ناراحت کننده یافته است",
    "Ask user if it is ok to ask additional questions": "بپرسید که آیا پرسیدن سوالات اضافی مجاز است",
    "Check if advanced exercises are appropriate for user": "بررسی کنید که آیا تمرینات پیشرفته برای کاربر مناسب است",
    "Choose an additional question": "یک سوال اضافی انتخاب کنید",
    "Invite user to project negative emotions onto their childhood self": "از کاربر بخواهید احساسات منفی را بر روی خود دوران کودکی منتقل کند",
    "Suggest exercise": "تمرین پیشنهاد دهید",
    "Invite user to attempt selected exercise": "از کاربر بخواهید تمرین انتخاب شده را امتحان کند",
    "Ask user how they feel after the exercise": "از کاربر بپرسید پس از تمرین چه احساسی دارد",
    "Ask if they would like another exercise": "بپرسید که آیا مایل به انجام تمرین دیگری هستند",
    "Thank user and end session": "از کاربر تشکر کنید و جلسه را خاتمه دهید",
    "Offer restart": "پیشنهاد راه‌اندازی مجدد دهید",
    "Ask how they are feeling": "بپرسید چه احساسی دارد",
    "Switch to desired tone": "به لحن مورد نظر تغییر دهید",
    "Is the emotion negative, positive or antisocial?": "آیا احساس منفی، مثبت یا ضد اجتماعی است؟",
    "Check if advanced exercises are appropriate": "بررسی کنید که آیا تمرینات پیشرفته مناسب هستند",
    "Invite user to project negative emotions onto a neutral object": "از کاربر بخواهید احساسات منفی را بر روی یک شیء خنثی منتقل کند",
    "Exercises 7, 15, 16": "تمرینات ۷، ۱۵، ۱۶",
    "Exercise 9": "تمرین ۹",
    "Exercise 10": "تمرین ۱۰",
    "Exercise 15": "تمرین ۱۵",
    "Add relevant exercises": "تمرینات مرتبط را اضافه کنید",
    "Yes/No": "بله/خیر",
    "User selection": "انتخاب کاربر"
})

state_name_translated = [translations.get(item, item) for item in state_name_padded]
condition_question_translated = [translations.get(item, item) for item in condition_question_padded]
next_state_yes_translated = [translations.get(item, item) for item in next_state_yes_padded]
next_state_no_translated = [translations.get(item, item) for item in next_state_no_padded]
exercises_translated = [translations.get(item, item) for item in exercises_padded]
user_input_translated = [translations.get(item, item) for item in user_input_padded]

df_final_translated = pd.DataFrame({
    "نام حالت": state_name_translated,
    "شرط/سوال": condition_question_translated,
    "مسیر بله/وضعیت بعدی": next_state_yes_translated,
    "مسیر خیر/وضعیت بعدی": next_state_no_translated,
    "تمرین(ها)": exercises_translated,
    "ورودی کاربر": user_input_translated
})

translated_file_path_manual = 'chatbot_flowchart_final_corrected_translated_full_manual.xlsx'
df_final_translated.to_excel(translated_file_path_manual, index=False)