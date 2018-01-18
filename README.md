# 433Mhz Socket Actor Plugin for CraftBeerPi 3.0

## Supported 433Mhz Socket

* Silvercrest RCR DP3 3711-A

## Installation

You need to have a typical cheap 433Mhz sender installed on GPIO Pin 0 (default for 433Utils).
You need wiringPi installed, but the craftbeerpi setup can do this for you.

Install 433Utils
```bash
git clone --recursive git://github.com/ninjablocks/433Utils.git
cd 433Utils/RPi_utils
make
```

Just download via CraftBeerPi Web Interface and restart CraftBeerPi.

## Actor Configuration

### SilverCrest433Mhz (hardcoded)
You can use an actor with hardcoded values.
You need to train your sockets to know these values.
Select "Silvercrest433Mhz" actor and select a socket.
Simply put the receivers in a power socket and trigger "on" of your actor within 30 seconds.


### Selflearning

You need known values to be sent as an on or off signal.
You can use RFSniffer from 433Utils to find out.
