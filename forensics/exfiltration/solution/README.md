# Solution 

So after opening the pcap file in `wireshark` you will notice that there are a lot of <br>
communications between the host with the ip address `192.168.1.113` and `172.19.0.2` <br>
After inspecting few packets you will see that the first four bytes which were sent are `89 50 4E 47` <br> 
which corresponds to png image magic numbers. <br>
extract data with: <br>
`tshark -r traffic.pcapng -Y "ip.src == 192.168.1.113 and ip.dst == 172.19.0.2" -Tfields -e data > packets.txt` <br>

and parse it you will get an image which contains the flag.
