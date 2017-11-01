# cat c_backup.dat | colrm 1 40 > c.dat
import json
import datetime


def get_command(target, filename="data/c.dat"):
    # variable for comparing time
    prev_result = -1
    prev_data = None

    # open command log file
    f = open(filename)
    for line in f:
        data = json.loads(line)['data']
        # compare time
        time = datetime.datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S.%f')
        result = (time - target).days
        if prev_result == -1 and result == 0:  # check
            print prev_data['time'], prev_data['vx'], prev_data['vy'], prev_data['va'], prev_data['vz']
            ret = prev_data
            break

        # update result for next search
        prev_result = result
        prev_data = data

    f.close()
    return ret

target = datetime.datetime.strptime("2017-10-27 11:29:23.459689", '%Y-%m-%d %H:%M:%S.%f')
print get_command(target)
