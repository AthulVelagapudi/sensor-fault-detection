
import os
class S3Sync:


    def sync_folder_to_s3(self,folder,aws_buket_url):
        command = f"aws s3 sync {folder} {aws_buket_url} "
        os.system(command)





