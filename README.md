# sysinfo
Platform / OS agnostic (hopefully!) way to get basic information such as disk size, RAM, CPU count, SMT Status

Really nothing clever, just uses psutil and py-cpuinfo under the cover but fairly handy for some of our use cases

Can be run from the command line as

    python3 -m hmxlabs.sysinfo [--file] [--filename]

Can be used from python as:

    from hmxlabs.sysinfo import sysinfo

    results = sysinfo.get_sysinfo()