import platform
import psutil
from psutil._common import bytes2human
import colorama
from colorama import Fore, Back, Style

green = Fore.GREEN
reset = Style.RESET_ALL

cpu_times = psutil.cpu_times()
cpu_stats = psutil.cpu_stats()
cpu_freq = psutil.cpu_freq()
load_average = psutil.getloadavg()
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
disk_usage = psutil.disk_usage('/')

gen_sys = [
    [f"{green}system{reset}", f"{green}{platform.system()}{reset}"],
    [f"{green}machine{reset}", f"{green}{platform.machine()}{reset}"],
    [f"{green}node{reset}", f"{green}{platform.node()}{reset}"],
    [f"{green}platform{reset}", f"{green}{platform.platform()}{reset}"],
    [f"{green}processor{reset}", f"{green}{platform.processor()}{reset}"],
    [f"{green}release{reset}", f"{green}{platform.release()}{reset}"],
]

# CPU

count_cpu = [
    ["cpu count", psutil.cpu_count()]
]

cpu_times = [
    ["user", bytes2human(cpu_times.user)],
    ["nice", bytes2human(cpu_times.nice)],
    ["system", bytes2human(cpu_times.system)],
    ["idle", bytes2human(cpu_times.idle)],
    ["iowait", bytes2human(cpu_times.iowait)],
    ["interrupt request", bytes2human(cpu_times.irq)],
    ["soft interrupt request", bytes2human(cpu_times.softirq)],
    ["steal", bytes2human(cpu_times.steal)],
    ["guest", bytes2human(cpu_times.guest)],
    ["guest nice", bytes2human(cpu_times.guest_nice)]
]

cpu_statistics = [
    ["ctx switches", cpu_stats.ctx_switches],
    ["interrupts", cpu_stats.interrupts],
    ["soft interrupts", cpu_stats.soft_interrupts],
    ["syscalls", cpu_stats.syscalls]
]

cpu_frequencies = [
    ["current", cpu_freq.current],
    ["min", cpu_freq.min],
    ["max", cpu_freq.max]
]

cpu_average = [
    ["load average 1", load_average[0]],
    ["load average 2", load_average[1]],
    ["load average 3", load_average[2]]
]

# Memory

vir_mem = [
    ["total", bytes2human(virtual_memory.total)],
    ["available", bytes2human(virtual_memory.available)],
    ["percent", bytes2human(virtual_memory.percent)],
    ["used", bytes2human(virtual_memory.used)],
    ["free", bytes2human(virtual_memory.free)],
    ["active", bytes2human(virtual_memory.active)],
    ["inactive", bytes2human(virtual_memory.inactive)],
    ["buffers", bytes2human(virtual_memory.buffers)],
    ["cached", bytes2human(virtual_memory.cached)],
    ["shared", bytes2human(virtual_memory.shared)],
    ["slab", bytes2human(virtual_memory.slab)]
]

swap_mem = [
    ["total", bytes2human(swap_memory.total)],
    ["used", bytes2human(swap_memory.used)],
    ["free", bytes2human(swap_memory.free)],
    ["percent", f"{swap_memory.free:.2%}"],
    ["swap-in", bytes2human(swap_memory.sin)],
    ["swap-out", bytes2human(swap_memory.sout)]
]

# Disk

dsk_usg = [
    ["total", bytes2human(disk_usage.total)],
    ["used", bytes2human(disk_usage.used)],
    ["free", bytes2human(disk_usage.free)],
    ["percent", f"{disk_usage.percent:.2%}"]
]
