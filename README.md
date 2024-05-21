# Wide Area Network for Mock Bank - Project ReadMe

## Project Overview

This project involves setting up a Wide Area Network (WAN) for a mock bank, which includes three Local Area Networks (LANs), one of which will be partitioned into two Virtual LANs (VLANs). The goal is to configure all network devices and endpoints to communicate efficiently across the entire WAN.

## Requirements

- Advanced knowledge of networking concepts and the Cisco IOS.
- Use of Cisco Packet Tracer 8.2.1 or later.

## Tools and Resources

- Cisco Packet Tracer 8.2.1 or later.

### Task 1: Design an IP Address Scheme

1. Divide the 172.16.10.0/16 network into seven subnets.
2. Determine the new subnet mask.
3. Calculate the number of usable host addresses per subnet.
4. Fill in the addressing table with the resulting subnets.

### Task 2: Implement VLANs and Trunk

1. Create and name VLANs:
   - VLAN 10 – Management
   - VLAN 20 – Marketing
   - VLAN 30 – Accounting
   - VLAN 100 – Native
2. Configure the interfaces on S1-Office1 and S2-Office1 as "Access" mode and assign VLANs.
3. Configure the interconnecting link between S1-Office1 and S2-Office1 as "Trunk".
4. Verify the VLAN and trunk configurations using appropriate show commands and save the configuration.
5. Disable DTP on the access ports of both switches.

### Task 3: Assign IP Addresses

1. Assign IP addresses to the subnets as planned.
2. Document the IP address assignment in a separate file.
3. Configure the Router-on-a-Stick setup for VLANs.
4. Assign the default gateways for each VLAN.

### Task 4: Configure R1 for Inter-VLAN Routing

1. Enable GigabitEthernet 0/0.
2. Create sub-interfaces on GigabitEthernet 0/0.
3. Set the correct encapsulation type and VLAN ID for each sub-interface.
4. Configure IP addresses and subnet masks.
5. Verify the configuration using appropriate show commands and save it.
6. Set GigabitEthernet 0/1 on S1-Office1 as Trunk with the appropriate Native VLAN.
7. Test inter-VLAN routing by pinging between devices.

### Task 5: Static Routing for Network Devices

1. Configure IP addresses and subnet masks for all routers.
2. Set up static routing on all routers.
3. Configure a default route.

### Task 6: Initial and Security Settings for Network Devices

1. Create a user account with the following credentials:
   - Username: Admin
   - Password: ACDC1973
2. Secure access to the console line.
3. Secure privileged mode access with the password: beatles1960.
4. Encrypt all passwords on the device.
5. Configure a security message (MOTD Banner).

### Task 7: Secure Remote Access

1. Configure SSHv2 services on all routers.
2. Set the IP domain name to AAST.com.
3. Generate secure keys (minimum key length: 1024 bits).
4. Configure VTY lines for SSH access.
5. Verify the configuration using appropriate show commands.
6. Configure the correct default gateway on the Admin PC and test SSH access.
