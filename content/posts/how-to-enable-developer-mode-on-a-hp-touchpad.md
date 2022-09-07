---
slug: how-to-enable-developer-mode-on-a-hp-touchpad
date: "2011-07-16T00:00:00Z"
published: true
tags:
- webos
- palm
title: How to enable developer mode on a HP TouchPad
---

<p>This might be a no-brainer for developers who developed for webOS phones in the past. But if you are getting started programming for webOS with a HP Touchpad and the (relatively) new Enyo framework like I am doing right now, you'll have a hard time figuring out how to test your app on the actual device.</p>
<p><strong>Step 1: Put your device in developer mode</strong></p>
<p><span>In "Just Type" enter&nbsp;<em>webos20090606</em>. If you happen to have a lot of time on your hands you can also enter&nbsp;<em>upupdowndownleftrightleftrightbastart </em>(the <a href="http://en.wikipedia.org/wiki/Konami_Code" title="Konami Code on Wikipedia">Konami Code</a>).&nbsp;Both secret phrases will result in a otherwise hidden button appearing:</span></p>
<p><span><img alt="image" src="http://jonemo.de/neubertify/20110716-test-your-app-on-touchpad/browser.png" /><br /></span></p>
<p><span>Press the button, switch the "Developer Mode" switch on, and follow the straightforward onscreen instructions. Your life will be a lot easier if you leave the password empty, but that also means that anyone who gets your Touchpad and connects it to a computer, has Novaterm and knows what he or she is doing can get root access to your Touchpad. You decide.</span></p>
<p><span>When you're done you should see this screen:</span></p>
<p><span><img alt="image" src="http://jonemo.de/neubertify/20110716-test-your-app-on-touchpad/devmodeswitcher.png" /><br /></span></p>
<p><strong>Step 2: Restart</strong></p>
<p>I am not sure this step is really needed but on the internets I read reports of things not working if you skip this step. To restart your Touchpad, press and hold the main button and then press and hold the on/off button. Keep holding them until the flashing HP logo appears.&nbsp;</p>
<p><span><strong>Step 2: Connect Touchpad to computer</strong></span></p>
<p>Plug the USB cable into the Touchpad and into the computer where you are developing the app. On the Touchpad you'll see a <strike>notification</strike> popup offering you to connect the Touchpad as a USB drive. Don't do it.&nbsp;</p>
<p><strong>Step 3: Load your app onto the Touchpad</strong></p>
<p>The assumption here is, that you have the Enyo SDK installed on your computer (if you used the emulator to test your app, you have the SDK). Open your command line (or terminal if on a Mac) and use the following command:</p>
<p><em>palm-package [directory where your app sourcecode is goes here]</em></p>
<p>This packages your app into an ipk archive named after the app name you gave the app in appinfo.json.</p>
<p><em>palm-install -d usb [filename of your compiled app archive goes here]</em></p>
<p>The app will apear under "Downloads" in the Launcher. Done.</p>
<p><strong>Appendix 1: Dear Microsoft</strong></p>
<p>Notice how this howto did not include a two week process of getting approved by one of your shitty partner companies and how it did not cost me 75 Euros to gain the right to test three apps on my device for one year.</p>
<p><strong>Appendix 2: Dear Apple</strong></p>
<p>Notice how this howto did not require going to the store to buy a Mac. Also note, that no NSA style encryption and security certificates were involved.</p>
<p><strong>Appendix 3: Dear Blackberry</strong></p>
<p>Notice how it was possible to test the app on the actual device.</p>
