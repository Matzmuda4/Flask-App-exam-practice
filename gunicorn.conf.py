import multiprocessing
import os

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

# Bind to the PORT environment variable
bind = f"0.0.0.0:{os.environ.get('PORT', '50505')}"

workers = (multiprocessing.cpu_count() * 2) + 1
threads = workers

timeout = 120
