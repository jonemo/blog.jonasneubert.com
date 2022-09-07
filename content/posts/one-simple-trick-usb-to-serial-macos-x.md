---
slug: one-simple-trick-usb-to-serial-macos-x
date: "2017-03-07T00:00:00Z"
published: true
tags:
- factorytech
- barcodes
title: One simple trick for USB-to-Serial on MacOS X
---

Call me a Luddite if you wish, but I lament the lack of serial ports in modern laptops.

My relationship with USB-to-Serial cables has been one of disappointments, crashed computers, and garbled data. The one I pulled out of a drawer this week randomly flipped the most significant bit of every character. How do I know this? Because I wasted three long nights debugging the problem.

But I'm a changed person now because I learned this one amazing trick for making USB-to-Serial _just work_ on macOS:

**Use a version of macOS newer than 10.9 and use a cable with FTDI chip.**

Do this and you will never have to fuzz around with manually installing drivers from shady websites! And you can now unplug the USB-to-Serial cable while your computer is sleeping without provoking a crash -- amazing!

## macOS >= 10.9 comes with (working) FTDI drivers

macOS includes kernel drivers for FTDI chips as of version 10.9, aka "Mavericks", released in 2013. I can't find the Engadget article about the five minute time slot Phil Schiller devoted to announcing this revolutionary innovation at WWDC, but [here is the official Apple tech note](https://developer.apple.com/library/content/technotes/tn2315/_index.html).

I had no idea because the last time I tried using a USB-to-Serial cable on macOS was with version 10.8.


## FTDI vs. Prolific

Admittedly, I'm less certain about this part of the amazing trick.

As far as I am aware, there are only two manufacturers of USB-to-Serial converter chips at the moment: [FTDI](http://www.ftdichip.com/) and [Prolific](http://www.prolific.com.tw/). These companies design the silicone that lives inside a small black box that lives on a printed circuit board that lives inside your converter cable. The cable is made by a different manufacturer, but the product description usually tells you which "chipset" is embedded in the cable.

My anecdotal evidence is that the cable with the Prolific chip paired with the [Prolific driver from the Prolific website](http://www.prolific.com.tw/us/showproduct.aspx?p_id=229&pcid=41) gave me the garbled data, while the FTDI cable with no extra effort has been working great.

Therefore, the cable with the Prolific chip now lives at Ox Mountain (the local landfill) while the cable with the FTDI chip will be used to connect to a barcode reader.


## Other USB-to-Serial Trivia

* FTDI stands for Future Technology Devices International Ltd. and is headquartered in Scotland.
* There are two types of drivers for FTDI chips: The VCP driver (Virtual COM Port) makes a port show up that can be used by any program as if it were a serial port. There's also a version that comes as a DLL and is meant for being bundled with device software.
* Every serial device shows up as two entries in `/dev`, one starting with `cu.` and another starting with `tty.`. [This Stackoverflow post](http://stackoverflow.com/questions/8632586/macos-whats-the-difference-between-dev-tty-and-dev-cu) explains the history of that in a way that does not assume prior knowledge of pre-internet style networking. Because most modern RS232 devices don't even have the hardware flow control lines connected, `tty` and `cu` usually behave identically. But when they don't, `cu` is usually the device you want to open, as explained in [this SO thread](http://stackoverflow.com/questions/26498582/opening-a-serial-port-on-os-x-hangs-forever-without-o-nonblock-flag).

