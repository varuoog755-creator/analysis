import json
import time
import os
from trend_engine import TrendEngine
import pandas as pd
from datetime import datetime

RESULTS_FILE = "agent_results.json"

LOGS_FILE = "fleet_logs.json"

class FleetEngine:
    def __init__(self):
        self.engine = TrendEngine()
        self.results_path = os.path.join(os.path.dirname(__file__), RESULTS_FILE)
        self.logs_path = os.path.join(os.path.dirname(__file__), LOGS_FILE)

    def add_log(self, message, agent="SYSTEM"):
        logs = []
        if os.path.exists(self.logs_path):
            try:
                with open(self.logs_path, 'r') as f:
                    logs = json.load(f)
            except: pass
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        logs.append(f"[{timestamp}] [{agent}] {message}")
        # Keep last 15 lines
        logs = logs[-15:]
        with open(self.logs_path, 'w') as f:
            json.dump(logs, f)

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
        self.add_log("Starting autonomous market pulse...", "Researcher-Alpha")
        
        # Dynamic niche exploration
        niches = ["AI Coding Agents", "Browser-use AI", "Sustainable Tech", "Vegan Pet Food", "Tailwind v4", "DeepSeek-V3"]
        
        results = self.load_results()
        results["active_agents"] = ["Researcher-Alpha"]
        results["last_run"] = datetime.now().isoformat()
        
        new_discoveries = False
        for kw in niches:
            if not any(f['keyword'] == kw for f in results["findings"]):
                self.add_log(f"Scanning niche: {kw}", "Researcher-Alpha")
                x_trends = self.engine.get_x_trends(kw)
                
                # Mock score logic
                strength = len(x_trends) if not x_trends.empty else 0
                if strength > 2:
                    self.add_log(f"High signal found for '{kw}' with score {strength}", "Researcher-Alpha")
                    finding = {
                        "keyword": kw,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "source": "X.com / HN / RSS",
                        "strength": strength,
                        "status": "Verified"
                    }
                    results["findings"].insert(0, finding)
                    new_discoveries = True
                time.sleep(1) # Rate limit protection
        
        results["findings"] = results["findings"][:30] # Keep top 30
        results["active_agents"] = []
        self.save_results(results)
        
        if new_discoveries:
            self.add_log("Broadcasting new intelligence to OpenClaw Bridge...", "Content-Bot")
            self.notify_openclaw()
        
        self.add_log("Pulse loop complete. Entering standby.", "SYSTEM")

    def notify_openclaw(self):
        """Creates a trigger file for OpenClaw to process."""
        trigger_path = os.path.join(os.path.dirname(__file__), "openclaw_trigger.txt")
        with open(trigger_path, 'w') as f:
            f.write(f"New trends detected at {datetime.now().isoformat()}. OpenClaw, please summarize for the user.")
        print("OpenClaw notified.")

    def run_continuous(self, interval_sec=14400): # 4 hours default
        self.add_log("24/7 Multi-Agent Fleet initialized.", "SYSTEM")
        while True:
            try:
                self.researcher_pulse()
            except Exception as e:
                self.add_log(f"CRITICAL ERROR: {str(e)}", "SYSTEM")
            
            self.add_log(f"Next heartbeat in {interval_sec//60} mins...", "SYSTEM")
            time.sleep(interval_sec)

if __name__ == "__main__":
    import sys
    btn_flag = "--loop" in sys.argv
    fleet = FleetEngine()
    if btn_flag:
        fleet.run_continuous()
    else:
        fleet.researcher_pulse()
