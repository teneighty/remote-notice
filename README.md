# remote-notice

Simple server that takes json messages and sends them to dbus.

## Example
Try running

    ./remote-notice.py -p 33333

Then:

    echo "{ \"title\" : \"Stewie\", \"msg\" : \"You must be shrooming.\" } " | nc localhost 33333

## Usage

I usually run irssi in a screen session on my destop. When I am on my laptop I
run this server and RemoteForward 33333 in my ssh connection.  Lastly, I load
`scripts/irssi/notify.pl` into my remote `.irssi/scripts`. Now when new IRC
messages come in, I will receive desktop notifcations.

