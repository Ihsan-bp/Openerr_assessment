from langchain_google_genai import ChatGoogleGenerativeAI

#google free api key(shuld save in .env)
GOOGLE_API_KEY='AIzaSyD9DJ52ky_r7R5hPY7X5RDQrcI-Ag3YZEU'

# defining llm
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)


prompt="""
Given 5 bullet points for a particular experience from a user’s resume, and given 15 keywords that represent skills/experience that the user has but has not included them in the resume, generate a new bullet point per keyword.

○ 5 bullet points:
■ “Owned product lifecycle; monitoring, measuring, minimizing customer support and promoting self-serve.”
■ “Built product culture, OKR and data feedback systems to take MAU to 10k and ARR to $100k from near 0”
■ “Iterated with experimentation of acquisition levers; ran scripts to track sites where target users gathered, reacted fast and appropriately and each new tool/post brought in 1000s of users and signups”
■ “Restructured APIs to be less opinionated for usability/popularity, contributing to x2 increase in GitHub Stars”
■ “Discovered major bottlenecks to activation, prioritization increased activation by x2 over last 6 months”

○ 15 keywords:
■ “product vision”, “roadmap”, “product metrics”, “key metrics”, “business/product requirements”, “product development”, “project management skills”, “competitive analysis”, “customer experience”, “problem-solving”, “strong ownership”, “business judgment”, “gantt chart”, “customer funnel”

● Ensure the following when generating bullet points:
○ The scope covered by the generated bullet points should be within the scope defined by the existing 5 bullet points, for example:
■ A new bullet point should not list a product/project that the user has not done
○ Any generated bullet point should not repeat anything written in the existing bullet points, for example:
■ Old bullet point: “Owned product lifecycle; monitoring, measuring, minimizing customer support and promoting self-serve."
■ Generated bullet point for keyword “customer experience”: “Owned product lifecycle; monitoring, measuring, minimizing customer support and promoting self-serve to enhance customer experience.”
● These two are too similar and are repeating the same point
○ Generated bullet points should not repeat any information amongst themselves, for example:
■ Generated bullet point for keyword “customer experience”: “Owned product lifecycle; monitoring, measuring, minimizing customer support and promoting self-serve to enhance customer experience.”
■ Generated bullet point for keyword “product development”: “Owned product lifecycle in product development; monitoring, measuring, minimizing customer support and promoting self-serve.”
● These two are too similar and are repeating the same point

generate a new bullet point per keyword.
"""
# invoking llm
single_prompt =llm.invoke(prompt)
#fetching content from the llm answer
single_prompt_answer = single_prompt.content
print(single_prompt_answer)