import humanize, datetime
from flask import Flask, jsonify
from flask_cors import CORS
import platform, subprocess, distro , psutil

app = Flask(__name__)
CORS(app)

#@app.route("/")
#def index():

@app.route("/cpu", methods=['GET'])
def get_cpu_info():
    ######################### CPU #########################
    # cpu var
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_count_physique = psutil.cpu_count(logical=False)
    cpu_per = psutil.cpu_percent(interval=1, percpu=True)
    main_core = cpu_per.index(max( cpu_per ))
    freq = psutil.cpu_freq().current
    # cpu 
    cpu_info = {
    "CPU Usage": cpu_usage,
    "Freqency Mhz": freq,
    "CPU cores": cpu_count,
    "Physical cores": cpu_count_physique,
    "Main CPU Core": main_core}

    return jsonify(cpu_info)

@app.route("/memory", methods=['GET'])
def get_memory_info():
    ######################### Memory #########################
    # memory var 
    memory =psutil.virtual_memory()
    total = humanize.naturalsize(memory.total)
    available = humanize.naturalsize(memory.available)
    used = humanize.naturalsize(memory.used)
    usage_per = memory.percent
    available_per = round ( (memory.available / memory.total)* 100 ,1)
    # memory print 
    memory_info = {
    "Total Memory": total,
    "Available Memory": available,
    "Used Memory": used,
    "Available Memory per %": available_per,
    "Used Memory per % " : usage_per}

    return jsonify(memory_info)

@app.route("/battery", methods=['GET'])
def get_battery_info():
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
        battery_info ={
            "Battery Percentage ": " N/A ",
            "Plugged in ": " N/A ",
            "Charging time": " N/A ",
            "Remaining time " : " N/A ",
            "Status" : Status
        }
    else :
        #print(f"Battery Percentage: {percent}%")
        #print(f"Plugged in: {plugged}")
        if plugged :
            #print(f"Charging time: {Charging_time}")
            if percent < 100 :
                Status = "Currently charging"
            if percent == 0 :
                Status = "Dead"
            else :
                Status = "Fully charged"
            battery_info ={
            "Battery Percentage ": percent,
            "Plugged in ": plugged,
            "Charging time": Charging_time,
            "Remaining time " : " N/A ",
            "Status" : Status }
        else :
            if percent < 100 :
                #print(f"Remaining time : {time_left}")
                Status = "Discharging"
                battery_info ={
                "Battery Percentage ": percent,
                "Plugged in ": plugged,
                "Charging time": Charging_time,
                "Remaining time " : time_left,
                "Status" : Status }
            else :
                Status = "Fully charged"
                battery_info ={
                "Battery Percentage ": percent,
                "Plugged in ": plugged,
                "Charging time": Charging_time,
                "Remaining time " : " N/A ",
                "Status" : Status }
    #print (f"Status: {Status}")
    return jsonify(battery_info)

@app.route("/general", methods=['GET'])
def get_general_info():
    ######################### General System information #########################
    # var
    system_platform = platform.system()
    system_architecture = platform.machine()
    operating_system = platform.uname().system
    operating_system_release = platform.uname().release
    system_date = datetime.date.today().strftime('%Y-%m-%d')
    system_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    processor_info = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq | awk -F ':' '{print $2}'",
                                         shell=True).decode().strip()

    dist_info = distro.linux_distribution()
    dist_name = dist_info[0]
    dist_version = dist_info[1]
    dist_id = dist_info[2]

    # print 
    system_info = {
    "System Platform": system_platform,
    "System Architecture": system_architecture,
    "Operating System": operating_system,
    "Operating System Release": operating_system_release,
    "System Date": system_date,
    "System Time": system_time,
    "Processor": processor_info,
    "Distribution Name": dist_name,
    "Distribution Version": dist_version,
    "Distribution ID": dist_id }

    return jsonify (system_info)

@app.route("/disk", methods=['GET'])
def get_disk_info():
    ########################### Disk ############################################
    partitions = psutil.disk_partitions(all=False)
    partition_dict={}
    partition_info=[]

    #print("----- Partitions -----")
    for partition in partitions:
        partition_dict = {
        "Device": partition.device,
        "Mountpoint": partition.mountpoint,
        "File System Type": partition.fstype,
        "Mount Options": partition.opts}
        partition_info.append(partition_dict)

    disk = psutil.disk_usage("/")
    per_usage_disk = disk.percent
    free_disk = humanize.naturalsize(disk.free)
    used_disk = humanize.naturalsize(disk.used)
    total_disk = humanize.naturalsize(disk.total)

    disk_usage_info = {
    "Percentage Used": per_usage_disk,
    "Free Space": free_disk,
    "Used Space": used_disk,
    "Total Space": total_disk}

    return jsonify(partition_info,disk_usage_info)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
