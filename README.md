# Deep Agent – Autonomous Planning & Execution System
An Agentic AI system that takes a high-level goal, decomposes it into structured steps, executes them through sub-agents, and stores the results in memory for future reasoning.

This project demonstrates a Planner → Executor → Memory architecture, enabling an LLM to reason about complex tasks and execute them sequentially.
# Architecture
User Goal
   │
   ▼
Planner Agent
   │
   ▼
Task Steps
   │
   ▼
Executor Agents
   │
   ▼
Memory Storage

Planner Agent

Responsible for breaking a complex goal into structured steps.

Executor Agents

Execute each step sequentially and generate outputs.

Memory Module

Stores the outputs in a persistent memory file (JSON) so results can be retrieved or reused later.

# Input Goal
Plan a 7-day trip to Japan for a family of four, including activities for kids and adults.

# Generated Plan
1.	Choose travel dates and ensure availability
	2.	Decide travel style and create itinerary
	3.	Research kid-friendly activities
	4.	Book family-friendly accommodations
	5.	Reserve attractions and transportation

Each step is executed by the agent and stored in memory.
# Tech Stack
	•	Python
	•	LangChain
	•	Groq LLM (LLaMA-3.1-8B Instant)
	•	Agent-based architecture
	•	JSON memory storage
