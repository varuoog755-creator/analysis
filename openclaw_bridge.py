import json
import os
from datetime import datetime

RESULTS_FILE = "agent_results.json"

def get_summary():
    path = os.path.join(os.path.dirname(__file__), RESULTS_FILE)
    if not os.path.exists(path):
        return "No TrendPulse findings yet. The fleet is still searching."

    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        return f"Error reading results: {str(e)}"

    findings = data.get("findings", [])
    if not findings:
        return "The TrendPulse fleet has not verified any new niches today."

    summary = "🚀 **TrendPulse Daily Intelligence Report**\n\n"
    for i, f in enumerate(findings[:5], 1):
        summary += f"{i}. **{f['keyword']}**\n"
        summary += f"   - Strength: {'🔥' * (f['strength'] // 2 + 1)}\n"
        summary += f"   - Source: {f['source']}\n"
        summary += f"   - Detected: {f['timestamp'][:16]}\n\n"

    summary += "💡 *Ask me to 'analyze [keyword]' for a deep dive!*"
    return summary

if __name__ == "__main__":
    # This output is what OpenClaw will capture and send to the user
    print(get_summary())
