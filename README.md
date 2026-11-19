# Thermodynamics Visualized: The Second Law & Entropy
This repository contains the Python/Manim source code for a video series visualizing the core concepts of the Second Law of Thermodynamics, the Clausius Inequality, and Entropy.

📺 **[Watch the full video series on YouTube](https://www.youtube.com/playlist?list=PLS5tmNdH2GK4
)**


## 📚 Reference Material
The mathematical derivations, figures, and concepts in these animations are directly based on:
* **Thermodynamics: An Engineering Approach, 5th Edition**
* **Authors:** Yunus A. Çengel and Michael A. Boles
* *(Specifically: Chapters 6 & 7 - The Second Law of Thermodynamics and Entropy)*

## ⚙️ Prerequisites
To run these animations on your machine, you will need:
1. **Python 3.9+** (Tested on Python 3.13)
2. **FFmpeg** (Required for Manim to process video)
3. **LaTeX** (Required for rendering mathematical equations, e.g., MiKTeX on Windows)

## 🚀 Installation & Setup

This project is built using [Manim Community](https://www.manim.community/) and `manim-voiceover` for the AI narration.

**Using `uv` (Recommended):**

    git clone https://github.com/XPlaneIT/Thermodynamics-Visualized-Entropy.git
    cd Thermodynamics-Visualized-Entropy
    uv venv
    uv sync

## 🎬 How to Run the Animations

Each file corresponds to a specific chapter in the video. To render a scene, use the following command format:

**For quick, low-quality previews (480p 15fps):**

    uv run manim -pql _014clausius_voiceover.py ClausiusInequalityDiagram

**For final, high-quality renders (1080p 60fps):**

    uv run manim -pqh _014clausius_voiceover.py ClausiusInequalityDiagram

*(Note: `-p` means play when finished, `q` is quality, `l` is low, `h` is high).*

## 📂 Repository Structure
* `_010voice_helper.py`: Custom Edge-TTS service for Manim Voiceover.
* `_013reversible_heat_engine.py`: Reversible heat engine intro.
* `_014clausius_voiceover.py`: Visualizing the Clausius Inequality.
* `_015entropy_definition.py`: Proving entropy is a property (Path Independence).
* `_016entropy_generation.py`: Deriving entropy generation.
* `_017increase_entropy.py`: The increase of entropy principle & subsystems.
* `entropy_part1.py`: Part 1 entropy animations.
