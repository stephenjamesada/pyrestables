import platform
import psutil
from psutil._common import bytes2human
import colorama
from colorama import Fore, Back, Style

green = Fore.GREEN
cyan = Fore.CYAN
reset = Style.RESET_ALL

cpu_times = psutil.cpu_times()
cpu_stats = psutil.cpu_stats()
cpu_freq = psutil.cpu_freq()
load_average = psutil.getloadavg()
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
disk_usage = psutil.disk_usage('/')

gen_sys = [
    [f"{green}system{reset}", f"{cyan}{platform.system()}{reset}"],
    [f"{green}machine{reset}", f"{cyan}{platform.machine()}{reset}"],
    [f"{green}node{reset}", f"{cyan}{platform.node()}{reset}"],
    [f"{green}platform{reset}", f"{cyan}{platform.platform()}{reset}"],
    [f"{green}processor{reset}", f"{cyan}{platform.processor()}{reset}"],
    [f"{green}release{reset}", f"{cyan}{platform.release()}{reset}"],
]

# CPU

count_cpu = [
    [f"{green}cpu count{reset}", f"{cyan}{psutil.cpu_count()}{reset}"]
]

cpu_times = [
    [f"{green}user{reset}", f"{cyan}{bytes2human(cpu_times.user)}{reset}"],
    [f"{green}nice{reset}", f"{cyan}{bytes2human(cpu_times.nice)}{reset}"],
    [f"{green}system{reset}", f"{cyan}{bytes2human(cpu_times.system)}{reset}"],
    [f"{green}idle{reset}", f"{cyan}{bytes2human(cpu_times.idle)}{reset}"],
    [f"{green}iowait{reset}", f"{cyan}{bytes2human(cpu_times.iowait)}{reset}"],
    [f"{green}interrupt request{reset}", f"{cyan}{bytes2human(cpu_times.irq)}{reset}"],
    [f"{green}soft interrupt request{reset}", f"{cyan}{bytes2human(cpu_times.softirq)}{reset}"],
    [f"{green}steal{reset}", f"{cyan}{bytes2human(cpu_times.steal)}{reset}"],
    [f"{green}guest{reset}", f"{cyan}{bytes2human(cpu_times.guest)}{reset}"],
    [f"{green}guest nice{reset}", f"{cyan}{bytes2human(cpu_times.guest_nice)}{reset}"]
]

cpu_statistics = [
    [f"{green}ctx switches{reset}", f"{cyan}{cpu_stats.ctx_switches}{reset}"],
    [f"{green}interrupts{reset}", f"{cyan}{cpu_stats.interrupts}{reset}"],
    [f"{green}soft interrupts{reset}", f"{cyan}{cpu_stats.soft_interrupts}{reset}"],
    [f"{green}syscalls{reset}", f"{cyan}{cpu_stats.syscalls}{reset}"]
]

cpu_frequencies = [
    [f"{green}current{reset}", f"{cyan}{cpu_freq.current}{reset}"],
    [f"{green}min{reset}", f"{cyan}{cpu_freq.min}{reset}"],
    [f"{green}max{reset}", f"{cyan}{cpu_freq.max}{reset}"]
]

cpu_average = [
    [f"{green}load average 1{reset}", f"{cyan}{load_average[0]}{reset}"],
    [f"{green}load average 2{reset}", f"{cyan}{load_average[1]}{reset}"],
    [f"{green}load average 3{reset}", f"{cyan}{load_average[2]}{reset}"]
]

# Memory

vir_mem = [
    [f"{green}total{reset}", f"{cyan}{bytes2human(virtual_memory.total)}{reset}"],
    [f"{green}available{reset}", f"{cyan}{bytes2human(virtual_memory.available)}{reset}"],
    [f"{green}percent{reset}", f"{cyan}{bytes2human(virtual_memory.percent)}{reset}"],
    [f"{green}used{reset}", f"{cyan}{bytes2human(virtual_memory.used)}{reset}"],
    [f"{green}free{reset}", f"{cyan}{bytes2human(virtual_memory.free)}{reset}"],
    [f"{green}active{reset}", f"{cyan}{bytes2human(virtual_memory.active)}{reset}"],
    [f"{green}inactive{reset}", f"{cyan}{bytes2human(virtual_memory.inactive)}{reset}"],
    [f"{green}buffers{reset}", f"{cyan}{bytes2human(virtual_memory.buffers)}{reset}"],
    [f"{green}cached{reset}", f"{cyan}{bytes2human(virtual_memory.cached)}{reset}"],
    [f"{green}shared{reset}", f"{cyan}{bytes2human(virtual_memory.shared)}{reset}"],
    [f"{green}slab{reset}", f"{cyan}{bytes2human(virtual_memory.slab)}{reset}"]
]

swap_mem = [
    [f"{green}total{reset}", f"{cyan}{bytes2human(swap_memory.total)}{reset}"],
    [f"{green}used{reset}", f"{cyan}{bytes2human(swap_memory.used)}{reset}"],
    [f"{green}free{reset}", f"{cyan}{bytes2human(swap_memory.free)}{reset}"],
    [f"{green}percent{reset}", f"{cyan}{swap_memory.free:.2%}{reset}"],
    [f"{green}swap-in{reset}", f"{cyan}{bytes2human(swap_memory.sin)}{reset}"],
    [f"{green}swap-out{reset}", f"{cyan}{bytes2human(swap_memory.sout)}{reset}"]
]

# Disk

dsk_usg = [
    [f"{green}total{reset}", f"{cyan}{bytes2human(disk_usage.total)}{reset}"],
    [f"{green}used{reset}", f"{cyan}{bytes2human(disk_usage.used)}{reset}"],
    [f"{green}free{reset}", f"{cyan}{bytes2human(disk_usage.free)}{reset}"],
    [f"{green}percent{reset}", f"{cyan}{disk_usage.percent:.2%}{reset}"]
]
