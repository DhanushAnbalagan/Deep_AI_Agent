from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

# ----------------------------------------
# Loading Model
#------------------------------------------

print("Loading model.. It might take few seconds")

load_dotenv()  # Load environment variables from .env file

llm = ChatGroq(model="llama-3.1-8b-instant")

print("Model loaded successfully.\n")

#------------------------
# Creating Planner Agent
#------------------------

def create_planner_agent(goal):
    prompt = f""" 
    You are a Trip Planner Agent.
    Create excactly 5 step to achieve the following user goal: {goal}
    Each step should be clear and actionable.
    
    Rules:
    - Create excatly 5 steps.
    - Each step should be clear and actionable.
    - Do not include any explanations or justifications.
    - Each step should build upon the previous one.
    - Do not repeat any steps.
    - Keep it concise and to the point.
    
    Generate the 5 steps in below formate:
    
    Step 1:
    Step 2:
    Step 3:
    Step 4:
    Step 5:
    """
    llm_response =llm.invoke(prompt)
    return llm_response.content.strip()


#------------------------
# Sub Agent
#------------------------

def writing_agent(task):
    prompt = f"""
    Yor are a Professional writer.
    
    Your Job:
    - Turning the following task into a well-structured wihtin 50 words and detailed response: {task}
    - Write clearly for a general audience.
    - Use Heading and Short paragraphs to enhance readability.
    - Be practical and actionable in your response.
    
    Task = {task}
    """
    
    llm_response = llm.invoke(prompt)
    return llm_response.content.strip()

#------------------------
# Memory System
#------------------------

def save__memory(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)


#------------------------
# Deep Agent Orchestrator
#------------------------

def deep_agent(goal):
    print("Goal:", goal)
    
    #Step 1: Create Plan
    plan = create_planner_agent(goal)
    print("\nGenerated Plan:\n", plan)
    
    steps = plan.split('\n')
    results = []
    
    #Step 2: Execute steps
    print("\nSub Agent Results:\n")
    for step in steps:
        step = step.strip()
        if not step:
            continue
        
        result = writing_agent(step) 
        
        print("Completed Step:", step)
        results.append(result)
        
    #Step 3: Save Memory
    save__memory('agent_memory.json', results) 
    print("\nAll steps completed. Results saved to agent_memory.json")
    
#------------------------
# Running the Deep Agent
#------------------------

if __name__ == "__main__":
    user_goal = "Plan a 7-day trip to Japan for a family of four, including activities for kids and adults."
    deep_agent(user_goal)  
    