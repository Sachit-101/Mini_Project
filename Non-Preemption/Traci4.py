# ------------------------------
# Normal Traffic Light Operation
# No Emergency Priority
# ------------------------------

import os
import sys

# Step 1: Load SUMO Tools
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

import traci

# Step 2: SUMO Configuration
sumo_cmd = [
    "sumo-gui",
    "-c", "Test1.sumocfg",
    "--step-length", "0.05",
    "--delay", "1000",
    "--lateral-resolution", "0.1"
]

# Step 3: Start TraCI Connection
traci.start(sumo_cmd)

# Step 4: Simulation Loop
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    # No priority, no traffic light manipulation — everything runs normally

# Step 5: Close TraCI
traci.close()
