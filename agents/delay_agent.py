class DelayAssessmentAgent:
    def analyze(self, launch_data, weather_data):
        print("[DelayAssessmentAgent] Analyzing conditions for possible delay...")

        wind = weather_data['wind_speed']
        description = weather_data['description']
        risk = False

        if wind > 10 or 'storm' in description.lower() or 'rain' in description.lower():
            risk = True

        status = "LIKELY" if risk else "UNLIKELY"
        result = (
            f"Launch: {launch_data['name']} at {launch_data['site']}\n"
            f"Date: {launch_data['date']}\n"
            f"Weather: {weather_data['description']} with {weather_data['wind_speed']} m/s wind\n"
            f"Delay Risk: {status}"
        )
        return result