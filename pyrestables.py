from tabulate import tabulate
import tabulate_data
import argparse
import pyfiglet
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

green = Fore.GREEN
blue = Fore.BLUE
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
                    help="Outputs all parsable system information"
)

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
                     help="Outputs total CPU count"
)

parser.add_argument("--cpu-frequency",
                    action="store_true",
                    help="Outputs current, minimum, and maximum CPU frequencies"
)

parser.add_argument("--cpu-average",
                    action="store_true",
                    help="Outputs CPU average")

parser.add_argument("--cpu-all",
                    action="store_true",
                    help="Outputs all CPU-related information"
)

parser.add_argument("--virtual-mem",
                    action="store_true",
                    help="Outputs virtual memory statistics")

parser.add_argument("--swap-mem",
                    action="store_true",
                    help="Outputs swap memory statistics")

parser.add_argument("--disk-usage",
                    action="store_true",
                    help="Outputs current disk usage on the system")

args = parser.parse_args()

if args.general_info:
    clear()
    print(figlet.renderText("System Info"))
    print("━" * 56)
    print(f"\n{system_information}\n")
elif args.cpu_stats:
    clear()
    print(figlet.renderText("CPU Stats"))
    print("━" * 43)
    print(f"\n{cpu_stat}\n")
elif args.cpu_time:
    clear()
    print(figlet.renderText("CPU Times"))
    print("━" * 48)
    print(f"\n{cpu_time}\n")
elif args.cpu_count:
    clear()
    print(figlet.renderText("CPU Count"))
    print("━" * 48)
    print(f"\n{cpu_counts}\n")
elif args.cpu_frequency:
    clear()
    print(figlet.renderText("CPU Frequencies"))
    print("━" * 75)
    print(f"\n{cpu_freqs}\n")
elif args.cpu_average:
    clear()
    print(figlet.renderText("CPU Average"))
    print("━" * 57)
    print(f"\n{cpu_aver}\n")
elif args.cpu_all:
    clear()
    print(figlet.renderText("All CPU Info"))
    print(f"\n{cpu_stat}\n{cpu_time}\n{cpu_counts}\n{cpu_freqs}\n{cpu_aver}")
elif args.virtual_mem:
    clear()
    print(figlet.renderText("Virtual Memory"))
    print("━" * 75)
    print(f"\n{virt_mem}\n")
elif args.swap_mem:
    clear()
    print(figlet.renderText("Swap Memory"))
    print("━" * 66)
    print(f"\n{swap_mem}\n")
elif args.disk_usage:
    clear()
    print(figlet.renderText("Disk Usage"))
    print("━" * 47)
    print(f"\n{dsk_usg}\n")
elif args.all:
    clear()
    print(figlet.renderText("System Info"))
    print("━" * 56)
    print(f"\n{system_information}\n")
    print(figlet.renderText("CPU Stats"))
    print("━" * 43)
    print(f"\n{cpu_stat}\n")
    print(figlet.renderText("CPU Times"))
    print("━" * 48)
    print(f"\n{cpu_time}\n")
    print(figlet.renderText("CPU Count"))
    print("━" * 48)
    print(f"\n{cpu_counts}\n")
    print(figlet.renderText("CPU Frequencies"))
    print("━" * 75)
    print(f"\n{cpu_freqs}\n")
    print(figlet.renderText("CPU Average"))
    print("━" * 57)
    print(f"\n{cpu_aver}\n")
    print(figlet.renderText("Virtual Memory"))
    print("━" * 75)
    print(f"\n{virt_mem}\n")
    print(figlet.renderText("Swap Memory"))
    print("━" * 66)
    print(f"\n{swap_mem}\n")
    print(figlet.renderText("Disk Usage"))
    print("━" * 47)
    print(f"\n{dsk_usg}\n")
else:
    clear()
    print(figlet.renderText("System Info"))
    print("━" * 56)
    print(f"\n{system_information}\n")
    print(figlet.renderText("CPU Stats"))
    print("━" * 43)
    print(f"\n{cpu_stat}\n")
    print(figlet.renderText("CPU Times"))
    print("━" * 48)
    print(f"\n{cpu_time}\n")
    print(figlet.renderText("CPU Count"))
    print("━" * 48)
    print(f"\n{cpu_counts}\n")
    print(figlet.renderText("CPU Frequencies"))
    print("━" * 75)
    print(f"\n{cpu_freqs}\n")
    print(figlet.renderText("CPU Average"))
    print("━" * 57)
    print(f"\n{cpu_aver}\n")
    print(figlet.renderText("Virtual Memory"))
    print("━" * 75)
    print(f"\n{virt_mem}\n")
    print(figlet.renderText("Swap Memory"))
    print("━" * 66)
    print(f"\n{swap_mem}\n")
    print(figlet.renderText("Disk Usage"))
    print("━" * 47)
    print(f"\n{dsk_usg}\n")
        
"""
I recommend you use a pager when you run this flagless, or when you run the "--all" flag.
"""
