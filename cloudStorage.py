import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
       dbx = dropbox.Dropbox(self.access_token)

       f= open(file_from, 'rb') 
       dbx.files_upload(f.read(), file_to)

    def main():
        access_token = 'sl.A2rnIOauzJsw0S2cd1iF3bX9ztyOOSoNC8tGFpZWDv9nL2AEhbDhVSjUZAMhii9x5xJwdeCJVCIlo6zoIg1FTcnJ9zu-Ceji-fWqeWeXEP_4rF3eyzn67nehheO7eDw6eaDD-kA'
        transferData =TransferData(access_token)