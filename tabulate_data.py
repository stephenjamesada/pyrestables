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
    [f"{green}user{reset}", bytes2human(cpu_times.user)],
    [f"{green}nice{reset}", bytes2human(cpu_times.nice)],
    [f"{green}system{reset}", bytes2human(cpu_times.system)],
    [f"{green}idle{reset}", bytes2human(cpu_times.idle)],
    [f"{green}iowait{reset}", bytes2human(cpu_times.iowait)],
    [f"{green}interrupt request{reset}", bytes2human(cpu_times.irq)],
    [f"{green}soft interrupt request{reset}", bytes2human(cpu_times.softirq)],
    [f"{green}steal{reset}", bytes2human(cpu_times.steal)],
    [f"{green}guest{reset}", bytes2human(cpu_times.guest)],
    [f"{green}guest nice{reset}", bytes2human(cpu_times.guest_nice)]
]

cpu_statistics = [
    [f"{green}ctx switches{reset}", cpu_stats.ctx_switches],
    [f"{green}interrupts{reset}", cpu_stats.interrupts],
    [f"{green}soft interrupts{reset}", cpu_stats.soft_interrupts],
    [f"{green}syscalls{reset}", cpu_stats.syscalls]
]

cpu_frequencies = [
    [f"{green}current{reset}", cpu_freq.current],
    [f"{green}min{reset}", cpu_freq.min],
    [f"{green}max{reset}", cpu_freq.max]
]

cpu_average = [
    [f"{green}load average 1{reset}", load_average[0]],
    [f"{green}load average 2{reset}", load_average[1]],
    [f"{green}load average 3{reset}", load_average[2]]
]

# Memory

vir_mem = [
    [f"{green}total{reset}", bytes2human(virtual_memory.total)],
    [f"{green}available{reset}", bytes2human(virtual_memory.available)],
    [f"{green}percent{reset}", bytes2human(virtual_memory.percent)],
    [f"{green}used{reset}", bytes2human(virtual_memory.used)],
    [f"{green}free{reset}", bytes2human(virtual_memory.free)],
    [f"{green}active{reset}", bytes2human(virtual_memory.active)],
    [f"{green}inactive{reset}", bytes2human(virtual_memory.inactive)],
    [f"{green}buffers{reset}", bytes2human(virtual_memory.buffers)],
    [f"{green}cached{reset}", bytes2human(virtual_memory.cached)],
    [f"{green}shared{reset}", bytes2human(virtual_memory.shared)],
    [f"{green}slab{reset}", bytes2human(virtual_memory.slab)]
]

swap_mem = [
    [f"{green}total{reset}", bytes2human(swap_memory.total)],
    [f"{green}used{reset}", bytes2human(swap_memory.used)],
    [f"{green}free{reset}", bytes2human(swap_memory.free)],
    [f"{green}percent{reset}", f"{swap_memory.free:.2%}"],
    [f"{green}swap-in{reset}", bytes2human(swap_memory.sin)],
    [f"{green}swap-out{reset}", bytes2human(swap_memory.sout)]
]

# Disk

dsk_usg = [
    [f"{green}total{reset}", bytes2human(disk_usage.total)],
    [f"{green}used{reset}", bytes2human(disk_usage.used)],
    [f"{green}free{reset}", bytes2human(disk_usage.free)],
    [f"{green}percent{reset}", f"{disk_usage.percent:.2%}"]
]
