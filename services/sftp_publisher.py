import paramiko

class SFTPPublisher:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.sftp = None

    def connect(self):
        """ Connect to the SFTP server."""
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.hostname, port=self.port, username=self.username, password=self.password)
        self.sftp = self.client.open_sftp()

    def publish_file(self, local_file_path, remote_file_path):
        """ Publish a file to the SFTP server."""
        if self.sftp is None:
            raise Exception("SFTP connection is not established.")
        self.sftp.put(local_file_path, remote_file_path)

    def disconnect(self):
        """ Disconnect from the SFTP server."""
        if self.sftp is not None:
            self.sftp.close()
        if self.client is not None:
            self.client.close()