import paramiko
import os


class SSHConnection(object):

    def __init__(self, server, port, username, password = None, key_path = None):
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.key_path = key_path
        if key_path:
            privatekey = os.path.expanduser(key_path)  # 私钥文件
            key = paramiko.RSAKey.from_private_key_file(privatekey)
            self.key = key
        else:
            self.key = None
        self._ssh = None

    def connection(self):
        if not self.is_connected():
            self._ssh = paramiko.SSHClient()
            self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self._ssh.connect(hostname=self.server, port=self.port,
                              username=self.username, password=self.password, pkey=self.key)

        return self._ssh

    def is_connected(self):
        transport = self._ssh.get_transport() if self._ssh else None
        return transport and transport.is_active()

    def exec_command(self, command):
        self.connection().exec_command(command)

    def get_sftp(self):
        self.connection()
        return self._ssh.open_sftp()
