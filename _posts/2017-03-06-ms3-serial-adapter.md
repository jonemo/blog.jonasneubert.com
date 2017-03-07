---
layout: post
title: MS3 Adapter for Serial Port and Power
tags:
 - pycon
 - robotics
 - factorytech
 - serial
published: true
date: Mar 6th, 2017
---

In last week's post [about barcode readers]({{ site.url }}/2017/02/26/intro-to-barcode-readers) I mentioned that I purchased an [MS3 from Microscan](http://www.microscan.com/en-us/products/laser-barcode-scanners/ms-3-compact-laser-barcode-scanner) for my PyCon demo.
What I had forgotten from last time I worked with the MS3 is that the pin-out of cable attached to the barcode reader is not just a DB9 (nine pin) serial port connector but a DB15 (VGA style) plug.
Those extra pins are used for sending power to the device and to accommodate a few extra features, namely trigger and reset inputs.

For the rich folk among us, Microscan sells an adapter, but since I'm on a budget I am going to cobble together my own.
I have designed a PCB to do this job once before, but that was for work and I while that board layout wasn't exactly the crown jewel of that company, I can't just publish it for the world to see.
So I sat down and whipped up a version of this adapater from scratch, including a couple of neat extra features.

The final (not yet tested) outcome of this Sunday afternoon is [on Github](https://github.com/jonemo/ms3-adapter).

This is what's in the box:
* 5.5mm center positive barrel connector for 5VDC power supply
* DB9 connector for PC connection and DB15 connector for barcode reader connection
* RS-232 [null modem with loopback handshacking](https://en.wikipedia.org/wiki/Null_modem#Loopback_handshaking)
* Holder for 5mm fuse in power supply line
* Indicator LEDs for power, data in, and data out
* Momentary buttons for pulling the reset and trigger lines to `GND`

I tried to source all parts from Sparkfun, mainly for the convenience of being able to use [Sparkfun's Eagle component footprint libraries](https://github.com/sparkfun/SparkFun-Eagle-Libraries) to speed up the design process.
I was almost successful with the exception of the DB15 connector of which Sparkfun doesn't sell one.

The board design is off to OSHPark for quick turn processing, which means the barcode reader should finally be ready for testing in a week or so.