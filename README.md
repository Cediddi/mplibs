# mplibs
Collection of helpers for Micropython

## What's in the project?
Mainly some small stuff, helpers, experiments and etc.

* **adc_vcc.py**: Helper from @eduvik, idea from @ssendev read about it @ micropython/micropython#2352
* **bi2c.py**: A better i2c implementation that supports chunked writing. Many i2c eeproms need chunked writing.
* **helpers.py**: Helpers used in various other files
* **morse.py**: A small morse code implementation that supports builtin led as well as external output.
* **sseg.py**: Seven segment display driver.
* **wemos.py**: Helper file for esp8266 based wemos products.
* _wemos_shields_/**dht22.py**: dht22 initialization and measure_realitme.
* _wemos_shields_/**oled.py**: ssd1306 and i2c initialization and easier text function that knows the shield's boundaries.

## FIXME:
* **morse.py**
  * needs memory optimizations.
* **sseg.py**
  * support for shift registers.
* _wemos_shields_/**oled.py**
  * better text handling.
  
## TODO:
* **enable_adc_vcc.py** : In case 
* _wemos_shields_/**dht11.py**
* _wemos_shields_/**sdcard.py**
* _wemos_shields_/**motor.py**
* _wemos_shields_/**rgb.py**
* _wemos_shields_/**relay.py**
* _wemos_shields_/**sht30.py**