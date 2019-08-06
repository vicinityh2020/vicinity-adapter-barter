ssh machine1 sudo 'docker ps --filter="name=dev-peer" --format "{{.ID}}: {{.RunningFor}}"'

import subprocess
cmd = ['echo', 'I like potatos']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: '  + e.decode('ascii'))
print('code: ' + str(proc.returncode))
