# DX Ball

A modern, full-screen recreation of the classic 1990s brick-breaker arcade game **DX-Ball**, built with **Python** and **Pygame**. Designed with retro aesthetics, 3D shaded graphics, procedural level layouts, real-time synthesized retro audio, and an in-game 3D Ball Shop.



## ✨ Key Features

### 🎮 Core Gameplay & Mechanics
* **Automatic Full-Screen Experience:** Dynamically detects screen resolution to launch in immersive full-screen mode.
* **Dynamic Level Progression:** Every level features a distinct procedural brick layout (Solid Blocks, Pyramids, Zig-Zag Checkerboards, and Arcade Patterns) with multi-hit armored bricks.
* **Magnetic / Sticky Catch System:** Catch the ball directly on the paddle and aim before manually launching it into play.
* **Dual Side-Cannon Lasers:** Equip the Laser ability to mount dual cannons on the paddle edges and blast through bricks.
* **Multi-Ball Split & Paddle Expansion:** Split active balls into multiple trajectories or expand paddle width for strategic control.

### 🎨 Visuals & Audio
* **3D Shaded Graphics:** Custom multi-layered 3D spheres with specular highlights, beveled bricks, particle explosion sparks, and floating score popups.
* **3D Rotating Checkered Sphere:** Main menu features a diagonally rotating 3D checkered sphere inspired by classic *DX-Ball 2* visuals.
* **Zero-Dependency Synthesized Audio:** Real-time waveform generation (`array` & `math`) produces retro background synth loops and crisp sound effects without requiring external `.wav` or `.mp3` assets.

### 🛒 3D Ball Shop & Persistence
* **Unlockable 3D Skins:** Collect coins during gameplay to unlock and equip custom 3D ball skins (*Chrome 3D*, *Solar Fireball*, *Neon Matrix*, *Cyber Void*, and *Royal Gold*).
* **Local Save System:** Automatically saves high scores, coin balances, and unlocked skins locally in `dxball_save.txt`.



## 🕹️ Controls

| Action | Control |
| :--- | :--- |
| **Move Paddle** | `Mouse` or `Left / Right Arrow Keys` (`A` / `D`) |
| **Shoot Laser / Release Magnetic Ball** | `Spacebar` or `Left Mouse Click` |
| **Pause / Resume Game** | `ESC` |



## 🎁 Power-Ups Guide

* **`SPLIT` (Cyan):** Splits the active ball into three simultaneous balls.
* **`WIDE` (Green):** Expands the paddle width for easier catches.
* **`LASER` (Purple):** Equips dual side-cannons on the paddle to shoot bricks.
* **`MAGNET` (Red):** Enables sticky paddle mode—catches the ball on contact for manual aiming.
* **`COIN` (Gold):** Awards `+10` bonus coins for the 3D Ball Shop.



## 🛠️ Installation & Setup

### Prerequisites
* **Python 3.8+**
* **Pygame**

### Steps to Run
1. **Clone or download** this repository to your local machine.
2. **Install Pygame** via terminal or command prompt:
   bash
   pip install pygame
