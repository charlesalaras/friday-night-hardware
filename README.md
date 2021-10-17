<p align="center">
  <img src="fnflogoedit.png" height="256">
</p>

![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)

# About
[Demo](https://www.youtube.com/watch?v=g3J5mf7iiGk)

Friday Night Hardware is a recreation of one of the levels from the browser / standalone game ["Friday Night Funkin'"](https://github.com/ninjamuffin99/Funkin). This was my final project for an Introduction to Embedded Systems course, taken in Spring 2021. The game utilizes many fundamental concepts taught in embedded systems, including state machines, task scheduling, time multiplexing, button debouncing, timer period, and much more.
# Component + File Guide
The following breadboard components were used to build the game:
- 2x ATMEGA1284P Processor (+ programmer)
- LED Matrix
- Piezoelectric Speaker
- Resistors
- 4 Buttons
- 3x Green LEDs
- Jumper Cables
- Power DIP + AC Adapter

# Dependencies
The game makes usage of the AVR Toolchain and various header files to function properly. Files provided by the instructor are as follows: `pwm.h`, `simAVRHeader.h`, `timer.h`.

Below are the descriptions of each file. *Italicized* files are not included for reasons denoted in the [Security](#Security) section:
- **MidiFreq.py**: This script was used to convert the MIDI song into a C-readable format. Specifically, the song is split into a rhythm and melody array. The script makes use of the library [mido](https://github.com/mido/mido) in order to parse the midi file.
- **gcd.cpp**: This file includes various utility scripts for reducing the memory footprint of the song arrays. Specifically, we use the `findGCD(arr, n)` function to reduce the number by a constant factor. Since mido only gives us on and off notes, offset between notes is also calculated.
- *tick.h*: Contains Tasks 2-5. Task 2 spawns notes into the LED Matrix based on whichever section of the song the user is currently at. It also sets a fail flag if the user has failed and the game should stop. Task 3 percolates bits up within the LED Matrix. Task 4 updates the matrix using time multiplexing. Task 5 tracks user input.
- *song.h*: Contains arrays created from `MidiFreq.py` and `gcd.cpp`.
- *main.c*: Schedules and orchestrates Tasks 2-5, which are focused on gameplay I/O. Runs on a 1 ms timer, utilizing the first ATMEGA1284P processor.
- *main2.c*: Plays the song for the game. Since playing the song utilizes large arrays (roughly 1000 elements), it was ultimately placed into a second ATMEGA1284P processor to save on memory constraints.

# Security
As this project was completed for a course, I am currently seeking approval to post the code publicly. Specifically, this is to ensure that this work is not plagiarized by future students who may take this Intro to Embedded Systems course. If approval is given, all source code will also be posted here. The demo and descriptions of each file are instead posted here.

# Credits
A special thank you to [Frank Vahid](https://www.cs.ucr.edu/~vahid/) for teaching this course, it was an absolute blast. The inspiration for this project came from Friday Night Funkin', a game created by [Cameron Taylor](https://github.com/ninjamuffin99). Please [check it out](https://github.com/ninjamuffin99/Funkin), as a lot of love and care was put into the original game. The original song used in this game was created by [KawaiSprite](https://twitter.com/kawaisprite), while the MIDI recreation used in this project was found [here](https://onlinesequencer.net/1870646). A big thank you to whoever made this rendition, it saved a ton of headache that would've been faced when playing the song on a piezoelectric speaker. The original Friday Night Funkin' logo was created by [PhantomArcade3k](https://twitter.com/phantomarcade3k) and [Evilsk8r](https://twitter.com/evilsk8r).

# Final Notes
If you have any questions or concerns, feel free to reach out to me, or create an issue on this project. I am happy to take down anything that may need to be taken down, or change anything that needs to be changed.
