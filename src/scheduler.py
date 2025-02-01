import schedule
import time
from log_reader import read_log_files
from log_archiver import archive_log_files

def job():
    log_files = read_log_files('path/to/logs')
    archive_log_files(log_files, 'archive.zip')

schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

from config import load_config

config = load_config('config.yaml')

log_dir = config['log_dir']
archive_name = config['archive_name']

def job():
    log_files = read_log_files(log_dir)
    archive_log_files(log_files, archive_name)

if config['schedule'] == 'daily':
    schedule.every().day.at("00:00").do(job)
# Add other scheduling options here

while True:
    schedule.run_pending()
    time.sleep(1)

    