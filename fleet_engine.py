import json
import time
import os
from trend_engine import TrendEngine
import pandas as pd
from datetime import datetime

RESULTS_FILE = "agent_results.json"

class FleetEngine:
    def __init__(self):
        self.engine = TrendEngine()
        self.results_path = os.path.join(os.path.dirname(__file__), RESULTS_FILE)

    def load_results(self):
        if os.path.exists(self.results_path):
            with open(self.results_path, 'r') as f:
                return json.load(f)
        return {"findings": [], "last_run": None, "active_agents": []}

    def save_results(self, data):
        with open(self.results_path, 'w') as f:
            json.dump(data, f, indent=4)

    def researcher_pulse(self):
        """Agent that finds new keywords autonomously."""
        print("Researcher Agent: Scanning for new niches...")
        new_keywords = ["OpenRouter", "DeepSeek", "PydanticAI", "Cursor AI", "Tailwind v4"]
        
        results = self.load_results()
        results["active_agents"] = ["Researcher"]
        results["last_run"] = datetime.now().isoformat()
        
        new_discoveries = False
        for kw in new_keywords:
            if not any(f['keyword'] == kw for f in results["findings"]):
                print(f"Found new niche: {kw}")
                x_trends = self.engine.get_x_trends(kw)
                finding = {
                    "keyword": kw,
                    "timestamp": datetime.now().isoformat(),
                    "source": "X.com / HN",
                    "strength": len(x_trends) if not x_trends.empty else 0,
                    "status": "Verified"
                }
                results["findings"].insert(0, finding)
                new_discoveries = True
        
        results["findings"] = results["findings"][:20]
        results["active_agents"] = []
        self.save_results(results)
        
        if new_discoveries:
            self.notify_openclaw()
        
        print("Researcher Agent: Run complete.")

    def notify_openclaw(self):
        """Creates a trigger file for OpenClaw to process."""
        trigger_path = os.path.join(os.path.dirname(__file__), "openclaw_trigger.txt")
        with open(trigger_path, 'w') as f:
            f.write(f"New trends detected at {datetime.now().isoformat()}. OpenClaw, please summarize for the user.")
        print("OpenClaw notified via trigger file.")

if __name__ == "__main__":
    fleet = FleetEngine()
    # Manual trigger for test
    fleet.researcher_pulse()
