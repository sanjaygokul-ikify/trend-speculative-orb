import time

def collect_metrics(metrics: dict) -> dict:
    metrics['execution_time'] = time.time()
    return metrics