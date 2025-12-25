#FusionPad

- FusionPad is a 6-key macropad with two rotary encoders and an OLED display. It is designed to be the ultimate companion for CAD work, specifically optimized for Fusion 360.

- It serves as a specialized tool to handle repetitive commands and navigation, allowing for a much faster design workflow.

#Features:

- Full 3D Printed Case: Durable, compact, and designed with internal heatset inserts.

- 0.91" OLED Display: Used to track current tool states and active layers.

- Dual EC11 Rotary Encoders: Two encoders to handle both zooming and timeline navigation simultaneously.

- 6 Keys: A 2x3 matrix for the most essential sketching and modeling shortcuts.

- KMK Firmware: Built on CircuitPython for instant, no-compile keymap updates.

#CAD Model:

Everything fits together using M3 bolts and heatset inserts for a robust feel. 

The design consists of a main enclosure body and a bottom cover. 

<img width="1735" height="862" alt="image" src="https://github.com/user-attachments/assets/ebd8c0d0-a424-4678-8f5c-d3f01c966195" />


Made in Fusion 360. It feels right to design a Fusion 360 controller inside Fusion 360!

#PCB

Here's the brain of the project! It uses a Seeed XIAO RP2040 mounted directly to the board. The 2x3 matrix utilizes diodes to prevent any ghosting when hitting shortcut combos.

#Schematic

<img width="1494" height="348" alt="image" src="https://github.com/user-attachments/assets/5e0e7827-f0e3-4ef1-854a-88e55e0628d4" />

#PCB Layout

<img width="532" height="829" alt="image" src="https://github.com/user-attachments/assets/24c6bda6-7c54-4fa4-b4bc-35eb4e76ea0f" />

I used MX-style footprints for the switches. The encoders are placed on the top corners for easy thumb or index finger access while your hand rests on the pad.

#Firmware Overview

This hackpad uses KMK firmware. Since it's CircuitPython-based, I can change my macros just by editing a text file on the drive.

Encoder 1: Set to Zoom (Mouse Wheel).

Encoder 2: Set to History Scrubbing (Undo/Redo).

Key 1-6: Mapped to Esc, Line (L), Dimension (D), Extrude (E), Search (S), and Enter.

OLED: Currently displays "FUSION 360" and the current active tool icon.


#BOM:

Here is the list of parts used for this build (all from the approved kit list):

6x MX-Style Switches

6x Blank DSA Keycaps (White)

4x M3x5x4mm Heatset inserts

4x M3x16mm Screws

6x 1N4148 Diodes

1x 0.91" 128x32 OLED Display (GND-VCC-SCL-SDA)

2x EC11 Rotary Encoders

1x Seeed XIAO RP2040

1x 3D Printed Case


<img width="507" height="907" alt="image" src="https://github.com/user-attachments/assets/a5be8645-744f-4883-a4fa-1cbe6dc00def" />

