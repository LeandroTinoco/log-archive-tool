import zipfile

def archive_log_files(log_files, archive_name):
    with zipfile.ZipFile(archive_name, 'w') as archive:
        for log_file in log_files:
            archive.write(log_file, os.path.basename(log_file))

