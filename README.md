# PyResTables

**PyResTables**, as the name suggests, is a resource monitoring system that outputs tables depending on the information of your system that you want to see.
It is entirely written in Python.

## Python Stack

- `psutil`
    - `bytes2human`
- `platform`
- `tabulate`
- `argparse`
- `colorama`

### How to Run

Here's how to run ***PyResTables***:

```
git clone https://github.com/stephenjamesada/pyrestables.git
cd pyrestables
pip install -r requirements.txt
python3 pyrestables.py
```

This will change as the project grows, but this is the quick, ubiquitous way.

#### Developer Notes

I used modules like `colorama` to get to know the common utilities used in tons of different Python projects.
I would've used Rich for styling, but I wanted this project to be simpler in its design, and to learn basics.
