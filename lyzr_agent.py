# DataGuardian-AI - Lyzr Agent Integration
# Enterprise Data Leak Prevention Agent

from lyzr_automata import Agent, Task

class DataGuardianAgent:
    def __init__(self):
        self.agent = Agent(
            role="Data Leak Prevention Specialist",
            goal="Detect and prevent sensitive data leaks in enterprise files",
            backstory="Expert in DLP, PII detection and compliance"
        )
    
    def scan_file(self, file_path):
        task = Task(
            description=f"Scan {file_path} for PII, API keys, passwords and sensitive data",
            expected_output="List of risks found with severity"
        )
        # Logic to detect patterns - Regex for Aadhaar, PAN, API keys
        return self.agent.execute_task(task)

    def generate_report(self, findings):
        return f"Risk Report: {len(findings)} issues found. Compliance: GDPR, DPDP Act"

# Usage
if __name__ == "__main__":
    guardian = DataGuardianAgent()
    print("DataGuardian Agent Ready - Built for St. Joseph Hackathon")
