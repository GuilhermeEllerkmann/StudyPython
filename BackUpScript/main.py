# Lucas Bombarda: Um sistema de backup
# Lucas Bombarda: Tu escolhe a pasta
# Lucas Bombarda: Ele zipa
# Lucas Bombarda: Salva com o nome sendo a data
# Lucas Bombarda: E exclui o antigo backup
import shutil
import os
from datetime import datetime

DICT_BACKUP_FOLDER = '/home/gui/Desktop/Curso_python/BackUpScript/BackUpFolder'
DICT_COPY_FOLDER = '/home/gui/Desktop/Curso_python/BackUpScript/CopyOfBackup'
BACKUP_FOLDER = '/home/gui/Desktop/Curso_python/BackUpScript'

class CopyFolderAndZip:

    def __init__(self):
        self.most_recent_time = datetime.now()
        self.shape = "%Y-%m-%d %H:%M:%S"
        self.final_hour = self.most_recent_time.strftime(self.shape)
        self.ZIP_ARCHIVE = f'{BACKUP_FOLDER}/{self.final_hour}-Backup.zip'
        self.old_backups = []

        for filename in os.listdir(BACKUP_FOLDER):
            if filename.endswith(".zip"):
                self.old_backups.append(filename) #appends on a list all the files ending with .zip

        for old_backup in self.old_backups:
            os.remove(os.path.join(BACKUP_FOLDER, old_backup)) # Remove old backups

        shutil.copytree(DICT_BACKUP_FOLDER, DICT_COPY_FOLDER) # Copy the backup folder
        
        shutil.make_archive(self.ZIP_ARCHIVE[:-4], 'zip', DICT_COPY_FOLDER) # Create the new zipped backup

        shutil.rmtree(DICT_COPY_FOLDER) # Remove the temporary copy folder

CopyFolderAndZip()