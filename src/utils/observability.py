import json
import time
from datetime import datetime


class ObservabilityLogger:
    def __init__(self, log_file="rag_logs.jsonl"):
        self.log_file = log_file

    def log(self, data: dict):
        data["timestamp"] = datetime.utcnow().isoformat()

        with open(self.log_file, "a") as f:
            f.write(json.dumps(data) + "\n")
