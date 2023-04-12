def extract_cpu_times(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    cpu_times = []
    for line in lines:
        if line.startswith("CPU-time:"):
            cpu_time = float(line.split()[1])
            cpu_times.append((cpu_time, line))
            print(cpu_times)
    return cpu_times

def sort_cpu_times(cpu_times):
    return sorted(cpu_times, key=lambda x: x[0])

filename = "C:\codewithme\doc_exercises\efficiency.txt"
cpu_times = extract_cpu_times(filename)
sorted_cpu_times = sort_cpu_times(cpu_times)

for cpu_time, line in sorted_cpu_times:
    print(line.strip())



