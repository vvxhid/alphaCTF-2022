# Solution

The `challenge.ods` file has some hidden and locked columns. decompress the file with `unzip challenge.ods` <br>
`grep -Ri . | grep "pass"` you will notice that there is a password inside `content.xml` <br>
use the password the extract the content of `secret.pdf.zip` <br>
`binwalk --dd='.*' secret.pdf` you will find a zip named `883` unzip it and you will get the file <br>
containing the flag.