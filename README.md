# Fusion360 Cycloidal Gear Generator Add-In
You'll need to have a Fusion 360 installed and have downloaded this repo from github. If you download as a zip folder you'll need to have extracted the folder before you 'install'

To manually install (the only option provided for now):
1. Download this repo from github. If you download as a zip folder you'll need to have extracted the folder to continue
2. Open the Add-In's dialog from the Utilities workspace (keyboard shortcut is shift-s)
3. Click the Add-ins tab
4. CLick the small green '+' symbol at the top left of the dialog
5. This opens the add-in's folder (probably empty if this is your first add-in)
6. Copy the entire folder of the add-in to the add-ins folder
7. In Fusion360, click on the "Utilities" workspace tap
8. Click on  the Add-ins Icon in the toolbar
9. Click on the Add-ins tab of the Scripts and Add-Ins dialog box
10. Click the green '+' symbol next to "My Add-ins" (Opens file explorer to the Add-ins folder)
11. Copy the entire folder of the Add-in to the folder that just opened
12. Click on "Select Folder"
13. Click on the Add-ins toolbar button
14. Click on the 'Add-Ins" tab of the "Scripts and Add-Ins" dialog
15. Select cycloidal_gear_generator from the list
16. There should now be a new icon ![Go to media folder](media/16x16.png) next to the Add-Ins toolbar button

Video: Installing on Windows
https://youtu.be/6j6FxZL6bGs


A parametric cycloidal gear system generator add-in for Fusion360.

![Go to media folder](media/gear_cross_section.jpg)

## Calculating the gear reduction of a single stage cycloidal gear system 
The gear reduction of a single stage cycloidal drive is primarily determined by the number of pins (aka: stationary ring gear) and the cycloidal disc

Gear Reduction Ratio = 1 / (num_pins - 1)
Or simply one less than the number of pins

Example:

If a single stage cycloidal gear system has 11 pins:

10:1 (1 / (11 - 1) = 1 / 10 = 0.1)

With the above example, the output shaft will rotate 10 times for every single rotation of the input shaft.

## Key Points:

### Higher Pin Count: Increasing the number of pins on the ring gear results in a higher reduction ratio (slower output speed).

### Compact Design: Cycloidal gears are known for achieving high reduction ratios in a relatively compact size with very little backlash.

## Calculating the final gear reduction of a compound cycloidal gear assembly

Stage 1: Ring gear with 11 pins (R1 = 1 / (11 - 1) = 0.1)
Stage 2: Ring gear with 15 pins (R2 = 1 / (15 - 1) = 0.0714)
Final Gear Reduction Ratio = R1 * R2 = 0.1 * 0.0714 = 0.00714

140:1, meaning the output shaft will rotate 140 times slower than the input shaft.

Wikipedia article: https://en.wikipedia.org/wiki/Cycloidal_drive

## Configuration and Information dialogs:

![Go to media folder](media/variables.jpg)
![Go to media folder](media/calculated_values.jpg)

### Credit to mawildoer for original script (https://github.com/mawildoer/cycloidal_generator) and to https://github.com/bradlab-net for the grunt work of making the interactive add-in

ROBOT,ACTUATOR,GEAR,3D,PRINT,FUSION,360,FUSION360,ADD-IN,ADDIN,REDUCER
