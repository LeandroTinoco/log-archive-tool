# src/log_reader.py
import os

def read_log_files(log_dir):
    log_files = [os.path.join(log_dir, file) for file in os.listdir(log_dir) if file.endswith('.log')]
    return log_files