## AirgapBender

- Challenge Name: `Airgap Bender`

## Solution

We can notice on the network capture some wifi beacon packets that has a changing source address each 10~ packet, if we concatinate the changing parts of the source address and remove the duplicates and we get the flag

```sh
$ tshark -r ./capture.pcapng -Y 'wlan.ssid == "FancyCozyBear28"' -Tfields -e wlan.sa|sed -n '$!N; /^\(.*\)\n\1$/!P; D'|cut -d':' -f3,4 |tr -d ':\n' |xxd -r -p
```
