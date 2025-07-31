# HomographyTransformation

Made for "Iulian Munteanu". Good Luck!

author: freddy.meza.alfaro@gmail.com

This project uses **homography transformation** to warp a flat image so that it fits into a distorted quadrilateral shape — such as when projecting onto a table or viewing a flat object from an angle.

It’s ideal for applications like:
- Video projection mapping
- Correcting for projector distortion
- Simulating perspective changes in augmented reality

Imagine you have a **rectangular image** like this:
```
(0,0)      -----------      (800,0)
           |         |
           |         |
           |         |
(0,600)    -----------      (800,600)
```

But you want it to appear on a **trapezoid-shaped surface**, like a tilted table or wall:

```
(120,80)       ________      (750,60)
              /        \
             /          \
(100,600)   /____________\    (770,280)
```

Run it as follow:

```
python transform.py
```

If you found this project useful:
- ⭐ Give it a star on GitHub
- ☕ Or [buy me a coffee](https://coff.ee/freddymezai) to support future work!
