# 🚀 Multi-Agent AI System with Google ADK

This project implements a multi-agent system that takes a user goal, plans it, routes data between agents, and iteratively refines output.

---

## 🧠 Goal Example
> "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."

---

## 🧩 Agents

- **PlannerAgent**: Breaks down the goal into sub-tasks
- **LaunchInfoAgent**: Fetches upcoming SpaceX launch info (via [SpaceX API](https://github.com/r-spacex/SpaceX-API))
- **WeatherAgent**: Uses OpenWeatherMap API to get weather for the launch location
- **DelayAssessmentAgent**: Analyzes the risk of delay based on weather data

---

## 🔧 Setup Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
Create .env file

ini
Copy
Edit
OPENWEATHER_API_KEY=your_api_key_here
Run the app

bash
Copy
Edit
python main.py
📊 Evaluation
✅ Agent chaining and data enrichment

✅ Planner correctly delegates tasks

✅ Output refined iteratively

✅ Modular and testable agent structure

📦 APIs Used
SpaceX Launch API

OpenWeatherMap API
---
📄 3. `requirements.txt`
requests
python-dotenv
📑 4. .env File (Don't share this publicly!)
OPENWEATHER_API_KEY=your_api_key_here
📝 5. Evaluation Report (Optional Example)
## Evaluation: Goal Fulfillment

### Test Goal:
"Find the next SpaceX launch, check weather at that location, and determine if it may be delayed."

**Result:**
- Launch info retrieved: ✅
- Weather fetched using coordinates: ✅
- Delay analysis completed based on wind/clouds: ✅
- Final summary compiled by agents: ✅

**Conclusion:** The multi-agent system fulfilled the goal end-to-end with proper agent routing and output dependency.
