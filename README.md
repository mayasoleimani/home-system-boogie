# home-system-boogie

This project is designed to practice my networking and cloud knowledge by creating an at home virtual lab, post passing my CCNA exam and studying for AWS SAA-C03. Concepts used in this project include network and cloud architecture, automation, and monitoring. home-system-boogie aims to create a network using automation scripting instead of setting up the process manually. At the completion of the system, there will be a monitoring period looking specifically at latency and up-time metrics. This project aims to answer the problem of how to host your own simulated network (AWS and GNS3), create network automation scripts (Netmiko), and monitor the system's behavior (Grafana and Prometheus)

### Applications used:
* GNS3
* Netmiko
* AWS VPC and EC2
* Prometheus
* Grafana

### Phases
* Phase 1: Setup network topology in GNS3. Confirm connection from GNS3 domain to network on local PC using ping and SSH. Write Netmiko script to automate configuration tasks like VLAN setup, interface setup, etc. Additionally, setup Github repository to track project process
* Phase 2: Cloud Networking
* Phase 3: Monitoring


### Troubleshooting:

In phase 1, I was having  trouble trying to ping my local terminal from the router inside GNS3. I tried using every ethernet adapter my computer had to offer but nothing was working. Finally, I followed this guide on the official GNS3 website (https://www.gns3.com/community/support/can-t-ping-local-pc-to-gns3-usin) which instructed me to uninstall ncap and download winpcap 4.1.3. After doing this, I had successful pings and was able to SSH into the terminal on my local machine.

When I put the project down and come back to it, I ping the routers from my terminal to check my connection. Often when it's been a while since I worked on the project and come back, I do not get successful pings. The solution to this was restarting GNS3.

Regular SSH command is not working on my PC terminal, had to add some parameters:
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa -oCiphers=+aes128-cbc -oMACs=+hmac-sha1 maya@172.16.10.10
