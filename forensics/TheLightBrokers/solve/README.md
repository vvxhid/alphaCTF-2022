# The Light Brokers

- Challenge Name: `The Light Brokers`
- Description: `Hello back fellow hacker, we got our hands on another leak from thelightbrokers NSA hack. This time it is an encrypted zip archive with NSA hacking tools we tried to crack it with all wordlists that we had but it was all in veins. But we all know you are no ordinary hacker, it shouldn't take you anytime to get the decrypted files.`
- Files: nsa_hacking_tools.zip

## Solution

When we check the encryption method used by the zip file:

```
$ 7z l -slt nsa_hacking_tools.zip
```

We can see that it's using legacy encryption (`Method = ZipCrypto Store`) and not AES, this encryption is vulnerable to known plaintext attack.

We can use bkcrack tool to decrypt the archive with putty-076.tar.gz (downloaded from official website) as the known plaintext.

```sh
$ zip -0 putty.zip putty-0.76.tar.gz
$ bkcrack -C ./nsa_hacking_tools.zip -c 'putty-0.76.tar.gz' -P putty.zip -p putty-0.76.tar.gz
bkcrack 1.3.4 - 2022-01-07
[15:26:52] Z reduction using 1048568 bytes of known plaintext
3.8 % (39396 / 1048568)
[15:26:54] Attack on 68 Z values at index 1009450
Keys: 5f977144 2a270ab6 e28fcd73
29.4 % (20 / 68)
[15:26:55] Keys
5f977144 2a270ab6 e28fcd73
$ bkcrack -C ./nsa_hacking_tools.zip -c 'flagger.sh' -k 5f977144 2a270ab6 e28fcd73 -d flagger.sh
$ ./flagger.sh
alphaCTF{c4nt_B3l1ev3_NS4_1s_Us1Ng_Z1PL3gacy_3NCryptiong}
```
