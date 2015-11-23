from django.core.management.base import BaseCommand, CommandError
from stocks.utils.TradeRecordExtractor import TradeRecordExtractor
import dropbox
from time import sleep
import urllib3

import os
import tempfile
import shutil
from contextlib import contextmanager
from dropbox.files import DownloadError, FileMetadata
import io

@contextmanager
def tempinput(file_):
    temp = tempfile.NamedTemporaryFile(delete=False)
    
    shutil.copyfileobj(file_, temp)
    temp.close()
    print('temp file created')
    yield temp.name
    os.unlink(temp.name)
    print('temp file deleted')

class Command(BaseCommand):


    def handle(self, *args, **options):
        print("Reading DropBox...")
        dbx = dropbox.Dropbox('DO8936TNbkgAAAAAAAAAg4zB4LdJK2SBNBPdjaTWM5mpzjU8dFmp1MV5DNiEXDzk')
        print(dbx.users_get_current_account())
        for entry in dbx.files_list_folder('/业绩单',recursive=True).entries:
            if not isinstance(entry, FileMetadata):
                continue
            #TODO: deal with subdirectory file path resolution
            filepath = entry.lower_path+entry.name
            print(filepath)
            try:
                metadata,response = dbx.files_download(filename)
                
            except Exception:
                print("Error downloading {} - skipped".format(filename))
                continue
            with tempinput(io.BytesIO(response.content)) as tempfilename:
                extractor = TradeRecordExtractor(entry.name, tempfilename)
                extractor.process()
                response.close()
                return
        return