import psutil
import humanize
import datetime
from flask import Flask
import platform
import subprocess
import distro

app = Flask(__name__)

@app.route("/")
def index():

    ######################### CPU #########################
    # cpu var
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_count_physique = psutil.cpu_count(logical=False)
    cpu_per = psutil.cpu_percent(interval=1, percpu=True)
    main_core = cpu_per.index(max( cpu_per ))
    freq = psutil.cpu_freq().current
    # cpu print
    print (f"CPU Usage: {cpu_usage}%" )
    print (f"Freqency: {freq} Mhz")
    print(f"CPU cores: {cpu_count}")
    print(f"Physical cores: {cpu_count_physique}")
    print(f"Main CPU Core: {main_core}")

    ######################### Memory #########################
    # memory var 
    memory =psutil.virtual_memory()
    total = humanize.naturalsize(memory.total)
    available = humanize.naturalsize(memory.available)
    used = humanize.naturalsize(memory.used)
    usage_per = memory.percent
    available_per = round ( (memory.available / memory.total)* 100 ,1)
    # memory print 
    print(f"Total Memory: {total}")
    print(f"Available Memory: {available}")
    print(f"Used Memory: {used}")
    print(f"Available Memory per: {available_per}%")
    print(f"Used Memory per: {usage_per}%")

    ######################### Battery #########################
    # battery var
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    time_left = datetime.timedelta(seconds=battery.secsleft)
    Status = ""
    Charging_time = " N/A "
    # battery print
    if battery is None:
        Status = "Not Available"
    else :
        print(f"Battery Percentage: {percent}%")
        print(f"Plugged in: {plugged}")
        if plugged :
            print(f"Charging time: {Charging_time}")
            if percent < 100 :
                Status = "Currently charging"
            if percent == 0 :
                Status = "Dead"
            else :
                Status = "Fully charged"
        else :
            if percent < 100 :
                print(f"Remaining time : {time_left}")
                Status = "Discharging"
            else :
                Status = "Fully charged"
    print (f"Status: {Status}")

    ######################### General System information #########################
    # var
    system_platform = platform.system()
    system_architecture = platform.machine()
    operating_system = platform.uname().system
    operating_system_release = platform.uname().release
    system_date = datetime.date.today()
    system_time = datetime.datetime.now().time()
    processor_info = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq | awk -F ':' '{print $2}'",
                                         shell=True).decode().strip()

    dist_info = distro.linux_distribution()
    dist_name = dist_info[0]
    dist_version = dist_info[1]
    dist_id = dist_info[2]

    # print 
    print(f"System Platform: {system_platform}")
    print(f"System Architecture: {system_architecture}")
    print(f"Operating System: {operating_system}")
    print(f"Operating System Release: {operating_system_release}")
    print(f"System Date: {system_date}")
    print(f"System Time: {system_time}")
    print(f"Processor: {processor_info}")
    print("Distribution Name:", dist_name)
    print("Distribution Version:", dist_version)
    print("Distribution ID:", dist_id)





    return("ok")


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
