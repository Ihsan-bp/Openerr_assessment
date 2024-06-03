from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
from dotenv import load_dotenv

#google free api key(shuld save in .env)
GOOGLE_API_KEY='AIzaSyD9DJ52ky_r7R5hPY7X5RDQrcI-Ag3YZEU'

# defining llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

existing_bullet_points = {
    " Owned product lifecycle; monitoring, measuring, minimizing customer support and promoting self-serve.\n",
    " Built product culture, OKR and data feedback systems to take MAU to 10k and ARR to $100k from near 0\n",
    " Iterated with experimentation of acquisition levers; ran scripts to track sites where target users gathered, reacted fast and appropriately and each new tool/post brought in 1000s of users and signups\n",
    " Restructured APIs to be less opinionated for usability/popularity, contributing to x2 increase in GitHub Stars\n",
    " Discovered major bottlenecks to activation, prioritization increased activation by x2 over last 6 months\n"
}


prompt_for_break_down=f"""
You are given a set of bullet points from a user's resume that describe their professional experience. 
Our goal is to break down each of these bullet points into separate, distinct topics, keywords, or short descriptions. 
Each extracted element should capture a unique aspect of the user's experience mentioned in the bullet point. 
This breakdown will help us create more detailed and comprehensive descriptions of their skills and accomplishments in 
subsequent steps. 

Here's what we need you to do:

1. Analyze each bullet point carefully.
2. Identify and extract distinct elements or keywords that describe different aspects of the experience mentioned.
3. Ensure that each extracted element is unique and does not overlap with others.
4. Aim for maximum quality and clarity in the extracted topics or keywords.

The purpose of this exercise is to generate a detailed set of descriptors that we can use to create new, detailed bullet points, 
enhancing the user's resume by highlighting specific skills, actions, and outcomes more effectively.

Here are the bullet points you need to break down:

{existing_bullet_points}

Please provide the distinct topics, keywords, or short descriptions for each bullet point, ensuring maximum quality and minimal overlap.

Example:

 Owned product lifecycle:
    - Product lifecycle management
    - Monitoring product performance
    - Measuring product metrics
    - Minimizing customer support
    - Promoting self-serve solutions

[Continue with the breakdown for the remaining bullet points]
"""

#calling llm to generate keywords/short description
keywords =llm.invoke(prompt_for_break_down)
breakdown_points = keywords.content


Prompt_for_Generating_Bullet_Points=f"""
You are given a set of distinct topics, keywords, or short descriptions that were extracted from initial resume bullet points. 
Your task is to generate detailed and comprehensive bullet points based on these descriptions. These new bullet points 
will be used to enhance a resume, so it is important that each point effectively highlights the individual's experience, 
skills, actions, and outcomes. 

Please follow these guidelines:

1. Use the provided topics, keywords, or descriptions to create new, detailed bullet points.
2. Each bullet point should clearly convey a unique aspect of the individual's professional experience.
3. Avoid generating duplicate or residual points; each bullet should be distinct and not overlap with others.
4. Ensure that the bullet points are relevant, impactful, and suitable for inclusion in a professional resume.

Here are the topics, keywords, or short descriptions for you to work with:
{breakdown_points}

Please generate detailed bullet points for each topic/keyword. For example:

Please generate detailed bullet points for each topic/keyword. For example:

1. **Product lifecycle management:**
   - Managed the complete product lifecycle from ideation to launch, ensuring alignment with business goals and user needs.

2. **Product performance monitoring:**
   - Implemented comprehensive monitoring tools to track product performance, identifying areas for improvement and ensuring optimal user experience.


Each bullet point should be specific, action-oriented, and reflect significant contributions or achievements. 
Ensure that they collectively provide a clear and compelling overview of the individual’s capabilities and accomplishments.

[Continue generating detailed bullet points for the remaining topics/keywords]
"""
new_generated_points =llm.invoke(Prompt_for_Generating_Bullet_Points)

newly_generated_points = new_generated_points.content

print(newly_generated_points)

