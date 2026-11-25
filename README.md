Blender Python (`bpy`) Creative Automation Toolkit
An open-source collection of Python scripts and procedural workflows designed to streamline 3D modeling, scene assembly, and rendering pipelines in Blender.
This repository bridges the gap between creative direction and technical execution—allowing indie animators, series creators, and 3D artists to automate repetitive tasks without starting from scratch.
---
🚀 Key Features
Procedural Asset Generation: Quickly generate base meshes, modular environments, and randomized variations using lightweight `bpy` scripts.
Automated Scene & Lighting Setup: One-click studio lighting rigs, camera tracking setups, and world shader configurations.
Batch Rendering & Export: Automate multi-angle renders, turntable animations, and clean `.fbx`/`.glTF` exports for video and game pipelines.
Series Production Helpers: Standardized naming conventions, collection organization, and frame-range management for multi-episode projects.
---
🛠️ Prerequisites
Blender: Version `3.6 LTS` or `4.x+` recommended.
Python: Uses Blender's bundled Python interpreter (no external setup required for core scripts).
---
📦 Installation & Usage
Clone the repository:
```bash
   git clone https://github.com/YOUR_USERNAME/blender-python-automation.git
   ```
Open Blender and switch to the Scripting workspace tab at the top.
Click Open in the Text Editor and select any `.py` script from the `/scripts` folder.
Click Run Script (or press `Alt + P`) to execute the automation in your current scene.
---
📂 Repository Structure
```text
├── scripts/
│   ├── procedural_layout.py     # Generates base scene geometry and object arrays
│   ├── auto_lighting_rig.py     # Sets up a customizable 3-point lighting system
│   └── batch_render_frames.py   # Automates camera switching and output paths
├── templates/                   # Starter .blend configuration presets
└── README.md
```
---
🤝 Contributing
Contributions, issues, and feature requests are welcome! If you have a useful Blender automation snippet or workflow improvement:
Fork the project.
Create your feature branch (`git checkout -b feature/NewScript`).
Commit your changes (`git commit -m 'Add new camera rig script'`).
Push to the branch (`git push origin feature/NewScript`) and open a Pull Request.
---
📄 License
Distributed under the MIT License. Free to use, modify, and distribute for both personal and commercial creative projects.
