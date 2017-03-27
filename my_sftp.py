import paramiko
import os
import SSHConnection

port = 22
hostname = '192.168.2.67'
keyPath = './2.67-zhan'
username = 'zhan'
password = ''
key_file_pwd = ''

paramiko.util.log_to_file('sftp.log')
ssh = SSHConnection.SSHConnection(hostname, port, username, key_path=keyPath)
sftp = ssh.get_sftp()

# put，get，mkdir，rename，stat，listdir等方法操作文件，分别实现文件上传、下载、文件夹创建、文件重命名，显示文件属性和文件夹列表

dir_info = sftp.listdir('/home/zhan/')  # 文件列表
print(dir_info)
sftp.put('test', '/home/zhan/test')  # 上传文件
file_info = sftp.stat('/home/zhan/test')  # 文件属性
print(file_info)
sftp.get('/home/zhan/test2', 'test2')   # 下载文件
dir_info = sftp.listdir('/home/zhan')
print(dir_info)