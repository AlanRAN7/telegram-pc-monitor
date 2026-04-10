import time
import psutil
import subprocess
import wmi

def bytes2human(n):
    symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if abs(n) >= prefix[s]:
            value = float(n) / prefix[s]
            return "{:.1f}{}".format(value, s)
    return "{}B".format(n)

def everyTemperaturaCoreInTheCPU():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        for sensor in w.Sensor():
            if sensor.SensorType == u'Temperature':
                print(sensor.Name, sensor.Value)
    except Exception as e:
        print("No se pudo obtener temperatura:", e)

def getCPUPercent():
    return psutil.cpu_percent(interval=1)


def get_ram_usage():
    ram = psutil.virtual_memory()
    
    return {
        "total": bytes2human(ram.total),
        "used": bytes2human(ram.used),
        "free": bytes2human(ram.available),
        "percent": ram.percent
    }



def get_gpu_usage():
    result = subprocess.check_output(
        ["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"]
    )
    
    used, total = result.decode("utf-8").strip().split(", ")
    
    return int(used), int(total)


def get_gpu_temperature():
    result = subprocess.check_output(
        ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"]
    )
    
    temp = result.decode("utf-8").strip()
    return int(temp)


def get_system_status():
    cpu = getCPUPercent()
    ram = get_ram_usage()
    gpu_used, gpu_total = get_gpu_usage()
    gpu_temp = get_gpu_temperature()

    return {
        "cpu": cpu,
        "ram": ram,
        "gpu": {
            "used": gpu_used,
            "total": gpu_total,
            "temp": gpu_temp
        }
    }