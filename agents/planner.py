class PlannerAgent:
    def create_plan(self, goal):
        print("[PlannerAgent] Breaking down goal into tasks...")
        return [
            "Get next SpaceX launch",
            "Check weather at launch site",
            "Assess likelihood of delay"
        ]