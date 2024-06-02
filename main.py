from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json


#google free api key(shuld save in .env)
GOOGLE_API_KEY='AIzaSyD9DJ52ky_r7R5hPY7X5RDQrcI-Ag3YZEU'

# defining llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

#defining the initial bullet points
existing_bullet_points = [
    "Owned product lifecycle; monitoring, measuring, minimizing customer support and promoting self-serve.",
    "Built product culture, OKR and data feedback systems to take MAU to 10k and ARR to $100k from near 0",
    "Iterated with experimentation of acquisition levers; ran scripts to track sites where target users gathered, reacted fast and appropriately and each new tool/post brought in 1000s of users and signups",
    "Restructured APIs to be less opinionated for usability/popularity, contributing to x2 increase in GitHub Stars",
    "Discovered major bottlenecks to activation, prioritization increased activation by x2 over last 6 months"
]

prompt_for_generating_questions=f"""
Given the following 5 bullet points from a user's resume, generate a set of 15 questions to collect additional key information that is not 
already covered in these points. The questions should aim to gather details that can be used to create new and unique bullet points for a 
resume, covering aspects such as product vision, roadmap, product metrics, business/product requirements, product development, project 
management skills, competitive analysis, customer experience, problem-solving, strong ownership, business judgment, Gantt chart, and customer 
funnel.
Existing bullet points:
{existing_bullet_points}
Ensure that each question seeks to gather information that is relevant for creating new bullet points and that no question repeats the content already 
covered in the existing bullet points. Here are the 15 keywords to be considered for creating the questions: product vision, roadmap, product metrics, 
key metrics, business/product requirements, product development, project management skills, competitive analysis, customer experience, problem-solving, 
strong ownership, business judgment, Gantt chart, customer funnel.
Ask question who's answer must be keywords not paragraphs or sentences(example of answer to question :'problem-solving','product development')

Generate the 15 questions.
generate question straightaway, do not add any description before or after.
"""

questions =llm.invoke(prompt_for_generating_questions)

# storing all the questions into a list
questions_list = questions.content.split('\n')



#function to ask users question that are already generated and collect the users answer.
def ask_questions(questions_list):
    # Dictionary to store user responses
    responses = {}

    # Loop through each question and collect responses
    for question in questions_list[0:5]:
        # Ask the question
        print(question)
        # Collect the user's response
        response = input("Your answer: ")
        # Store the response in the dictionary
        responses[question] = response
        print("\n")

    return responses

# calling the function
responses = ask_questions(questions_list)

# Convert responses to JSON format
responses_json = json.dumps(responses, indent=4)

prompt_for_generating_bullet_points = f"""
Given the following user responses in JSON format, generate new bullet points for a resume. Each bullet point should represent a skill or experience 
the user has but has not explicitly stated in the existing responses. Use the following keywords to guide the creation of each bullet point: 
product vision, roadmap, product metrics, key metrics, business/product requirements, product development, project management skills, competitive 
analysis, customer experience, problem-solving, strong ownership, business judgment, Gantt chart, customer funnel.

Context and Purpose:
The goal is to enhance the user's resume by creating new, unique bullet points that highlight additional skills and experiences. Each new bullet point 
should be specific, actionable, and different from the information already provided in the JSON responses.

User Responses (in JSON format):
{responses_json}

Instructions:
1. Review the user responses.
2. For each keyword, generate a new bullet point that highlights a relevant skill or experience not already covered in the responses.
3. Ensure that each bullet point is unique and adds new information to the resume.
4. Use bullet format. just return as a bullet point, for example
   '* Articulated and defined product vision, outlining long-term goals and strategic direction.'

Generate the new bullet points below:
"""
# print(prompt_for_generating_bullet_points)

Bullet_points =llm.invoke(prompt_for_generating_bullet_points)


Bullet_points = Bullet_points.content.split('\n')

bullet_points_json = json.dumps(Bullet_points)

# Write JSON data to a file
with open("bullet_points.json", "w") as json_file:
    json_file.write(bullet_points_json)

# Write bullet points to a TXT file
with open("bullet_points.txt", "w") as txt_file:
    for bullet_point in Bullet_points:
        txt_file.write("%s\n" % bullet_point)

print(Bullet_points)