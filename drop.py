import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'hYlFNOvKAEQAAAAAAAAAAY4oMNh7FZ77_cFVQvzpErjtKK8uJMb5xUtKwCBbutwy'
    transferData = TransferData(access_token)

    file_from = input("Enter source path: ")
    file_to = input("Enter destination path: ") 
  
    transferData.upload_file(file_from, file_to)
    print("File has moved.")

main()
