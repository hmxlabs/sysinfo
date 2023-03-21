import os
import psutil
import json
from cpuinfo import get_cpu_info


RESULTS_FILE = "sysinfo.json"

cpu_count = os.cpu_count()
cpu_info = get_cpu_info()
core_count = psutil.cpu_count(logical=False)  # This will get the number of physical CPUs regardless of whehter HT/ SMT is enabled or not
mem = psutil.virtual_memory()
arch = cpu_info["arch"]
cpu_f = psutil.cpu_freq(percpu=False)
cpu_vendor = cpu_info["vendor_id_raw"]
cpu_model = cpu_info["brand_raw"]
cpu_freq = cpu_info["hz_advertised"][0]
cpu_freq_act = cpu_info["hz_actual"][0]


results = {
    "core_count": core_count,
    "cpu_count": cpu_count,
    "cpu_vendor": cpu_vendor,
    "cpu_model": cpu_model,
    "cpu_frequency": cpu_freq,
    "cpu_frequency_actual": cpu_freq_act,
    "cpu_freq_min": cpu_f.min,
    "cpu_freq_max": cpu_f.max,
    "installed_memory":  mem.total,
    "py_cpuinfo": cpu_info
}

with open(RESULTS_FILE, 'a') as res_file:
    res_file.write(json.dumps(results))