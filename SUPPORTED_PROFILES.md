# Supported profiles
All profiles (should) correspond to the official [EEP](http://www.enocean-alliance.org/eep/) by EnOcean.

<details open><summary>F6 <i>(RPS Telegram)</i></summary><blockquote>
<details open><summary>01 <i>(Switch Buttons)</i></summary><blockquote>
<details><summary>F6-01-01 <i>(Push Button)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PB      |Status of the push button                         |enum    |0 - Released                                                          |
|        |                                                  |        |1 - Pressed                                                           |

</blockquote></details>

</blockquote></details>

<details open><summary>02 <i>(Rocker Switch, 2 Rocker)</i></summary><blockquote>
<details><summary>F6-02-01 <i>(Light and Blind Control - Application Style 1)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|R1      |Rocker 1st action                                 |enum    |0 - Button AI                                                         |
|        |                                                  |        |1 - Button AO                                                         |
|        |                                                  |        |2 - Button BI                                                         |
|        |                                                  |        |3 - Button BO                                                         |
|EB      |Energy bow                                        |enum    |0 - released                                                          |
|        |                                                  |        |1 - pressed                                                           |
|R2      |Rocker 2nd action                                 |enum    |0 - Button AI                                                         |
|        |                                                  |        |1 - Button AO                                                         |
|        |                                                  |        |2 - Button BI                                                         |
|        |                                                  |        |3 - Button BO                                                         |
|SA      |2nd action                                        |enum    |0 - No 2nd action                                                     |
|        |                                                  |        |1 - 2nd action valid                                                  |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |

</blockquote></details>

<details><summary>F6-02-02 <i>(Light and Blind Control - Application Style 2)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|R1      |Rocker 1st action                                 |enum    |0 - Button AI                                                         |
|        |                                                  |        |1 - Button AO                                                         |
|        |                                                  |        |2 - Button BI                                                         |
|        |                                                  |        |3 - Button BO                                                         |
|EB      |Energy bow                                        |enum    |0 - released                                                          |
|        |                                                  |        |1 - pressed                                                           |
|R2      |Rocker 2nd action                                 |enum    |0 - Button AI                                                         |
|        |                                                  |        |1 - Button AO                                                         |
|        |                                                  |        |2 - Button BI                                                         |
|        |                                                  |        |3 - Button BO                                                         |
|SA      |2nd action                                        |enum    |0 - No 2nd action                                                     |
|        |                                                  |        |1 - 2nd action valid                                                  |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |

</blockquote></details>

</blockquote></details>

<details open><summary>04 <i>(Position Switch, Home and Office Application)</i></summary><blockquote>
<details><summary>F6-04-01 <i>(Key Card Activated Switch)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|KC      |Key Card                                          |enum    |0 - Taken out                                                         |
|        |                                                  |        |112 - Inserted                                                        |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |

</blockquote></details>

</blockquote></details>

<details open><summary>05 <i>(Detectors)</i></summary><blockquote>
<details><summary>F6-05-01 <i>(Liquid Leakage Sensor (mechanic harvester))</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WAS     |Water Sensor                                      |enum    |0-16 - not specified                                                  |
|        |                                                  |        |17 - Water detected                                                   |
|        |                                                  |        |18-255 - not specified                                                |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |

</blockquote></details>

<details><summary>F6-05-02 <i>(Smoke Detector)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SMO     |Status of detection and battery                   |enum    |0 - Smoke Alarm OFF                                                   |
|        |                                                  |        |16 - Smoke Alarm ON                                                   |
|        |                                                  |        |48 - Energy LOW                                                       |

</blockquote></details>

</blockquote></details>

<details open><summary>10 <i>(Mechanical Handle)</i></summary><blockquote>
<details><summary>F6-10-00 <i>(Window Handle)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WIN     |Window handle                                     |enum    |0 - Moved from up to vertical                                         |
|        |                                                  |        |1 - Moved from vertical to up                                         |
|        |                                                  |        |2 - Moved from down to vertical                                       |
|        |                                                  |        |3 - Moved from vertical to down                                       |
|T21     |T21                                               |status  |                                                                      |
|NU      |NU                                                |status  |                                                                      |

</blockquote></details>

</blockquote></details>

</blockquote></details>
<details open><summary>D5 <i>(1BS Telegram)</i></summary><blockquote>
<details open><summary>00 <i>(Contacts and Switches)</i></summary><blockquote>
<details><summary>D5-00-01 <i>(Single Input Contact)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CO      |Contact                                           |enum    |0 - open                                                              |
|        |                                                  |        |1 - closed                                                            |

</blockquote></details>

</blockquote></details>

</blockquote></details>
<details open><summary>A5 <i>(4BS Telegram)</i></summary><blockquote>
<details open><summary>02 <i>(Temperature Sensors)</i></summary><blockquote>
<details><summary>A5-02-01 <i>(Temperature Sensor Range -40°C to 0°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -40.0-0.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-02 <i>(Temperature Sensor Range -30°C to +10°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -30.0-10.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-03 <i>(Temperature Sensor Range -20°C to +20°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -20.0-20.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-04 <i>(Temperature Sensor Range -10°C to +30°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -10.0-30.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-05 <i>(Temperature Sensor Range 0°C to +40°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |

</blockquote></details>

<details><summary>A5-02-06 <i>(Temperature Sensor Range +10°C to +50°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 10.0-50.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-07 <i>(Temperature Sensor Range +20°C to +60°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 20.0-60.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-08 <i>(Temperature Sensor Range +30°C to +70°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 30.0-70.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-09 <i>(Temperature Sensor Range +40°C to +80°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 40.0-80.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-0A <i>(Temperature Sensor Range +50°C to +90°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 50.0-90.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-0B <i>(Temperature Sensor Range +60°C to +100°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 60.0-100.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-10 <i>(Temperature Sensor Range -60°C to +20°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -60.0-20.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-11 <i>(Temperature Sensor Range -50°C to +30°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -50.0-30.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-12 <i>(Temperature Sensor Range -40°C to +40°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -40.0-40.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-13 <i>(Temperature Sensor Range -30°C to +50°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -30.0-50.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-14 <i>(Temperature Sensor Range -20°C to +60°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -20.0-60.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-15 <i>(Temperature Sensor Range -10°C to +70°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ -10.0-70.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-16 <i>(Temperature Sensor Range 0°C to +80°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-80.0 °C                                               |

</blockquote></details>

<details><summary>A5-02-17 <i>(Temperature Sensor Range +10°C to +90°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 10.0-90.0 °C                                              |

</blockquote></details>

<details><summary>A5-02-18 <i>(Temperature Sensor Range +20°C to +100°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 20.0-100.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-19 <i>(Temperature Sensor Range +30°C to +110°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 30.0-110.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-1A <i>(Temperature Sensor Range +40°C to +120°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 40.0-120.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-1B <i>(Temperature Sensor Range +50°C to +130°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 50.0-130.0 °C                                             |

</blockquote></details>

<details><summary>A5-02-20 <i>(10 Bit Temperature Sensor Range -10°C to +41.2°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |1023.0-0.0 ↔ -10.0-41.2 °C                                            |

</blockquote></details>

<details><summary>A5-02-30 <i>(10 Bit Temperature Sensor Range -40°C to +62.3°C)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |1023.0-0.0 ↔ -40.0-62.3 °C                                            |

</blockquote></details>

</blockquote></details>

<details open><summary>04 <i>(Temperature and Humidity Sensor)</i></summary><blockquote>
<details><summary>A5-04-01 <i>(Range 0°C to +40°C and 0% to 100%)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-250.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-250.0 ↔ 0.0-40.0 °C                                               |
|TSN     |Availability of the Temperature Sensor            |enum    |0 - not available                                                     |
|        |                                                  |        |1 - available                                                         |

</blockquote></details>

<details><summary>A5-04-02 <i>(Range -20°C to +60°C and 0% to 100%)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-250.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-250.0 ↔ -20.0-60.0 °C                                             |
|TSN     |Availability of the Temperature Sensor            |enum    |0 - not available                                                     |
|        |                                                  |        |1 - available                                                         |

</blockquote></details>

<details><summary>A5-04-03 <i>(Range -20°C to +60°C 10bit-measurement and 0% to 100%)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-255.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-1023.0 ↔ -20.0-60.0 °C                                            |
|TTP     |Telegram Type                                     |enum    |0 - Heartbeat                                                         |
|        |                                                  |        |1 - Event triggered                                                   |

</blockquote></details>

<details><summary>A5-04-04 <i>(Range -40°C to +120°C 12bit-measurement and 0% to 100%)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-199.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-1599.0 ↔ -40.0-120.0 °C                                           |

</blockquote></details>

</blockquote></details>

<details open><summary>06 <i>(Light Sensor)</i></summary><blockquote>
<details><summary>A5-06-01 <i>(Range 300lx to 60.000lx)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL2    |Illumination 2 (linear)                           |value   |0.0-255.0 ↔ 300.0-30000.0 lx                                          |
|ILL1    |Illumination 1 (linear)                           |value   |0.0-255.0 ↔ 600.0-60000.0 lx                                          |
|RS      |Range select                                      |enum    |0 - Range acc. to DB_1 (ILL1)                                         |
|        |                                                  |        |1 - Range acc. to DB_2 (ILL2)                                         |

</blockquote></details>

<details><summary>A5-06-02 <i>(Range 0lx to 1.020lx)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL2    |Illumination 2 (linear)                           |value   |0.0-255.0 ↔ 0.0-510.0 lx                                              |
|ILL1    |Illumination 1 (linear)                           |value   |0.0-255.0 ↔ 0.0-1020.0 lx                                             |
|RS      |Range select                                      |enum    |0 - Range acc. to DB_1 (ILL1)                                         |
|        |                                                  |        |1 - Range acc. to DB_2 (ILL2)                                         |

</blockquote></details>

</blockquote></details>

<details open><summary>07 <i>(Occupancy Sensor)</i></summary><blockquote>
<details><summary>A5-07-01 <i>(Occupancy with Supply voltage monitor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (OPTIONAL)                         |value   |0.0-250.0 ↔ 0.0-5.0 V                                                 |
|PIRS    |PIR Status                                        |enum    |0 - PIR off                                                           |
|        |                                                  |        |1 - PIR on                                                            |
|SVA     |Supply voltage availability                       |enum    |0 - Supply voltage is not supported                                   |
|        |                                                  |        |1 - Supply voltage is supported                                       |

</blockquote></details>

<details><summary>A5-07-02 <i>(Occupancy with Supply voltage monitor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (REQUIRED)                         |value   |0.0-250.0 ↔ 0.0-5.0 V                                                 |
|PIRS    |PIR Status                                        |enum    |0 - Uncertain of occupancy status                                     |
|        |                                                  |        |1 - Motion detected                                                   |

</blockquote></details>

<details><summary>A5-07-03 <i>(Occupancy with Supply voltage monitor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (REQUIRED)                         |value   |0.0-250.0 ↔ 0.0-5.0 V                                                 |
|ILL     |Illumination                                      |value   |0.0-1000.0 ↔ 0.0-1000.0 lx                                            |
|PIRS    |PIR Status                                        |enum    |0 - Uncertain of occupancy status                                     |
|        |                                                  |        |1 - Motion detected                                                   |

</blockquote></details>

</blockquote></details>

<details open><summary>08 <i>(Light, Temperature and Occupancy Sensor)</i></summary><blockquote>
<details><summary>A5-08-01 <i>(Range 0lx to 510lx, 0°C to +51°C and Occupancy Button)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL     |Illumination (linear)                             |value   |0.0-255.0 ↔ 0.0-510.0 lx                                              |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ 0.0-51.0 °C                                               |
|PIRS    |PIR Status                                        |enum    |0 - PIR on                                                            |
|        |                                                  |        |1 - PIR off                                                           |
|OCC     |Occupancy Button                                  |enum    |0 - Button pressed                                                    |
|        |                                                  |        |1 - Button released                                                   |

</blockquote></details>

<details><summary>A5-08-02 <i>(Range 0lx to 1020lx, 0°C to +51°C and Occupancy Button)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL     |Illumination (linear)                             |value   |0.0-255.0 ↔ 0.0-1020.0 lx                                             |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ 0.0-51.0 °C                                               |
|PIRS    |PIR Status                                        |enum    |0 - PIR on                                                            |
|        |                                                  |        |1 - PIR off                                                           |
|OCC     |Occupancy Button                                  |enum    |0 - Button pressed                                                    |
|        |                                                  |        |1 - Button released                                                   |

</blockquote></details>

<details><summary>A5-08-03 <i>(Range 0lx to 1530lx, -30°C to +51°C and Occupancy Button)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage (linear)                           |value   |0.0-255.0 ↔ 0.0-5.1 V                                                 |
|ILL     |Illumination (linear)                             |value   |0.0-255.0 ↔ 0.0-1530.0 lx                                             |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ -30.0-50.0 °C                                             |
|PIRS    |PIR Status                                        |enum    |0 - PIR on                                                            |
|        |                                                  |        |1 - PIR off                                                           |
|OCC     |Occupancy Button                                  |enum    |0 - Button pressed                                                    |
|        |                                                  |        |1 - Button released                                                   |

</blockquote></details>

</blockquote></details>

<details open><summary>09 <i>(Gas Sensor)</i></summary><blockquote>
<details><summary>A5-09-04 <i>(CO2 Sensor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-200.0 ↔ 0.0-100.0 %                                               |
|Conc    |Concentration (linear)                            |value   |0.0-255.0 ↔ 0.0-2550.0 ppm                                            |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ 0.0-51.0 °C                                               |
|HSN     |Availability of the Humidity Sensor               |enum    |0 - not available                                                     |
|        |                                                  |        |1 - available                                                         |
|TSN     |Availability of the Temperature Sensor            |enum    |0 - not available                                                     |
|        |                                                  |        |1 - available                                                         |

</blockquote></details>

<details><summary>A5-09-05 <i>(VOC Sensor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|Conc    |VOC Concentration                                 |value   |0.0-65535.0 ↔ 0.0-65535.0 ppb                                         |
|VOC_ID  |VOC Identification                                |enum    |0 - VOCT (total)                                                      |
|        |                                                  |        |1 - Formaldehyde                                                      |
|        |                                                  |        |2 - Benzene                                                           |
|        |                                                  |        |3 - Styrene                                                           |
|        |                                                  |        |4 - Toluene                                                           |
|        |                                                  |        |5 - Tetrachloroethylene                                               |
|        |                                                  |        |6 - Xylene                                                            |
|        |                                                  |        |7 - n-Hexane                                                          |
|        |                                                  |        |8 - n-Octane                                                          |
|        |                                                  |        |9 - Cyclopentane                                                      |
|        |                                                  |        |10 - Methanol                                                         |
|        |                                                  |        |11 - Ethanol                                                          |
|        |                                                  |        |12 - 1-Pentanol                                                       |
|        |                                                  |        |13 - Acetone                                                          |
|        |                                                  |        |14 - ethylene Oxide                                                   |
|        |                                                  |        |15 - Acetaldehyde ue                                                  |
|        |                                                  |        |16 - Acetic Acid                                                      |
|        |                                                  |        |17 - Propionice Acid                                                  |
|        |                                                  |        |18 - ValericAcid                                                      |
|        |                                                  |        |19 - ButyricAcid                                                      |
|        |                                                  |        |20 - Ammoniac                                                         |
|        |                                                  |        |22 - Hydrogen Sulfide                                                 |
|        |                                                  |        |23 - Dimethylsulfide                                                  |
|        |                                                  |        |24 - 2-Butanol (butyl Alcohol)                                        |
|        |                                                  |        |25 - 2-Methylpropanol                                                 |
|        |                                                  |        |26 - Diethyl ether                                                    |
|        |                                                  |        |255 - ozone                                                           |

</blockquote></details>

</blockquote></details>

<details open><summary>10 <i>(Room Operating Panel)</i></summary><blockquote>
<details><summary>A5-10-03 <i>(Temperature Sensor and Set Point)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |

</blockquote></details>

<details><summary>A5-10-05 <i>(Temperature Sensor, Set Point and Occupancy Control)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |
|OCC     |Occupancy Button                                  |enum    |0 - Button pressed                                                    |
|        |                                                  |        |1 - Button released                                                   |

</blockquote></details>

<details><summary>A5-10-06 <i>(Temperature Sensor, Set Point and Day/Night Control)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |
|SLSW    |Slide switch                                      |enum    |0 - Position I / Night / Off                                          |
|        |                                                  |        |1 - Position O / Day / On                                             |

</blockquote></details>

<details><summary>A5-10-10 <i>(Temperature and Humidity Sensor, Set Point and Occupancy Control)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-250.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-250.0 ↔ 0.0-40.0 °C                                               |
|OCC     |Occupancy Button                                  |enum    |0 - Button pressed                                                    |
|        |                                                  |        |1 - Button released                                                   |

</blockquote></details>

<details><summary>A5-10-12 <i>(Temperature and Humidity Sensor and Set Point)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Set Point (linear)                                |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-250.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature (linear)                              |value   |0.0-250.0 ↔ 0.0-40.0 °C                                               |

</blockquote></details>

</blockquote></details>

<details open><summary>11 <i>(Controller Status)</i></summary><blockquote>
<details><summary>A5-11-02 <i>(Temperature Controller Output)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CVAR    |Actual value of controller                        |value   |0.0-255.0 ↔ 0.0-100.0 %                                               |
|FAN     |Actual value of fan                               |enum    |0 - State 0 Manual                                                    |
|        |                                                  |        |1 - State 1 Manual                                                    |
|        |                                                  |        |2 - State 2 Manual                                                    |
|        |                                                  |        |3 - State 3 Manual                                                    |
|        |                                                  |        |16 - State 0 Automatic                                                |
|        |                                                  |        |17 - State 1 Automatic                                                |
|        |                                                  |        |18 - State 2 Automatic                                                |
|        |                                                  |        |19 - State 3 Automatic                                                |
|        |                                                  |        |255 - Not Available                                                   |
|ASP     |Actual Setpoint                                   |value   |0.0-255.0 ↔ 0.0-51.2 C                                                |
|ALR     |Alarm                                             |enum    |0 - No alarm                                                          |
|        |                                                  |        |1 - Alarm                                                             |
|CTM     |Controller mode                                   |enum    |1 - Heating                                                           |
|        |                                                  |        |2 - Cooling                                                           |
|        |                                                  |        |3 - Off                                                               |
|CTS     |Controller state                                  |enum    |0 - Automatic                                                         |
|        |                                                  |        |1 - Override                                                          |
|ERH     |Energy hold-off                                   |enum    |0 - Normal                                                            |
|        |                                                  |        |1 - Energy hold-off / Dew point                                       |
|RO      |Room occupancy                                    |enum    |0 - Occupied                                                          |
|        |                                                  |        |1 - Unoccupied                                                        |
|        |                                                  |        |2 - StandBy                                                           |
|        |                                                  |        |3 - Frost                                                             |

</blockquote></details>

<details><summary>A5-11-03 <i>(Blind Status)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|BSP     |Blind/shutter position                            |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|AS      |Angle sign                                        |enum    |0 - Positive sign                                                     |
|        |                                                  |        |1 - Negative sign                                                     |
|AN      |Angle in 2 degrees steps                          |value   |0.0-90.0 ↔ 0.0-180.0 degrees                                          |
|PVF     |Position value flag                               |enum    |0 - No position value available                                       |
|        |                                                  |        |1 - Position value available                                          |
|AVF     |Angle value flag                                  |enum    |0 - No Angle value available                                          |
|        |                                                  |        |1 - Angle value available                                             |
|ES      |Error state                                       |enum    |0 - No error present                                                  |
|        |                                                  |        |1 - End-positions are not configured                                  |
|        |                                                  |        |2 - Internal failure                                                  |
|        |                                                  |        |3 - Not used                                                          |
|EP      |End position                                      |enum    |0 - No End-position available                                         |
|        |                                                  |        |1 - No End-position reached                                           |
|        |                                                  |        |2 - Blind fully open                                                  |
|        |                                                  |        |3 - Blind fully closed                                                |
|ST      |Status                                            |enum    |0 - No status available                                               |
|        |                                                  |        |1 - Blind is stopped                                                  |
|        |                                                  |        |2 - Blind opens                                                       |
|        |                                                  |        |3 - Blind closes                                                      |
|SM      |Service mode                                      |enum    |0 - Normal mode                                                       |
|        |                                                  |        |1 - Service mode activated                                            |
|MOTP    |Mode of the position                              |enum    |0 - Normal mode                                                       |
|        |                                                  |        |1 - Inverse ode                                                       |

</blockquote></details>

</blockquote></details>

<details open><summary>12 <i>(Automated Meter Reading (AMR))</i></summary><blockquote>
<details><summary>A5-12-00 <i>(Counter)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MR      |Current value in or cumulative counter value      |value   |0.0-16777215.0 ↔ 0.0-16777215.0                                       |
|CH      |Measurement channel                               |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|DT      |Current value or cumulative counter value         |enum    |0 - Cumulative value                                                  |
|        |                                                  |        |1 - Current value                                                     |
|DIV     |Divisor for value                                 |enum    |0 - x/1                                                               |
|        |                                                  |        |1 - x/10                                                              |
|        |                                                  |        |2 - x/100                                                             |
|        |                                                  |        |3 - x/1000                                                            |

</blockquote></details>

<details><summary>A5-12-01 <i>(Electricity)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MR      |current value in W or cumulative value in kWh     |value   |0.0-16777215.0 ↔ 0.0-16777215.0                                       |
|TI      |Tariff info                                       |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|DT      |Current value or cumulative value                 |enum    |0 - kWh                                                               |
|        |                                                  |        |1 - W                                                                 |
|DIV     |Divisor for value                                 |enum    |0 - x/1                                                               |
|        |                                                  |        |1 - x/10                                                              |
|        |                                                  |        |2 - x/100                                                             |
|        |                                                  |        |3 - x/1000                                                            |

</blockquote></details>

</blockquote></details>

<details open><summary>13 <i>(Environmental Applications)</i></summary><blockquote>
<details><summary>A5-13-01 <i>(Weather Station)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|DWS     |Dawn sensor                                       |value   |0.0-255.0 ↔ 0.0-999.0 lx                                              |
|TMP     |Outdoor Temp                                      |value   |0.0-255.0 ↔ -40.0-80.0 °C                                             |
|WND     |Wind speed                                        |value   |0.0-255.0 ↔ 0.0-70.0 m/s                                              |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|DN      |Day / Night                                       |enum    |0 - Day                                                               |
|        |                                                  |        |1 - Night                                                             |
|RAN     |Rain Indication                                   |enum    |0 - No Rain                                                           |
|        |                                                  |        |1 - Rain                                                              |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SNW     |Sun - West                                        |value   |0.0-255.0 ↔ 0.0-150.0 klx                                             |
|SNS     |Sun - South                                       |value   |0.0-255.0 ↔ 0.0-150.0 klx                                             |
|SNE     |Sun - East                                        |value   |0.0-255.0 ↔ 0.0-150.0 klx                                             |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|HEM     |Hemisphere                                        |enum    |0 - North                                                             |
|        |                                                  |        |1 - South                                                             |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|DY      |Day                                               |value   |1.0-31.0 ↔ 1.0-31.0                                                   |
|MTH     |Month                                             |value   |1.0-12.0 ↔ 1.0-12.0                                                   |
|YR      |Year                                              |value   |0.0-99.0 ↔ 2000.0-2099.0                                              |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|SRC     |Source                                            |enum    |0 - Real Time Clock                                                   |
|        |                                                  |        |1 - GPS or equivalent (e.g. DCF77, WWV)                               |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WDY     |Weekday                                           |enum    |1 - Monday                                                            |
|        |                                                  |        |2 - Tuesday                                                           |
|        |                                                  |        |3 - Wednesday                                                         |
|        |                                                  |        |4 - Thursday                                                          |
|        |                                                  |        |5 - Friday                                                            |
|        |                                                  |        |6 - Saturday                                                          |
|        |                                                  |        |7 - Sunday                                                            |
|HR      |Hour                                              |value   |0.0-23.0 ↔ 0.0-23.0                                                   |
|MIN     |Minute                                            |value   |0.0-59.0 ↔ 0.0-59.0                                                   |
|SEC     |Second                                            |value   |0.0-59.0 ↔ 0.0-59.0                                                   |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|TMF     |Time Format                                       |enum    |0 - 24 Hours                                                          |
|        |                                                  |        |1 - 12 Hours                                                          |
|A/PM    |AM/PM                                             |enum    |0 - AM                                                                |
|        |                                                  |        |1 - PM                                                                |
|SRC     |Source                                            |enum    |0 - Real Time Clock                                                   |
|        |                                                  |        |1 - GPS or equivalent (e.g. DCF77, WWV)                               |

###### command: 5
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|ELV     |Elevation                                         |value   |0.0-180.0 ↔ -90.0-90.0 °                                              |
|AZM     |Azimut                                            |value   |0.0-359.0 ↔ 0.0-359.0 °                                               |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |

###### command: 6
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|LAT_MSB |Latitude(MSB)                                     |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|LOT_MSB |Longitude(MSB)                                    |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|LAT_LSB |Latitude(LSB)                                     |value   |0.0-255.0 ↔ 0.0-255.0 °                                               |
|LOT_LSB |Longitude(LSB)                                    |value   |0.0-255.0 ↔ 0.0-255.0 °                                               |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |

</blockquote></details>

<details><summary>A5-13-02 <i>(Sun Intensity)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SNW     |Sun - West                                        |value   |0.0-255.0 ↔ 0.0-150.0 klx                                             |
|SNS     |Sun - South                                       |value   |0.0-255.0 ↔ 0.0-150.0 klx                                             |
|SNE     |Sun - East                                        |value   |0.0-255.0 ↔ 0.0-150.0 klx                                             |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|HEM     |Hemisphere                                        |enum    |0 - North                                                             |
|        |                                                  |        |1 - South                                                             |

</blockquote></details>

<details><summary>A5-13-03 <i>(Date Exchange)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|DY      |Day                                               |value   |1.0-31.0 ↔ 1.0-31.0                                                   |
|MTH     |Month                                             |value   |1.0-12.0 ↔ 1.0-12.0                                                   |
|YR      |Year                                              |value   |0.0-99.0 ↔ 2000.0-2099.0                                              |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|SRC     |Source                                            |enum    |0 - Real Time Clock                                                   |
|        |                                                  |        |1 - GPS or equivalent (e.g. DCF77, WWV)                               |

</blockquote></details>

<details><summary>A5-13-04 <i>(Time and Day Exchange)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|WDY     |Weekday                                           |enum    |1 - Monday                                                            |
|        |                                                  |        |2 - Tuesday                                                           |
|        |                                                  |        |3 - Wednesday                                                         |
|        |                                                  |        |4 - Thursday                                                          |
|        |                                                  |        |5 - Friday                                                            |
|        |                                                  |        |6 - Saturday                                                          |
|        |                                                  |        |7 - Sunday                                                            |
|HR      |Hour                                              |value   |0.0-23.0 ↔ 0.0-23.0                                                   |
|MIN     |Minute                                            |value   |0.0-59.0 ↔ 0.0-59.0                                                   |
|SEC     |Second                                            |value   |0.0-59.0 ↔ 0.0-59.0                                                   |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |
|TMF     |Time Format                                       |enum    |0 - 24 Hours                                                          |
|        |                                                  |        |1 - 12 Hours                                                          |
|A/PM    |AM/PM                                             |enum    |0 - AM                                                                |
|        |                                                  |        |1 - PM                                                                |
|SRC     |Source                                            |enum    |0 - Real Time Clock                                                   |
|        |                                                  |        |1 - GPS or equivalent (e.g. DCF77, WWV)                               |

</blockquote></details>

<details><summary>A5-13-05 <i>(Direction Exchange)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|ELV     |Elevation                                         |value   |0.0-180.0 ↔ -90.0-90.0 °                                              |
|AZM     |Azimut                                            |value   |0.0-359.0 ↔ 0.0-359.0 °                                               |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |

</blockquote></details>

<details><summary>A5-13-06 <i>(Geographic Position Exchange)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|LAT_MSB |Latitude(MSB)                                     |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|LOT_MSB |Longitude(MSB)                                    |value   |0.0-15.0 ↔ 0.0-15.0                                                   |
|LAT_LSB |Latitude(LSB)                                     |value   |0.0-255.0 ↔ 0.0-255.0 °                                               |
|LOT_LSB |Longitude(LSB)                                    |value   |0.0-255.0 ↔ 0.0-255.0 °                                               |
|ID      |Identifier                                        |enum    |0-15 - Identifier {value}                                             |

</blockquote></details>

</blockquote></details>

<details open><summary>14 <i>(Multi-Func Sensor)</i></summary><blockquote>
<details><summary>A5-14-01 <i>(Single Input Contact (Window/Door), Supply voltage monitor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage / super cap. (linear); 251 - 255 reserved for error code|value   |0.0-250.0 ↔ 0.0-5.0 V                                                 |
|CT      |Contact                                           |enum    |1 - open                                                              |
|        |                                                  |        |0 - closed                                                            |

</blockquote></details>

<details><summary>A5-14-09 <i>(Window/Door-Sensor with States Open/Closed/Tilt, Supply voltage monitor)</i></summary><blockquote>

| shortcut | description                          | type  | values                |
| -------- | ------------------------------------ | ----- | --------------------- |
| SVC      | Supply voltage / super cap. (linear) | value | 0.0-250.0 ↔ 0.0-5.0 V |
| CT       | Contact                              | enum  | 0 - Closed            |
|          |                                      |       | 1 - Tilt              |
|          |                                      |       | 2 - Reserved          |
|          |                                      |       | 3 - Open              |

</blockquote></details>

<details><summary>A5-14-0A <i>(Window/Door-Sensor with States Open/Closed/Tilt, Supply voltage monitor and Vibration detection)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SVC     |Supply voltage / super cap. (linear)              |value   |0.0-250.0 ↔ 0.0-5.0 V                                                 |
|CT      |Contact                                           |enum    |0 - Closed                                                            |
|        |                                                  |        |1 - Tilt                                                              |
|        |                                                  |        |2 - Reserved                                                          |
|        |                                                  |        |3 - Open                                                              |
|VIB     |Vibration                                         |enum    |1 - Vibration detected                                                |
|        |                                                  |        |0 - No vibration detected                                             |

</blockquote></details>

</blockquote></details>

<details open><summary>20 <i>(HVAC Components)</i></summary><blockquote>
<details><summary>A5-20-01 <i>(Battery Powered Actuator (BI-DIR))</i></summary><blockquote>

###### direction: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CV      |Current Value                                     |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|SO      |Service On                                        |enum    |0 - off                                                               |
|        |                                                  |        |1 - on                                                                |
|ENIE    |Energy input enabled                              |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|ES      |Energy storage sufficiently charged               |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|BCAP    |Battery capacity; change battery next days        |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|CCO     |Contact, cover open                               |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|FTS     |Failure Temperature sensor, out of range          |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|DWO     |Detection, window open                            |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|ACO     |Actuator obstructed                               |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|TMP     |Temperature (linear)                              |value   |0.0-255.0 ↔ 0.0-40.0 °C                                               |

###### direction: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Valve Position or Temperature Setpoint            |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|TMP     |Temperature from RCU                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |
|RIN     |Run init sequence                                 |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|LFS     |Lift set                                          |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|VO      |Valve open / maintenance                          |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|VC      |Valve closed                                      |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|SB      |Summer bit, Reduction of energy consumption       |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|SPS     |Set point selection                               |enum    |0 - Valve position                                                    |
|        |                                                  |        |1 - Temperature set point                                             |
|SPN     |Set point inverse                                 |enum    |0 - false                                                             |
|        |                                                  |        |1 - true                                                              |
|RCU     |Select function                                   |enum    |0 - RCU                                                               |
|        |                                                  |        |1 - service on                                                        |

</blockquote></details>

<details><summary>A5-20-04 <i>(Heating Radiator Valve Actuating Drive with feed and room temperature MEasurement, Local Set point and Display (BI-DIR))</i></summary><blockquote>

###### direction: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CP      |Current Value                                     |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|FTS     |Feed Temperature OR Temperature Set Point         |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|TMPFC   |Room Temperature OR Failure Code                  |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|MST     |Measurement Status                                |enum    |0 - Active                                                            |
|        |                                                  |        |1 - Inactive                                                          |
|STR     |Status Request                                    |enum    |0 - No change                                                         |
|        |                                                  |        |1 - Status requested                                                  |
|BLS     |Button Lock Status                                |enum    |0 - Unlocked                                                          |
|        |                                                  |        |1 - Locked                                                            |
|TS      |Temperature Selection                             |enum    |0 - Feed Temperature                                                  |
|        |                                                  |        |1 - Temperature Set Point                                             |
|FL      |Failure                                           |enum    |0 - No Failure                                                        |
|        |                                                  |        |1 - Failure                                                           |

###### direction: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|POS     |Valve Position                                    |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|TSP     |Temperature Set Point                             |value   |0.0-255.0 ↔ 10.0-30.0 °C                                              |
|MC      |Measure Control                                   |enum    |0 - Enable                                                            |
|        |                                                  |        |1 - Disable                                                           |
|WUC     |Wake Up Cycle                                     |enum    |0 - 10 sec                                                            |
|        |                                                  |        |1 - 60 sec                                                            |
|        |                                                  |        |2 - 90 sec                                                            |
|        |                                                  |        |3 - 120 sec                                                           |
|        |                                                  |        |4 - 150 sec                                                           |
|        |                                                  |        |5 - 180 sec                                                           |
|        |                                                  |        |6 - 210 sec                                                           |
|        |                                                  |        |7 - 240 sec                                                           |
|        |                                                  |        |8 - 270 sec                                                           |
|        |                                                  |        |9 - 300 sec                                                           |
|        |                                                  |        |10 - 330 sec                                                          |
|        |                                                  |        |11 - 360 sec                                                          |
|        |                                                  |        |11 - 390 sec                                                          |
|        |                                                  |        |12 - 420 sec                                                          |
|        |                                                  |        |13 - 450 sec                                                          |
|        |                                                  |        |14 - 450 sec                                                          |
|        |                                                  |        |15 - 480 sec                                                          |
|        |                                                  |        |16 - 510 sec                                                          |
|        |                                                  |        |17 - 540 sec                                                          |
|        |                                                  |        |18 - 570 sec                                                          |
|        |                                                  |        |19 - 600 sec                                                          |
|        |                                                  |        |20 - 630 sec                                                          |
|        |                                                  |        |21 - 660 sec                                                          |
|        |                                                  |        |22 - 690 sec                                                          |
|        |                                                  |        |23 - 720 sec                                                          |
|        |                                                  |        |24 - 750 sec                                                          |
|        |                                                  |        |25 - 780 sec                                                          |
|        |                                                  |        |26 - 810 sec                                                          |
|        |                                                  |        |27 - 840 sec                                                          |
|        |                                                  |        |28 - 870 sec                                                          |
|        |                                                  |        |29 - 900 sec                                                          |
|        |                                                  |        |30 - 930 sec                                                          |
|        |                                                  |        |31 - 960 sec                                                          |
|        |                                                  |        |32 - 990 sec                                                          |
|        |                                                  |        |33 - 1020 sec                                                         |
|        |                                                  |        |34 - 1050 sec                                                         |
|        |                                                  |        |35 - 1080 sec                                                         |
|        |                                                  |        |36 - 1110 sec                                                         |
|        |                                                  |        |37 - 1140 sec                                                         |
|        |                                                  |        |38 - 1170 sec                                                         |
|        |                                                  |        |39 - 1200 sec                                                         |
|        |                                                  |        |40 - 1230 sec                                                         |
|        |                                                  |        |41 - 1260 sec                                                         |
|        |                                                  |        |42 - 1290 sec                                                         |
|        |                                                  |        |43 - 1320 sec                                                         |
|        |                                                  |        |44 - 1350 sec                                                         |
|        |                                                  |        |45 - 1380 sec                                                         |
|        |                                                  |        |46 - 1410 sec                                                         |
|        |                                                  |        |47 - 1440 sec                                                         |
|        |                                                  |        |48 - 1470 sec                                                         |
|        |                                                  |        |49 - 1500 sec                                                         |
|        |                                                  |        |50 - 3 hrs                                                            |
|        |                                                  |        |51 - 6 hrs                                                            |
|        |                                                  |        |52 - 9 hrs                                                            |
|        |                                                  |        |53 - 12 hrs                                                           |
|        |                                                  |        |54 - 15 hrs                                                           |
|        |                                                  |        |55 - 18 hrs                                                           |
|        |                                                  |        |56 - 21 hrs                                                           |
|        |                                                  |        |57 - 24 hrs                                                           |
|        |                                                  |        |58 - 27 hrs                                                           |
|        |                                                  |        |59 - 30 hrs                                                           |
|        |                                                  |        |60 - 33 hrs                                                           |
|        |                                                  |        |61 - 36 hrs                                                           |
|        |                                                  |        |62 - 39 hrs                                                           |
|        |                                                  |        |63 - 42 hrs (max)                                                     |
|DSO     |Display Orientation                               |enum    |0 - 0°                                                                |
|        |                                                  |        |1 - 90°                                                               |
|        |                                                  |        |2 - 180°                                                              |
|        |                                                  |        |3 - 270°                                                              |
|BLC     |Button Lock Control                               |enum    |0 - Unlocked                                                          |
|        |                                                  |        |1 - Locked                                                            |
|SER     |Service command                                   |enum    |0 - No change                                                         |
|        |                                                  |        |1 - Open valve                                                        |
|        |                                                  |        |2 - Run initialisation                                                |
|        |                                                  |        |3 - Close valve                                                       |

</blockquote></details>

<details><summary>A5-20-06 <i>(Harvesting-powered actuator with local temperature offset control (BI-DIR))</i></summary><blockquote>

###### direction: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CV      |Current Valve position                            |value   |0.0-100.0 ↔ 0.0-100.0 %                                               |
|LOM     |Local Offset Mode                                 |enum    |0 - LO is relative                                                    |
|        |                                                  |        |1 - LO is absolute                                                    |
|LO      |Local Offset                                      |value   |0.0-127.0 ↔ 0.0-127.0 °C                                              |
|TMP     |Local Ambient or Feed temperature                 |value   |0.0-255.0 ↔ 0.0-255.0 °C                                              |
|TSL     |Indicates which sensor is used for TMP            |enum    |0 - Ambient sensor temp                                               |
|        |                                                  |        |1 - Feed sensor temperature                                           |
|ENIE    |Harvesting status                                 |enum    |0 - Not harvesting                                                    |
|        |                                                  |        |1 - Harvesting active                                                 |
|ES      |Charge level of energy storage                    |enum    |0 - Low, almost discharged                                            |
|        |                                                  |        |1 - Sufficiently charged                                              |
|DWO     |Window open detection                             |enum    |0 - No open window detected                                           |
|        |                                                  |        |1 - Open window detected                                              |
|RCE     |Indicates radio communication errors              |enum    |0 - Radio communication is stable                                     |
|        |                                                  |        |1 - Six or more consecutive radio communication errors have occurred  |
|RSS     |Weak radio signal warning                         |enum    |0 - Radio signal is strong                                            |
|        |                                                  |        |1 - Radio signal is weak (-77 dBm or less)                            |
|ACO     |Reports blocked actuator (motor)                  |enum    |0 - Actuator working correctly                                        |
|        |                                                  |        |1 - Actuator is blocked                                               |

###### direction: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SP      |Valve Position or Temperature Set point           |value   |0.0-255.0 ↔ 0.0-255.0 %                                               |
|TMP     |Room temperature from room control unit           |value   |0.0-160.0 ↔ 0.0-40.0 °C                                               |
|REF     |Execute reference-run                             |enum    |0 - Normal operation                                                  |
|        |                                                  |        |1 - Reference-run and Maintenance Interval                            |
|RFC     |Radio duty cycle selection.                       |enum    |0 - AUTO (default)                                                    |
|        |                                                  |        |1 - 2 minutes                                                         |
|        |                                                  |        |2 - 5 minutes                                                         |
|        |                                                  |        |3 - 10 minutes                                                        |
|        |                                                  |        |4 - 20 minutes                                                        |
|        |                                                  |        |5 - 30 minutes                                                        |
|        |                                                  |        |6 - 60 minutes                                                        |
|        |                                                  |        |7 - 120 minutes                                                       |
|SB      |Initiate summer mode (reduced communication)      |enum    |0 - Normal operation                                                  |
|        |                                                  |        |1 - Summer mode with 8h radio duty cycle                              |
|SPS     |Set point selection for DB3                       |enum    |0 - Valve position mode                                               |
|        |                                                  |        |1 - Temperature set point                                             |
|TSL     |Temperature requested from the actuator           |enum    |0 - Request ambient temperature                                       |
|        |                                                  |        |1 - Request feed temperature                                          |
|SBY     |Enter standby mode, refer to Appendix             |enum    |0 - Normal operation                                                  |
|        |                                                  |        |1 - Standby                                                           |

</blockquote></details>

</blockquote></details>

<details open><summary>30 <i>(Digital Input)</i></summary><blockquote>
<details><summary>A5-30-03 <i>(4 Digital Inputs, Wake and Temperature)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature (linear)                              |value   |255.0-0.0 ↔ 0.0-40.0 °C                                               |
|WA0     |Value of wake signal                              |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI3     |Digital Input 3                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI2     |Digital Input 2                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI1     |Digital Input 1                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI0     |Digital Input 0                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |

</blockquote></details>

<details><summary>A5-30-04 <i>(3 Digital Inputs, 1 Digital Input 8 bits)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|DV0     |Digital Value 1 byte                              |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|DI2     |Digital Input 2                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI1     |Digital Input 1                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |
|DI0     |Digital Input 0                                   |enum    |0 - Low                                                               |
|        |                                                  |        |1 - High                                                              |

</blockquote></details>

</blockquote></details>

<details open><summary>38 <i>(Central Command)</i></summary><blockquote>
<details><summary>A5-38-08 <i>(Gateway)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|COM     |Command ID                                        |enum    |0-13 - Command ID {value}                                             |
|TIM     |Time in 1/10 seconds. 0 = no time specifed        |value   |1.0-65535.0 ↔ 0.1-6553.5 s                                            |
|LCK     |Lock for duration time if time >0, unlimited time of no time specified. Locking may be cleared with "unlock". During lock phase no other commands will be accepted or executed|enum    |0 - Unlock                                                            |
|        |                                                  |        |1 - Lock                                                              |
|DEL     |Delay or duration (if Time > 0); 0 = Duration (Execute switching command immediately and switch back after duration) 1 = Delay (Execute switching command after delay)|enum    |0 - Duration                                                          |
|        |                                                  |        |1 - Delay                                                             |
|SW      |Switching command ON/OFF                          |enum    |0 - Off                                                               |
|        |                                                  |        |1 - On                                                                |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|COM     |Command ID                                        |enum    |0-13 - Command ID {value}                                             |
|EDIM    |Dimming value (absolute [0...255] or relative [0...100])|value   |0.0-255.0 ↔ 0.0-255.0 %                                               |
|RMP     |Ramping time in seconds, 0 = no ramping, 1...255 = seconds to 100%|value   |0.0-255.0 ↔ 0.0-255.0 s                                               |
|EDIMR   |Dimming Range                                     |enum    |0 - Absolute value                                                    |
|        |                                                  |        |1 - Relative value                                                    |
|STR     |Store final value                                 |enum    |0 - No                                                                |
|        |                                                  |        |1 - Yes                                                               |
|SW      |Switching command                                 |enum    |0 - Off                                                               |
|        |                                                  |        |1 - On                                                                |

</blockquote></details>

</blockquote></details>

<details open><summary>3F <i>(Universal)</i></summary><blockquote>
<details><summary>A5-3F-7F <i>(Universal)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|DB3     |Data Byte 3                                       |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|DB2     |Data Byte 2                                       |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|DB1     |Data Byte 1                                       |value   |0.0-255.0 ↔ 0.0-255.0                                                 |
|DB0     |Data Byte 0                                       |value   |0.0-255.0 ↔ 0.0-255.0                                                 |

</blockquote></details>

</blockquote></details>

</blockquote></details>
<details open><summary>D2 <i>(VLD Telegram)</i></summary><blockquote>
<details open><summary>01 <i>(Electronic switches and dimmers with Energy Measurement and Local Control)</i></summary><blockquote>
<details><summary>D2-01-01 <i>(Electronic switch with Local Control)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

</blockquote></details>

<details><summary>D2-01-09 <i>(Type 0x09)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 5
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|RM      |Report measurement                                |enum    |0 - Query only                                                        |
|        |                                                  |        |1 - Query / auto                                                      |
|RE      |Reset measurement                                 |enum    |0 - Not active                                                        |
|        |                                                  |        |1 - Trigger signal                                                    |
|ep      |Measurement mode                                  |enum    |0 - Energy                                                            |
|        |                                                  |        |1 - Power                                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MD_LSB  |Measurement delta LSB                             |enum    |0-15 - Measurement delta LSB {value}                                  |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|MD_MSB  |Measurement delta MSB                             |enum    |0-255 - Measurement delta MSB {value}                                 |
|MAT     |Max message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Max message time {value}                                      |
|MIT     |Min message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Min message time {value}                                      |

###### command: 6
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|qu      |Query                                             |enum    |0 - Query energy                                                      |
|        |                                                  |        |1 - Query power                                                       |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 7
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MV      |Measurement value                                 |enum    |0-4294967295 - Measurement value {value}                              |

</blockquote></details>

<details><summary>D2-01-0A <i>(Smart Plug module, no metering capabilities)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

</blockquote></details>

<details><summary>D2-01-0B <i>(Smart Plug module with Energy Measurement)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 5
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|RM      |Report measurement                                |enum    |0 - Query only                                                        |
|        |                                                  |        |1 - Query / auto                                                      |
|RE      |Reset measurement                                 |enum    |0 - Not active                                                        |
|        |                                                  |        |1 - Trigger signal                                                    |
|ep      |Measurement mode                                  |enum    |0 - Energy                                                            |
|        |                                                  |        |1 - Power                                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MD_LSB  |Measurement delta LSB                             |enum    |0-15 - Measurement delta LSB {value}                                  |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|MD_MSB  |Measurement delta MSB                             |enum    |0-255 - Measurement delta MSB {value}                                 |
|MAT     |Max message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Max message time {value}                                      |
|MIT     |Min message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Min message time {value}                                      |

###### command: 6
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|qu      |Query                                             |enum    |0 - Query energy                                                      |
|        |                                                  |        |1 - Query power                                                       |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 7
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MV      |Measurement value                                 |enum    |0-4294967295 - Measurement value {value}                              |

</blockquote></details>

<details><summary>D2-01-0C <i>(Heating module with Pilotwire command and Energy Measurement)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 5
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|RM      |Report measurement                                |enum    |0 - Query only                                                        |
|        |                                                  |        |1 - Query / auto                                                      |
|RE      |Reset measurement                                 |enum    |0 - Not active                                                        |
|        |                                                  |        |1 - Trigger signal                                                    |
|ep      |Measurement mode                                  |enum    |0 - Energy                                                            |
|        |                                                  |        |1 - Power                                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MD_LSB  |Measurement delta LSB                             |enum    |0-15 - Measurement delta LSB {value}                                  |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|MD_MSB  |Measurement delta MSB                             |enum    |0-255 - Measurement delta MSB {value}                                 |
|MAT     |Max message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Max message time {value}                                      |
|MIT     |Min message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Min message time {value}                                      |

###### command: 6
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|qu      |Query                                             |enum    |0 - Query energy                                                      |
|        |                                                  |        |1 - Query power                                                       |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 7
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MV      |Measurement value                                 |enum    |0-4294967295 - Measurement value {value}                              |

###### command: 8
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|PM      |Pilotwire mode                                    |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Comfort                                                           |
|        |                                                  |        |2 - Eco                                                               |
|        |                                                  |        |3 - Anti-freeze                                                       |
|        |                                                  |        |4 - Comfort-1                                                         |
|        |                                                  |        |5 - Comfort-2                                                         |

###### command: 9
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |

###### command: 10
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|PM      |Pilotwire mode                                    |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Comfort                                                           |
|        |                                                  |        |2 - Eco                                                               |
|        |                                                  |        |3 - Anti-freeze                                                       |
|        |                                                  |        |4 - Comfort-1                                                         |
|        |                                                  |        |5 - Comfort-2                                                         |

</blockquote></details>

<details><summary>D2-01-0D <i>(Micro Smart Plug module with 1 channel, no metering capabilities)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

</blockquote></details>

<details><summary>D2-01-0E <i>(Micro Smart Plug module with 1 channel, and metering capabilities)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 5
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|RM      |Report measurement                                |enum    |0 - Query only                                                        |
|        |                                                  |        |1 - Query / auto                                                      |
|RE      |Reset measurement                                 |enum    |0 - Not active                                                        |
|        |                                                  |        |1 - Trigger signal                                                    |
|ep      |Measurement mode                                  |enum    |0 - Energy                                                            |
|        |                                                  |        |1 - Power                                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MD_LSB  |Measurement delta LSB                             |enum    |0-15 - Measurement delta LSB {value}                                  |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|MD_MSB  |Measurement delta MSB                             |enum    |0-255 - Measurement delta MSB {value}                                 |
|MAT     |Max message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Max message time {value}                                      |
|MIT     |Min message time                                  |enum    |0 - Reserved                                                          |
|        |                                                  |        |1-255 - Min message time {value}                                      |

###### command: 6
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|qu      |Query                                             |enum    |0 - Query energy                                                      |
|        |                                                  |        |1 - Query power                                                       |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 7
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|UN      |Unit                                              |enum    |0 - Energy [Ws]                                                       |
|        |                                                  |        |1 - Energy [Wh]                                                       |
|        |                                                  |        |2 - Energy [KWh]                                                      |
|        |                                                  |        |3 - Power [W]                                                         |
|        |                                                  |        |4 - Power [KW]                                                        |
|        |                                                  |        |5-7 - Not used                                                        |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|MV      |Measurement value                                 |enum    |0-4294967295 - Measurement value {value}                              |

</blockquote></details>

<details><summary>D2-01-0F <i>(Slot-in Module with 1 channel, no metering capabilities)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

</blockquote></details>

<details><summary>D2-01-12 <i>(Slot-in Module with 2 channels, no metering capabilities)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|DV      |Dim value                                         |enum    |0 - Switch to new output value                                        |
|        |                                                  |        |1 - Dim to new output level - dim timer 1                             |
|        |                                                  |        |2 - Dim to new output level - dim timer 2                             |
|        |                                                  |        |3 - Dim to new output level - dim timer 3                             |
|        |                                                  |        |4 - Stop dimming                                                      |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - All output channels supported by the device                      |
|        |                                                  |        |31 - Input channel (from mains supply)                                |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|PF      |Power Failure                                     |enum    |0 - Power Failure Detection disabled/not supported                    |
|        |                                                  |        |1 - Power Failure Detection enabled                                   |
|PFD     |Power Failure Detection                           |enum    |0 - Power Failure Detection not detected/not supported/disabled       |
|        |                                                  |        |1 - Power Failure Detection Detected                                  |
|CMD     |Command identifier                                |enum    |0-13 - Command ID {value}                                             |
|OC      |Over current switch off                           |enum    |0 - Over current switch off: ready / not supported                    |
|        |                                                  |        |1 - Over current switch off: executed                                 |
|EL      |Error level                                       |enum    |0 - Error level 0: hardware OK                                        |
|        |                                                  |        |1 - Error level 1: hardware warning                                   |
|        |                                                  |        |2 - Error level 2: hardware failure                                   |
|        |                                                  |        |3 - Error level not supported                                         |
|IO      |I/O channel                                       |enum    |0-29 - Output channel {value} (to load)                               |
|        |                                                  |        |30 - Not applicable, do not use                                       |
|        |                                                  |        |31 - Input channel (from mains supply)                                |
|LC      |Local control                                     |enum    |0 - Local control disabled / not supported                            |
|        |                                                  |        |1 - Local control enabled                                             |
|OV      |Output value                                      |enum    |0 - Output value 0% or OFF                                            |
|        |                                                  |        |1-100 - Output value {value}% or ON                                   |
|        |                                                  |        |101-126 - Not used                                                    |
|        |                                                  |        |127 - output value not valid / not set                                |

</blockquote></details>

</blockquote></details>

<details open><summary>03 <i>(Light, Switching + Blind Control)</i></summary><blockquote>
<details><summary>D2-03-0A <i>(Push Button – Single Button)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|BATT    |Battery Autonomy                                  |value   |1.0-100.0 ↔ 1.0-100.0 %                                               |
|BA      |Button Action                                     |enum    |0 - Reserved                                                          |
|        |                                                  |        |1 - Simple press                                                      |
|        |                                                  |        |2 - Double press                                                      |
|        |                                                  |        |3 - Long press                                                        |
|        |                                                  |        |4 - Long press released                                               |
|        |                                                  |        |5-255 - Reserved                                                      |

</blockquote></details>

</blockquote></details>

<details open><summary>05 <i>(Blinds Control for Position and Angle)</i></summary><blockquote>
<details><summary>D2-05-00 <i>(Type 0x00)</i></summary><blockquote>

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|POS     |Vertical position                                 |enum    |0-100 - Output position {value}%                                      |
|        |                                                  |        |127 - Do not change                                                   |
|ANG     |Rotation angle                                    |enum    |0-100 - Output angle {value}%                                         |
|        |                                                  |        |127 - Do not change                                                   |
|REPO    |Repositioning                                     |enum    |0 - Go directly to POS/ANG                                            |
|        |                                                  |        |1 - Go up (0%), then to POS/ANG                                       |
|        |                                                  |        |2 - Go down (100%), then to POS/ANG                                   |
|        |                                                  |        |3 - Reserved                                                          |
|LOCK    |Locking modes                                     |enum    |0 - Do not change                                                     |
|        |                                                  |        |1 - Set blockage mode                                                 |
|        |                                                  |        |2 - Set alarm mode                                                    |
|        |                                                  |        |3 - Reserved                                                          |
|        |                                                  |        |4 - Reserved                                                          |
|        |                                                  |        |5 - Reserved                                                          |
|        |                                                  |        |6 - Reserved                                                          |
|        |                                                  |        |7 - Deblockage                                                        |
|CHN     |Channel                                           |enum    |0 - Channel 1                                                         |
|CMD     |Command Id                                        |enum    |0-5 - Command ID {value}                                              |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CHN     |Channel                                           |enum    |0 - Channel 1                                                         |
|CMD     |Command Id                                        |enum    |0-5 - Command ID {value}                                              |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|CHN     |Channel                                           |enum    |0 - Channel 1                                                         |
|CMD     |Command Id                                        |enum    |0-5 - Command ID {value}                                              |

###### command: 4
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|POS     |Current vertical position                         |enum    |0-100 - Output position {value}%                                      |
|        |                                                  |        |127 - Position unknown, will be known after the next goto cmd         |
|ANG     |Current rotation angle                            |enum    |0-100 - Output angle {value}%                                         |
|        |                                                  |        |127 - Angle unknown, will be known after the next goto cmd            |
|LOCK    |Current locking mode                              |enum    |0 - Normal (no lock)                                                  |
|        |                                                  |        |1 - Blockage mode                                                     |
|        |                                                  |        |2 - Alarm mode                                                        |
|        |                                                  |        |3 - Reserved                                                          |
|        |                                                  |        |4 - Reserved                                                          |
|        |                                                  |        |5 - Reserved                                                          |
|        |                                                  |        |6 - Reserved                                                          |
|        |                                                  |        |7 - Reserved                                                          |
|CHN     |Channel                                           |enum    |0 - Channel 1                                                         |
|        |                                                  |        |1 - Channel 2                                                         |
|        |                                                  |        |2 - Channel 3                                                         |
|        |                                                  |        |3 - Channel 4                                                         |
|CMD     |Command Id                                        |enum    |0-5 - Command ID {value}                                              |

</blockquote></details>

</blockquote></details>

<details open><summary>14 <i>(Multi Function Sensors)</i></summary><blockquote>
<details><summary>D2-14-30 <i>(Sensor for Smoke, Air quality, Hygrothermal comfort, Temperature and Humidity)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|SMA0    |Smoke Alarm status                                |enum    |0 - Smoke Alarm non-activated                                         |
|        |                                                  |        |1 - Smoke Alarm activated                                             |
|SMA1    |Sensor fault mode status                          |enum    |0 - Sensor Fault mode non-activated                                   |
|        |                                                  |        |1 - Sensor Fault mode activated                                       |
|SMA2    |Smoke Alarm Condition analysis: Maintenance       |enum    |0 - Maintenance OK                                                    |
|        |                                                  |        |1 - Maintenance not done                                              |
|SMA3    |Smoke Alarm Condition analysis: Humidity          |enum    |0 - Humidity range OK                                                 |
|        |                                                  |        |1 - Humidity range NOK                                                |
|SMA4    |Smoke Alarm Condition analysis: Temperature       |enum    |0 - Temperature range OK                                              |
|        |                                                  |        |1 - Temperature range NOK                                             |
|SMA5    |Time since last maintenance                       |enum    |0-250 - {value} week(s)                                               |
|        |                                                  |        |251-254 - Reserved                                                    |
|        |                                                  |        |255 - Error                                                           |
|ES      |Energy Storage Status                             |enum    |0 - High                                                              |
|        |                                                  |        |1 - Medium                                                            |
|        |                                                  |        |2 - Low                                                               |
|        |                                                  |        |3 - Critical                                                          |
|RPLT    |Countdown time until product end of life          |enum    |0-120 - {value} month(s)                                              |
|        |                                                  |        |121-254 - Reserved                                                    |
|        |                                                  |        |255 - Error                                                           |
|TMP8    |Temperature                                       |value   |0.0-250.0 ↔ 0.0-50.0 °C                                               |
|HUM     |Humidity                                          |value   |0.0-200.0 ↔ 0.0-100.0 %                                               |
|HCI     |Hygrothermal Comfort Index                        |enum    |0 - Good                                                              |
|        |                                                  |        |1 - Medium                                                            |
|        |                                                  |        |2 - Bad                                                               |
|        |                                                  |        |3 - Error                                                             |
|IAQTH   |T/Hum. Indoor Air Analysis                        |enum    |0 - Optimal air range                                                 |
|        |                                                  |        |1 - Dry Air range                                                     |
|        |                                                  |        |2 - High humidity range                                               |
|        |                                                  |        |3 - High temperature and humidity range                               |
|        |                                                  |        |4 - Temperature or Humidity out of analysis range                     |
|        |                                                  |        |5-6 - Reserved                                                        |
|        |                                                  |        |7 - Error                                                             |

</blockquote></details>

<details><summary>D2-14-41 <i>(Indoor -Temperature, Humidity XYZ Acceleration, Illumination Sensor)</i></summary><blockquote>

|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|TMP     |Temperature 10                                    |value   |0.0-1000.0 ↔ -40.0-60.0 °C                                            |
|HUM     |Rel. Humidity (linear)                            |value   |0.0-200.0 ↔ 0.0-100.0 %                                               |
|ILL     |Illumination (linear)                             |value   |0.0-100000.0 ↔ 0.0-100000.0 lx                                        |
|ACC     |Acceleration Status                               |enum    |0 - Periodic Update                                                   |
|        |                                                  |        |1 - Threshold 1 exceeded                                              |
|        |                                                  |        |2 - Threshold 2 exceeded                                              |
|ACX     |Absolute Acceleration on X axis                   |value   |0.0-1000.0 ↔ -2.5-2.5 g                                               |
|ACY     |Absolute Acceleration on Y axis                   |value   |0.0-1000.0 ↔ -2.5-2.5 g                                               |
|ACZ     |Absolute Acceleration on Z axis                   |value   |0.0-1000.0 ↔ -2.5-2.5 g                                               |
|CO      |Contact                                           |enum    |0 - Open                                                              |
|        |                                                  |        |1 - Closed                                                            |

</blockquote></details>

</blockquote></details>

<details open><summary>50 <i>(Heat Recovery Ventilation)</i></summary><blockquote>
<details><summary>D2-50-00 <i>(Type 0x00 (single room ventilation unit))</i></summary><blockquote>

###### command: 0
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|RMT     |Requested Message Type                            |enum    |0 - Ventilation basic status                                          |
|        |                                                  |        |1 - Ventilation extended status                                       |

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|DOMC    |Direct Operation Mode Control                     |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - No action (keep current ventilation mode/level)                  |
|OMC     |Operation Mode Control                            |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Select next operation mode (edge-trigger)                         |
|        |                                                  |        |2 - Select previous operation mode (edge-trigger)                     |
|        |                                                  |        |3 - Reserved                                                          |
|HBC     |Heat Exchanger Bypass Control                     |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Close bypass (edge-trigger)                                       |
|        |                                                  |        |2 - Open bypass (edge-trigger)                                        |
|        |                                                  |        |3 - Reserved                                                          |
|TOMC    |Timer Operation Mode Control                      |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Start timer operation mode (edge-trigger)                         |
|COT     |CO2 Threshold                                     |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|HT      |Humidity Threshold                                |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|AQT     |Air Quality Threshold                             |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|RTT     |Room temperature threshold                        |value   |1.0-127.0 ↔ -63.0-63.0 °C                                             |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|OMS     |Operation Mode Status                             |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - Reserved                                                         |
|SMS     |Safety Mode Status                                |enum    |0 - Fireplace safety mode disabled                                    |
|        |                                                  |        |1 - Fireplace safety mode enabled                                     |
|HBS     |Heat Exchanger Bypass Status                      |enum    |0 - Bypass closed (heat-recovery active)                              |
|        |                                                  |        |1 - Bypass opened (heat-recovery inactive)                            |
|SFP     |Supply Air Flap Position                          |enum    |0 - Supply air flap closed                                            |
|        |                                                  |        |1 - Supply air flap opened                                            |
|EFP     |Exhaust Air Flap Position                         |enum    |0 - Exhaust air flap closed                                           |
|        |                                                  |        |1 - Exhaust air flap opened                                           |
|DMS     |Defrost Mode Status                               |enum    |0 - Defrost mode inactive                                             |
|        |                                                  |        |1 - Defrost mode active                                               |
|CPS     |Cooling Protection Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|OHS     |Outdoor Air Heater Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|SHS     |Outdoor Air Heater Status                         |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|DHS     |Drain Heater Status                               |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|TOMS    |Timer Operation Mode Status                       |enum    |0 - timer operation mode inactive                                     |
|        |                                                  |        |1 - timer operation mode active                                       |
|FMS     |Filter Maintenance Status                         |enum    |0 - Maintenance not required                                          |
|        |                                                  |        |1 - Maintenance required                                              |
|WTPS    |Weekly Timer Program Status                       |enum    |0 - Weekly timer program disabled or not configured                   |
|        |                                                  |        |1 - Weekly timer program active                                       |
|RTCS    |Room Temperature Control Status                   |enum    |0 - Room temperature control inactive                                 |
|        |                                                  |        |1 - Room temperature control active                                   |
|AQS1    |Air Quality Sensor 1                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|MSS     |Master/Slave Configuration Status                 |enum    |0 - Master                                                            |
|        |                                                  |        |1 - Slave                                                             |
|AQS2    |Air Quality Sensor 2                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|OUTT    |Outdoor Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYT   |Supply Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|INT     |Indoor Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|EXHT    |Exhaust Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYFF  |Supply Air Fan Air Flow Rate                      |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|EXHFF   |Exhaust Air Fan Air Flow Rate                     |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|SPLYFS  |Supply Fan Speed                                  |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |
|EXHFS   |Exhaust Fan Speed                                 |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|SVI     |Software Version Info                             |value   |0.0-4095.0 ↔ 0.0-4095.0                                               |
|OHC     |Operation Hours Counter                           |value   |0.0-65535.0 ↔ 0.0-196605.0                                            |
|DIS     |Digital Input 0...15 Status                       |enum    |1-32768 - {value}                                                     |
|DOS     |Digital Output 0...15 Status                      |enum    |1-32768 - {value}                                                     |
|IMS     |Info Message 0...15 Status                        |enum    |1-32768 - {value}                                                     |
|FS      |Fault 0...31 Status                               |enum    |1-2147483648 - {value}                                                |

</blockquote></details>

<details><summary>D2-50-01 <i>(Type 0x01 (single room ventilation unit with pre-heater))</i></summary><blockquote>

###### command: 0
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|RMT     |Requested Message Type                            |enum    |0 - Ventilation basic status                                          |
|        |                                                  |        |1 - Ventilation extended status                                       |

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|DOMC    |Direct Operation Mode Control                     |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - No action (keep current ventilation mode/level)                  |
|OMC     |Operation Mode Control                            |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Select next operation mode (edge-trigger)                         |
|        |                                                  |        |2 - Select previous operation mode (edge-trigger)                     |
|        |                                                  |        |3 - Reserved                                                          |
|HBC     |Heat Exchanger Bypass Control                     |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Close bypass (edge-trigger)                                       |
|        |                                                  |        |2 - Open bypass (edge-trigger)                                        |
|        |                                                  |        |3 - Reserved                                                          |
|TOMC    |Timer Operation Mode Control                      |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Start timer operation mode (edge-trigger)                         |
|COT     |CO2 Threshold                                     |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|HT      |Humidity Threshold                                |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|AQT     |Air Quality Threshold                             |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|RTT     |Room temperature threshold                        |value   |1.0-127.0 ↔ -63.0-63.0 °C                                             |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|OMS     |Operation Mode Status                             |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - Reserved                                                         |
|SMS     |Safety Mode Status                                |enum    |0 - Fireplace safety mode disabled                                    |
|        |                                                  |        |1 - Fireplace safety mode enabled                                     |
|HBS     |Heat Exchanger Bypass Status                      |enum    |0 - Bypass closed (heat-recovery active)                              |
|        |                                                  |        |1 - Bypass opened (heat-recovery inactive)                            |
|SFP     |Supply Air Flap Position                          |enum    |0 - Supply air flap closed                                            |
|        |                                                  |        |1 - Supply air flap opened                                            |
|EFP     |Exhaust Air Flap Position                         |enum    |0 - Exhaust air flap closed                                           |
|        |                                                  |        |1 - Exhaust air flap opened                                           |
|DMS     |Defrost Mode Status                               |enum    |0 - Defrost mode inactive                                             |
|        |                                                  |        |1 - Defrost mode active                                               |
|CPS     |Cooling Protection Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|OHS     |Outdoor Air Heater Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|SHS     |Outdoor Air Heater Status                         |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|DHS     |Drain Heater Status                               |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|TOMS    |Timer Operation Mode Status                       |enum    |0 - timer operation mode inactive                                     |
|        |                                                  |        |1 - timer operation mode active                                       |
|FMS     |Filter Maintenance Status                         |enum    |0 - Maintenance not required                                          |
|        |                                                  |        |1 - Maintenance required                                              |
|WTPS    |Weekly Timer Program Status                       |enum    |0 - Weekly timer program disabled or not configured                   |
|        |                                                  |        |1 - Weekly timer program active                                       |
|RTCS    |Room Temperature Control Status                   |enum    |0 - Room temperature control inactive                                 |
|        |                                                  |        |1 - Room temperature control active                                   |
|AQS1    |Air Quality Sensor 1                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|MSS     |Master/Slave Configuration Status                 |enum    |0 - Master                                                            |
|        |                                                  |        |1 - Slave                                                             |
|AQS2    |Air Quality Sensor 2                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|OUTT    |Outdoor Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYT   |Supply Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|INT     |Indoor Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|EXHT    |Exhaust Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYFF  |Supply Air Fan Air Flow Rate                      |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|EXHFF   |Exhaust Air Fan Air Flow Rate                     |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|SPLYFS  |Supply Fan Speed                                  |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |
|EXHFS   |Exhaust Fan Speed                                 |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|SVI     |Software Version Info                             |value   |0.0-4095.0 ↔ 0.0-4095.0                                               |
|OHC     |Operation Hours Counter                           |value   |0.0-65535.0 ↔ 0.0-196605.0                                            |
|DIS     |Digital Input 0...15 Status                       |enum    |1-32768 - {value}                                                     |
|DOS     |Digital Output 0...15 Status                      |enum    |1-32768 - {value}                                                     |
|IMS     |Info Message 0...15 Status                        |enum    |1-32768 - {value}                                                     |
|FS      |Fault 0...31 Status                               |enum    |1-2147483648 - {value}                                                |

</blockquote></details>

<details><summary>D2-50-10 <i>(Type 0x10 (multi room ventilation unit without bypass))</i></summary><blockquote>

###### command: 0
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|RMT     |Requested Message Type                            |enum    |0 - Ventilation basic status                                          |
|        |                                                  |        |1 - Ventilation extended status                                       |

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|DOMC    |Direct Operation Mode Control                     |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - No action (keep current ventilation mode/level)                  |
|OMC     |Operation Mode Control                            |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Select next operation mode (edge-trigger)                         |
|        |                                                  |        |2 - Select previous operation mode (edge-trigger)                     |
|        |                                                  |        |3 - Reserved                                                          |
|HBC     |Heat Exchanger Bypass Control                     |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Close bypass (edge-trigger)                                       |
|        |                                                  |        |2 - Open bypass (edge-trigger)                                        |
|        |                                                  |        |3 - Reserved                                                          |
|TOMC    |Timer Operation Mode Control                      |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Start timer operation mode (edge-trigger)                         |
|COT     |CO2 Threshold                                     |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|HT      |Humidity Threshold                                |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|AQT     |Air Quality Threshold                             |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|RTT     |Room temperature threshold                        |value   |1.0-127.0 ↔ -63.0-63.0 °C                                             |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|OMS     |Operation Mode Status                             |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - Reserved                                                         |
|SMS     |Safety Mode Status                                |enum    |0 - Fireplace safety mode disabled                                    |
|        |                                                  |        |1 - Fireplace safety mode enabled                                     |
|HBS     |Heat Exchanger Bypass Status                      |enum    |0 - Bypass closed (heat-recovery active)                              |
|        |                                                  |        |1 - Bypass opened (heat-recovery inactive)                            |
|SFP     |Supply Air Flap Position                          |enum    |0 - Supply air flap closed                                            |
|        |                                                  |        |1 - Supply air flap opened                                            |
|EFP     |Exhaust Air Flap Position                         |enum    |0 - Exhaust air flap closed                                           |
|        |                                                  |        |1 - Exhaust air flap opened                                           |
|DMS     |Defrost Mode Status                               |enum    |0 - Defrost mode inactive                                             |
|        |                                                  |        |1 - Defrost mode active                                               |
|CPS     |Cooling Protection Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|OHS     |Outdoor Air Heater Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|SHS     |Outdoor Air Heater Status                         |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|DHS     |Drain Heater Status                               |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|TOMS    |Timer Operation Mode Status                       |enum    |0 - timer operation mode inactive                                     |
|        |                                                  |        |1 - timer operation mode active                                       |
|FMS     |Filter Maintenance Status                         |enum    |0 - Maintenance not required                                          |
|        |                                                  |        |1 - Maintenance required                                              |
|WTPS    |Weekly Timer Program Status                       |enum    |0 - Weekly timer program disabled or not configured                   |
|        |                                                  |        |1 - Weekly timer program active                                       |
|RTCS    |Room Temperature Control Status                   |enum    |0 - Room temperature control inactive                                 |
|        |                                                  |        |1 - Room temperature control active                                   |
|AQS1    |Air Quality Sensor 1                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|MSS     |Master/Slave Configuration Status                 |enum    |0 - Master                                                            |
|        |                                                  |        |1 - Slave                                                             |
|AQS2    |Air Quality Sensor 2                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|OUTT    |Outdoor Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYT   |Supply Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|INT     |Indoor Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|EXHT    |Exhaust Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYFF  |Supply Air Fan Air Flow Rate                      |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|EXHFF   |Exhaust Air Fan Air Flow Rate                     |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|SPLYFS  |Supply Fan Speed                                  |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |
|EXHFS   |Exhaust Fan Speed                                 |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|SVI     |Software Version Info                             |value   |0.0-4095.0 ↔ 0.0-4095.0                                               |
|OHC     |Operation Hours Counter                           |value   |0.0-65535.0 ↔ 0.0-196605.0                                            |
|DIS     |Digital Input 0...15 Status                       |enum    |1-32768 - {value}                                                     |
|DOS     |Digital Output 0...15 Status                      |enum    |1-32768 - {value}                                                     |
|IMS     |Info Message 0...15 Status                        |enum    |1-32768 - {value}                                                     |
|FS      |Fault 0...31 Status                               |enum    |1-2147483648 - {value}                                                |

</blockquote></details>

<details><summary>D2-50-11 <i>(Type 0x11 (multi room ventilation unit with bypass))</i></summary><blockquote>

###### command: 0
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|RMT     |Requested Message Type                            |enum    |0 - Ventilation basic status                                          |
|        |                                                  |        |1 - Ventilation extended status                                       |

###### command: 1
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|DOMC    |Direct Operation Mode Control                     |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - No action (keep current ventilation mode/level)                  |
|OMC     |Operation Mode Control                            |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Select next operation mode (edge-trigger)                         |
|        |                                                  |        |2 - Select previous operation mode (edge-trigger)                     |
|        |                                                  |        |3 - Reserved                                                          |
|HBC     |Heat Exchanger Bypass Control                     |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Close bypass (edge-trigger)                                       |
|        |                                                  |        |2 - Open bypass (edge-trigger)                                        |
|        |                                                  |        |3 - Reserved                                                          |
|TOMC    |Timer Operation Mode Control                      |enum    |0 - No action                                                         |
|        |                                                  |        |1 - Start timer operation mode (edge-trigger)                         |
|COT     |CO2 Threshold                                     |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|HT      |Humidity Threshold                                |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|AQT     |Air Quality Threshold                             |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Default (use threshold configured in device)                    |
|RTT     |Room temperature threshold                        |value   |1.0-127.0 ↔ -63.0-63.0 °C                                             |

###### command: 2
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|OMS     |Operation Mode Status                             |enum    |0 - Off                                                               |
|        |                                                  |        |1 - Level 1                                                           |
|        |                                                  |        |2 - Level 2                                                           |
|        |                                                  |        |3 - Level 3                                                           |
|        |                                                  |        |4 - Level 4                                                           |
|        |                                                  |        |5-10 - Reserved                                                       |
|        |                                                  |        |11 - Automatic                                                        |
|        |                                                  |        |12 - Automatic on demand                                              |
|        |                                                  |        |13 - Supply air only                                                  |
|        |                                                  |        |14 - Exhaust air only                                                 |
|        |                                                  |        |15 - Reserved                                                         |
|SMS     |Safety Mode Status                                |enum    |0 - Fireplace safety mode disabled                                    |
|        |                                                  |        |1 - Fireplace safety mode enabled                                     |
|HBS     |Heat Exchanger Bypass Status                      |enum    |0 - Bypass closed (heat-recovery active)                              |
|        |                                                  |        |1 - Bypass opened (heat-recovery inactive)                            |
|SFP     |Supply Air Flap Position                          |enum    |0 - Supply air flap closed                                            |
|        |                                                  |        |1 - Supply air flap opened                                            |
|EFP     |Exhaust Air Flap Position                         |enum    |0 - Exhaust air flap closed                                           |
|        |                                                  |        |1 - Exhaust air flap opened                                           |
|DMS     |Defrost Mode Status                               |enum    |0 - Defrost mode inactive                                             |
|        |                                                  |        |1 - Defrost mode active                                               |
|CPS     |Cooling Protection Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|OHS     |Outdoor Air Heater Status                         |enum    |0 - Cooling protection mode inactive                                  |
|        |                                                  |        |1 - Cooling protection mode active                                    |
|SHS     |Outdoor Air Heater Status                         |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|DHS     |Drain Heater Status                               |enum    |0 - Inactive                                                          |
|        |                                                  |        |1 - Active                                                            |
|TOMS    |Timer Operation Mode Status                       |enum    |0 - timer operation mode inactive                                     |
|        |                                                  |        |1 - timer operation mode active                                       |
|FMS     |Filter Maintenance Status                         |enum    |0 - Maintenance not required                                          |
|        |                                                  |        |1 - Maintenance required                                              |
|WTPS    |Weekly Timer Program Status                       |enum    |0 - Weekly timer program disabled or not configured                   |
|        |                                                  |        |1 - Weekly timer program active                                       |
|RTCS    |Room Temperature Control Status                   |enum    |0 - Room temperature control inactive                                 |
|        |                                                  |        |1 - Room temperature control active                                   |
|AQS1    |Air Quality Sensor 1                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|MSS     |Master/Slave Configuration Status                 |enum    |0 - Master                                                            |
|        |                                                  |        |1 - Slave                                                             |
|AQS2    |Air Quality Sensor 2                              |enum    |0-100 - {value} %                                                     |
|        |                                                  |        |101-126 - Reserved                                                    |
|        |                                                  |        |127 - Not available                                                   |
|OUTT    |Outdoor Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYT   |Supply Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|INT     |Indoor Air Temperature                            |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|EXHT    |Exhaust Air Temperature                           |value   |0.0-127.0 ↔ -64.0-63.0 °C                                             |
|SPLYFF  |Supply Air Fan Air Flow Rate                      |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|EXHFF   |Exhaust Air Fan Air Flow Rate                     |value   |0.0-1023.0 ↔ 0.0-1023.0 m3/h                                          |
|SPLYFS  |Supply Fan Speed                                  |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |
|EXHFS   |Exhaust Fan Speed                                 |value   |0.0-4095.0 ↔ 0.0-4095.0 1/min                                         |

###### command: 3
|shortcut|description                                       |type    |values                                                                |
|--------|--------------------------------------------------|--------|----                                                                  |
|MT      |Message Type                                      |enum    |0-3 - Message Type {value}                                            |
|SVI     |Software Version Info                             |value   |0.0-4095.0 ↔ 0.0-4095.0                                               |
|OHC     |Operation Hours Counter                           |value   |0.0-65535.0 ↔ 0.0-196605.0                                            |
|DIS     |Digital Input 0...15 Status                       |enum    |1-32768 - {value}                                                     |
|DOS     |Digital Output 0...15 Status                      |enum    |1-32768 - {value}                                                     |
|IMS     |Info Message 0...15 Status                        |enum    |1-32768 - {value}                                                     |
|FS      |Fault 0...31 Status                               |enum    |1-2147483648 - {value}                                                |

</blockquote></details>

</blockquote></details>

</blockquote></details>
