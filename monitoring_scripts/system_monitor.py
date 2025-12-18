import psutil
import logging

# Setup logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_system_health():
    print("--- Starting System Health Check ---")
    
    # 1. CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        msg = f"CRITICAL: High CPU Usage: {cpu_usage}%"
        print(msg)
        logging.warning(msg)
    else:
        print(f"CPU Usage: {cpu_usage}% (Normal)")

    # 2. Memory Usage
    memory = psutil.virtual_memory()
    if memory.percent > 80:
        msg = f"CRITICAL: High Memory Usage: {memory.percent}%"
        print(msg)
        logging.warning(msg)
    else:
        print(f"Memory Usage: {memory.percent}% (Normal)")

    # 3. Disk Space
    disk = psutil.disk_usage('/')
    if disk.percent > 90:
        msg = f"CRITICAL: Low Disk Space! Used: {disk.percent}%"
        print(msg)
        logging.warning(msg)
    else:
        print(f"Disk Usage: {disk.percent}% (Normal)")

    print("--- Health Check Complete ---")

if __name__ == "__main__":
    check_system_health()