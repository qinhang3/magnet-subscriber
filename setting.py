import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "s:")
setting_file = None
conf = {
    "session_key": "123456",
    "debug": True,
    "github_client_id": '',
    "github_client_secret": ''
}

for op, value in opts:
    if op == '-s':
        setting_file = value
print('setting_file', setting_file)
if setting_file:
    file = open(setting_file)
    if not file:
        print 'setting_file ' + setting_file + ' not exists!'
    for index, line in enumerate(file.readlines()):
        print('load setting:', line)
        [k, v] = line.split('=', 1)
        conf[k] = v.strip()
    print conf
    file.close()

