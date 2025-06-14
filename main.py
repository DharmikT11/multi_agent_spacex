import os
from agents.planner import PlannerAgent
from agents.launch_agent import LaunchInfoAgent
from agents.weather_agent import WeatherAgent
from agents.delay_agent import DelayAssessmentAgent
from dotenv import load_dotenv

load_dotenv()

def main():
    goal = "Find the next SpaceX launch, check weather at that location, and determine if it may be delayed."
    print(f"Goal: {goal}\n")

    # Planner splits the goal
    planner = PlannerAgent()
    plan = planner.create_plan(goal)

    # Step 1: Launch Info
    launch_agent = LaunchInfoAgent()
    launch_data = launch_agent.get_launch_details()

    # Step 2: Weather Info
    weather_agent = WeatherAgent()
    weather_data = weather_agent.get_weather(launch_data)

    # Step 3: Delay Assessment
    delay_agent = DelayAssessmentAgent()
    summary = delay_agent.analyze(launch_data, weather_data)

    print("\nFinal Output:")
    print(summary)

if __name__ == "__main__":
    main()
