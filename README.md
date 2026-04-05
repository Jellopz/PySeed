This program, if ran, generates seeds that are saved to Downloads in a file named seeds.txt. (PySeed.py)
This program, if ran, generates tokens that fill the storage while taking massive amounts of resources. (RD.py)

PySeed.py works by generating cryptographically secure tokens and translating it into a format Minecraft Java seed generator can read. I made it like this because random isn't actually random and just takes from a massive list of numbers, which means someone could've gotten the same number/seed. With cryptographically secure numbers the CPU generates tokens which leads to seeds being more random, leaving an almost 0% chance someone else got the same number.

RD.py works by generating such a big token that the CPU just has to work harder, and because there are so many different characters it fills storage pretty quick. RD.py is just a joke BTW because I wanted something to code and I had no idea what to make.
