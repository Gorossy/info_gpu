from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetPciInfo, nvmlShutdown, nvmlDeviceGetUUID, nvmlShutdown, nvmlDeviceGetCount
# Initialize NVML
nvmlInit()
# Get the number of GPUs
device_count = nvmlDeviceGetCount()
# Retrieve and print UUIDs
for i in range(device_count):
    handle = nvmlDeviceGetHandleByIndex(i)
    pci_info = nvmlDeviceGetPciInfo(handle)
    uuid = nvmlDeviceGetUUID(handle)
    print(f"GPU Index: {i}")
    print(f"- PCI Device ID: {pci_info}")  # Hex format
    print(f"- GPU {i}: {uuid}")
# Shutdown NVML
nvmlShutdown()