from dotenv import load_dotenv
import os

load_dotenv()

import asyncio
from scanner import robust_scan
from mapping import map_device_to_room

async def ble_scan_loop(logger):
    while True:
        scan_results = await robust_scan(logger)
        # Map scan results (e.g., RSSI or distance) to occupant IDs/rooms
        device_mapping = map_device_to_room(scan_results)
        for device, occupant in device_mapping.items():
            logger.info(f"Posting event: {device} mapped to {occupant}")
            # ...existing code for building service_data...
            # Example: post_event(logger, device, occupant)
        await asyncio.sleep(30)  # adjust scan interval as needed

async def main():
    # ...existing code...
    # Start BLE scanning loop alongside other tasks
    asyncio.create_task(ble_scan_loop(logger))
    # ...existing code...
    while True:
        await asyncio.sleep(3600)
# ...existing code...
