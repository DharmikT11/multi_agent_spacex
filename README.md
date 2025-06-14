# 🚀 Multi-Agent SpaceX Launch Info System

A modular multi-agent system powered by Python that processes a natural language goal, breaks it into sub-tasks, and executes them using dedicated AI agents.  

This project demonstrates agent collaboration by fetching **SpaceX launch data**, retrieving **weather forecasts** at the launch site, and evaluating potential **launch delays**.

---

## 🧠 Example Goal

> “Find the next SpaceX launch, check weather at that location, and determine if it may be delayed.”

---

## 🧩 Agents Overview

| Agent Name             | Description |
|------------------------|-------------|
| 🧭 **PlannerAgent**         | Breaks the goal into smaller tasks |
| 🚀 **LaunchInfoAgent**     | Retrieves next launch info via the SpaceX API |
| ☁️ **WeatherAgent**         | Gets real-time weather at the launch location using OpenWeatherMap |
| ⏱ **DelayAssessmentAgent** | Analyzes weather to assess delay risk |

---

## ⚙️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi_agent_spacex.git
cd multi_agent_spacex

### 2. Set Up a Virtual Environment

python -m venv venv
source venv/Scripts/activate     # On Windows
# OR
source venv/bin/activate         # On macOS/Linux

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Add Environment Variables

Create a .env file in the root directory with the following:
OPENWEATHER_API_KEY=your_api_key_here

### ▶️ Run the Program

python main.py

### 🧪 Future Ideas

Add speech-to-text agent input

Deploy as a web app with Streamlit

### 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo, make changes, and submit a PR.

Integrate notifications (e.g., email/SMS)

### 📜 License

This project is under the MIT License.
