---
date: "2017-03-13T00:00:00Z"
published: true
tags:
- pycon
- robotics
- factorytech
title: 'PyCon Talk Progress Update: What needs to be in a Robotics Demo?'
---

It's been a month since [my factory automation talk got accepted into PyCon](/2017/02/12/tap-tap-tap/). If you've been following along by means of this blog you've seen that I [bought a barcode reader on Ebay](/2017/02/26/intro-to-barcode-readers/), [made an adapter for it](/2017/03/06/ms3-serial-adapter/) and wasted some time figuring out [how to do Serial-to-USB on a Mac](/2017/03/07/serial-to-usb-on-mac/).

Barcode readers are cool stuff, but when you promised a factory automation demo, reading a few barcodes doesn't really cut it. The same goes for a lot of other automation equipment like pushers, shakers, label printers and so on: It might technically be factory automation, but nobody comes to PyCon to see tech that contains fewer transistors than the blender in their kitchen at home.

The [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product) for a robotics demo needs three elements: *Sensing*, *Actuation*, and *Control*.

## Sensing

This part is easy: The $25 (from Ebay) barcode reader covers it.

Other options I considered were distance sensors and color sensors, but nothing really beats the information/cost ratio of a barcode reader.


## Actuation

This part is the one that's currently giving me headaches. Actuation is essential to my demo, and it's _expensive_!

It's easy to drop a few hundred dollars on just a motor and the controller box that goes with it. A six-axis robot arm has, you guessed it, six motors. Catalog prices for "average" robotic arms are in the tens of thousands of dollars range.

As I'm writing this I have pulled the trigger on a purchase, but I'll keep the suspense up and only tell you what options I've been considering during a month of digging through surplus websites:
* Occasionally, a small used robot arm shows up for around $1,000 (see notes on my budget below). These usually don't have a controller box attached, so I'd have to figure out the pinout and signals myself. I know it's doable because [I've done it before](http://jonasneubert.com/projects/movemaster). It's also a big risk because it requires a lot of effort, the arm might be broken, or might break in transit, or I might break it (I've done that one before, too).
* Conveyor belts are a great example for factory automation because they exist in nearly every factory. A flat straight belt combined with a diverter is enough to set up a meaningful demo. And used conveyor belts show up at the $1,000 price point quite frequently. The caveat here is: Conveyor belts are usually too big to lug to a conference.
* Some of the more trivial machines are generally available at less than $1,000. Small shakers, indexed rotation stages and basic linear motion stages fall into this category. I consider these backup options because while they are cheap, I can't think of a meaningful demo to build around them.


## Control

For a PyCon talk, the idea is, of course, to write the logic of the system in Python. One of the main points of my talk will be (spoiler alert!) that it is becoming increasingly common for factory control systems to read and write information to/from other software systems outside the factory and that Python can be a great tool to build these connections.

But dreams of [Industry 4.0](https://en.wikipedia.org/wiki/Industry_4.0) and [Industrial IoT](https://www.accenture.com/us-en/labs-insight-industrial-internet-of-things) aside, there's the other part of "control" that deals with making motors go at the right speed and [debouncing switches](http://www.unm.edu/~zbaker/ece238/slides/Debounce.pdf). I would rather not have to reinvent the wheel and find a Python way of doing signal conditioning. For one, who's got time for that? More importantly, I intend my talk to be an introduction to real-world automation and in real-world factories, PLCs (Programmable Logic Controllers) are the name of the game.

The type and specification of actuator I get will determine what signals I need to generate, which is why I'm currently on hold for this part of the system.

If all goes well, my next Ebay purchase will be a PLC. If it doesn't go so well, the backup plan is to get a [Phidgets USB I/O board](http://www.phidgets.com/products.php?category=0), not quite "industrial grade" but good enough to send signals.


## Budget

The cost of non-consumer hardware usually falls somewhere on the spectrum between surprising and shocking. Consider road infrastructure, for example: A single traffic signal costs anywhere [between $50k and half a million](http://www.itsbenefits.its.dot.gov/its/benecost.nsf/DisplayRUCByUnitCostElementUnadjusted?ReadForm&UnitCostElement=Traffic+Signal&Subsystem=Roadside+Control+(RS-C))!

Factory equipment isn't quite that pricey, but it's not cheap either. Luckily, it does depreciate fast and there is an abundance of used equipment on Ebay. Which is why I'm hoping to get away with under $2,500 for this demo:

| Line Item | Expected Cost |
| === | === |
| Barcode Reader (incl. cables, peripherals) | $100 |
| Actuator (Arm or Conveyor or similar) | $1,500 |
| Controller (PLC or DAQ card) | $500 |
| Misc. cables and fixtures | $400 |
| --- | --- |
| Total | $2,500 |
