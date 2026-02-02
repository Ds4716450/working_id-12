import paramiko
# Create object of SSHClient and 
# connecting to SSH
ssh = paramiko.SSHClient()
 
# Adding new host key to the local 
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
ssh.connect('10.0.4.253', port=22, username='vcti',
            password='inD@18us', timeout=3)
 
# Execute command on SSH terminal 
# using exec_command
stdin, stdout, stderr = ssh.exec_command('ls && cd Dev72 && cat february.txt')
# stdin, stdout, stderr = ssh.exec_command('cd Dev72')
# stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())
ssh.close()
