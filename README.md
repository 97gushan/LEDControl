# LEDControl
A program to control a LED strip connected to a Raspberry Pi. 

The Raspberry pi controls a relay via a Python script. This script is in turned called by a PHP script from an Apache server where the user controls a button.
Two python scripts are also executed via Cron where the effect is that the lights turns on when the sun goes down and off when the sun rises again.
