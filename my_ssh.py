import paramiko
import os
import interactive
port = 22
hostname = '192.168.2.67'
keyPath = './2.67-zhan'
username = 'zhan'
password = ''
key_file_pwd = ''

paramiko.util.log_to_file('ssh_key-login.log')
privatekey = os.path.expanduser(keyPath)  # 私钥文件

key = paramiko.RSAKey.from_private_key_file(privatekey)
ssh = paramiko.SSHClient()
ssh.load_system_host_keys(filename=os.path.expanduser('~/.ssh/known_hosts'))
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, pkey=key)

# 交互式连接
# channel = ssh.invoke_shell()
# interactive.interactive_shell(channel)
# channel.close()
# ssh.close()

# 只执行一次命令
stdin, stdout, stderr = ssh.exec_command('ls')  # 执行远程主机系统命令
ret = stdout.read()
print()
ssh.close()