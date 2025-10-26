#!/usr/bin/env python3

from tabulate import tabulate
import tabulate_data
import argparse
import pyfiglet
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

green = Fore.GREEN
reset = Style.RESET_ALL

figlet = pyfiglet.Figlet()

def clear():
    print("\033c", end="")

system_information = tabulate(tabulate_data.gen_sys, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt=f"simple_outline")
cpu_stat = tabulate(tabulate_data.cpu_statistics, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
cpu_time = tabulate(tabulate_data.cpu_times, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
cpu_counts = tabulate(tabulate_data.count_cpu, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
cpu_freqs = tabulate(tabulate_data.cpu_frequencies, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
cpu_aver = tabulate(tabulate_data.cpu_average, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
virt_mem = tabulate(tabulate_data.vir_mem, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
swap_mem = tabulate(tabulate_data.swap_mem, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")
dsk_usg = tabulate(tabulate_data.dsk_usg, headers=[f"{green}key{reset}", f"{green}value{reset}"], tablefmt="simple_outline")

parser = argparse.ArgumentParser(description="Pythonic resource tables.")

parser.add_argument("--all",
                    action="store_true",
                    help="Outputs all parsable system information")

parser.add_argument("--general-info",
                     action="store_true",
                     help="Outputs general information about the system")

parser.add_argument("--cpu-stats",
                     action="store_true",
                     help="Outputs CPU statistics")

parser.add_argument("--cpu-time",
                     action="store_true",
                     help="Outputs CPU times")

parser.add_argument("--cpu-count",
                     action="store_true",
                     help="Outputs total CPU count")

parser.add_argument("--cpu-frequency",
                    action="store_true",
                    help="Outputs current, minimum, and maximum CPU frequencies")

parser.add_argument("--cpu-average",
                    action="store_true",
                    help="Outputs CPU average")

parser.add_argument("--cpu-all",
                    action="store_true",
                    help="Outputs all CPU-related information")

parser.add_argument("--virtual-mem",
                    action="store_true",
                    help="Outputs virtual memory statistics")

parser.add_argument("--swap-mem",
                    action="store_true",
                    help="Outputs swap memory statistics")

parser.add_argument("--disk-usage",
                    action="store_true",
                    help="Outputs current disk usage on the system")

parser.add_argument("--active-nets",
                    action="store_true",
                    help="Outputs all active network interfaces with packet, error, and byte info")

args = parser.parse_args()

if args.general_info:
    clear()
    print(f"{green}{figlet.renderText("System Info")}{reset}")
    print("━" * 56)
    print(f"\n{system_information}\n")
elif args.cpu_stats:
    clear()
    print(f"{green}{figlet.renderText("CPU Stats")}{reset}")
    print("━" * 43)
    print(f"\n{cpu_stat}\n")
elif args.cpu_time:
    clear()
    print(f"{green}{figlet.renderText("CPU Times")}{reset}")
    print("━" * 48)
    print(f"\n{cpu_time}\n")
elif args.cpu_count:
    clear()
    print(f"{green}{figlet.renderText("CPU Count")}{reset}")
    print("━" * 48)
    print(f"\n{cpu_counts}\n")
elif args.cpu_frequency:
    clear()
    print(f"{green}{figlet.renderText("CPU Frequencies")}{reset}")
    print("━" * 75)
    print(f"\n{cpu_freqs}\n")
elif args.cpu_average:
    clear()
    print(f"{green}{figlet.renderText("CPU Average")}{reset}")
    print("━" * 57)
    print(f"\n{cpu_aver}\n")
elif args.cpu_all:
    clear()
    print(f"{green}{figlet.renderText("All CPU Info")}{reset}")
    print(f"\n{cpu_stat}\n{cpu_time}\n{cpu_counts}\n{cpu_freqs}\n{cpu_aver}")
elif args.virtual_mem:
    clear()
    print(f"{green}{figlet.renderText("Virtual Memory")}{reset}")
    print("━" * 75)
    print(f"\n{virt_mem}\n")
elif args.swap_mem:
    clear()
    print(f"{green}{figlet.renderText("Swap Memory")}{reset}")
    print("━" * 66)
    print(f"\n{swap_mem}\n")
elif args.disk_usage:
    clear()
    print(f"{green}{figlet.renderText("Disk Usage")}{reset}")
    print("━" * 47)
    print(f"\n{dsk_usg}\n")
elif args.active_nets:
    clear()
    print(f"{green}{figlet.renderText("Network Interfaces")}{reset}")
    print("━" * 47)
    print(f"\n{tabulate_data.active_net_interfaces()}\n")
elif args.all:
    clear()
    print(f"{green}{figlet.renderText("System Info")}{reset}")
    print("━" * 56)
    print(f"\n{system_information}\n")
    print(f"{green}{figlet.renderText("CPU Stats")}{reset}")
    print("━" * 43)
    print(f"\n{cpu_stat}\n")
    print(f"{green}{figlet.renderText("CPU Times")}{reset}")
    print("━" * 48)
    print(f"\n{cpu_time}\n")
    print(f"{green}{figlet.renderText("CPU Count")}{reset}")
    print("━" * 48)
    print(f"\n{cpu_counts}\n")
    print(f"{green}{figlet.renderText("CPU Frequencies")}{reset}")
    print("━" * 75)
    print(f"\n{cpu_freqs}\n")
    print(f"{green}{figlet.renderText("CPU Average")}{reset}")
    print("━" * 57)
    print(f"\n{cpu_aver}\n")
    print(f"{green}{figlet.renderText("Virtual Memory")}{reset}")
    print("━" * 75)
    print(f"\n{virt_mem}\n")
    print(f"{green}{figlet.renderText("Swap Memory")}{reset}")
    print("━" * 66)
    print(f"\n{swap_mem}\n")
    print(f"{green}{figlet.renderText("Disk Usage")}{reset}")
    print("━" * 47)
    print(f"\n{dsk_usg}\n")
    print(f"{green}{figlet.renderText("Network Interfaces")}{reset}")
    print("━" * 47)
    print(f"\n{tabulate_data.active_net_interfaces()}\n")
else:
    clear()
    print(f"{green}{figlet.renderText("System Info")}{reset}")
    print("━" * 56)
    print(f"\n{system_information}\n")
    print(f"{green}{figlet.renderText("CPU Stats")}{reset}")
    print("━" * 43)
    print(f"\n{cpu_stat}\n")
    print(f"{green}{figlet.renderText("CPU Times")}{reset}")
    print("━" * 48)
    print(f"\n{cpu_time}\n")
    print(f"{green}{figlet.renderText("CPU Count")}{reset}")
    print("━" * 48)
    print(f"\n{cpu_counts}\n")
    print(f"{green}{figlet.renderText("CPU Frequencies")}{reset}")
    print("━" * 75)
    print(f"\n{cpu_freqs}\n")
    print(f"{green}{figlet.renderText("CPU Average")}{reset}")
    print("━" * 57)
    print(f"\n{cpu_aver}\n")
    print(f"{green}{figlet.renderText("Virtual Memory")}{reset}")
    print("━" * 75)
    print(f"\n{virt_mem}\n")
    print(f"{green}{figlet.renderText("Swap Memory")}{reset}")
    print("━" * 66)
    print(f"\n{swap_mem}\n")
    print(f"{green}{figlet.renderText("Disk Usage")}{reset}")
    print("━" * 47)
    print(f"\n{dsk_usg}\n")
    print(f"{green}{figlet.renderText("Network Interfaces")}{reset}")
    print("━" * 47)
    print(f"\n{tabulate_data.active_net_interfaces()}\n")
    
"""
I recommend you use a pager when you run this flagless, or when you run the "--all" flag.
"""
