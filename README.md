# Laser-Distance-sensor-python

Make a distance sensor using any webcam, laser and python. Basic python skills will help, and you can learn about open CV in a couple of hours (as I did). We fix the webcam and laser onto a frame, then program the webcam to pick up the laser. We then calibrate it to understand what the position of the laser will be at different distances. Finally, we reverse this to give us the distance using the laser position.
Camera Tracking program filters the video, detects the laser position (if you want to print it simply remove the hash on line 72), and calculates distance using values taken from the calibration program. The calibration program gives these values.
