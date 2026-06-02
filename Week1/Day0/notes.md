# Week 1 - Day 0: Environment Setup & Productivity Workflow

## Overview

Day 0 focused on setting up a structured workflow for the Summer Analytics 2026 program.

The goal was to:

* Build a repeatable folder structure
* Learn useful PowerShell commands
* Create custom terminal utilities
* Configure GitHub CLI
* Understand basic file management from terminal
* Learn Jupyter Notebook productivity shortcuts

---

## Topics Covered

### 1. PowerShell Folder Automation

Creating multiple folders at once using PowerShell.

Concepts:

* `mkdir`
* `ForEach-Object`
* Arrays
* Variables

Example:

```powershell
'Day0'..'Day5' | ForEach-Object {
    New-Item -Path "Week1\$_" -ItemType Directory -Force
}
```

---

### 2. File Creation Methods

Methods explored:

```powershell
ni file.txt
```

```powershell
echo $null > file.txt
```

```powershell
New-Item -ItemType File
```

---

### 3. Custom Touch Command

Created a Linux-like `touch` command in PowerShell.

Example:

```powershell
function touch {
    $args | ForEach-Object {
        New-Item -Path $_ -ItemType File -Force
    }
}
```

Capabilities:

* Create files quickly
* Update timestamps
* Handle multiple files simultaneously

---

### 4. PowerShell Profile

Learned about:

```powershell
$PROFILE
```

Used for:

* Loading custom functions automatically
* Persisting aliases and shortcuts
* Personalizing PowerShell startup

---

### 5. Winget Package Manager

Windows package manager.

Examples:

```powershell
winget install GNU.Nano
```

```powershell
winget install vim.vim
```

Purpose:

* Install software directly from terminal
* Manage packages efficiently

---

### 6. Useful Terminal Commands

#### View file contents

```powershell
Get-Content notes.txt
```

Alias:

```powershell
cat notes.txt
```

---

#### Merge files

```powershell
gc a.txt,b.txt
```

---

#### Search within files

```powershell
Select-String "IMPORTANT" notes.md
```

Linux equivalent:

```bash
grep "IMPORTANT" notes.md
```

---

### 7. GitHub CLI Workflow

Repository creation completely from terminal.

```bash
gh auth login
git init
git add .
git commit -m "Initial Commit"
gh repo create summer-analytics-2026 --public --source=. --push
```

Daily workflow:

```bash
git add .
git commit -m "Day X Update"
git push
```

---

### 8. Jupyter Notebook Productivity

Useful shortcuts:

| Shortcut      | Action                 |
| ------------- | ---------------------- |
| Shift + Enter | Run cell and move next |
| Ctrl + Enter  | Run cell and stay      |
| Esc           | Command mode           |
| A             | Add cell above         |
| B             | Add cell below         |
| D D           | Delete cell            |
| M             | Markdown cell          |
| Y             | Code cell              |
| J/K           | Navigate cells         |

---

## Why These Commands Matter

### touch

Creates files instantly without opening an editor.

### grep / Select-String

Searches large notes and code files quickly.

### cat / Get-Content

Reads files directly from terminal.

### $PROFILE

Makes PowerShell customizable and reusable.

### GitHub CLI

Removes dependency on browser-based repository creation.

---

### 9. Jupyter Notebook vs JupyterLab

| Feature         | Jupyter Notebook          | JupyterLab                                              |
| --------------- | ------------------------- | ------------------------------------------------------- |
| Interface       | Single notebook interface | Multi-tab IDE-like interface                            |
| File Management | Basic                     | Built-in file browser                                   |
| Multiple Files  | One notebook at a time    | Multiple notebooks, terminals, and files simultaneously |
| Extensions      | Limited                   | Rich extension ecosystem                                |
| Best For        | Beginners, simple tasks   | Advanced workflows and projects                         |

**Summary:**

* **Jupyter Notebook** = Simple, lightweight notebook environment.
* **JupyterLab** = Modern development environment with tabs, terminals, file explorer, and more productivity features.

---

### 10. Google Colab

**Google Colab (Colaboratory)** is a cloud-based Jupyter Notebook environment provided by Google.
 
Advantages

* No installation required.
* Free CPU, GPU, and TPU access.
* Easy sharing through Google Drive.
* Pre-installed ML/Data Science libraries.

Adding CSV Files

Since notebooks run in the cloud, local files are not directly available.

```python
from google.colab import files
uploaded = files.upload()
```

Or mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

---

### 10. Kaggle Notebooks

**Kaggle Notebooks** are cloud notebooks integrated with Kaggle's datasets and competitions.

Advantages

* Free CPU/GPU/TPU resources.
* Direct access to Kaggle datasets.
* No setup required.
* Excellent for machine learning competitions.

Direct CSV/Dataset Access in Kaggle

A major advantage is that datasets can be attached directly from the **"Add Input"** button.

After adding a dataset:

```python
import pandas as pd

df = pd.read_csv('/kaggle/input/dataset-name/file.csv')
```

No manual upload is needed.

---

### Comparison with Other Platforms

| Platform      | Direct Dataset Attachment             |
| ------------- | ------------------------------------- |
| Kaggle        | ✅ Yes, through "Add Input"            |
| Google Colab  | ❌ Upload manually or use Google Drive |
| Local Jupyter | ❌ File must exist on your machine     |

---

### 11. GPU and TPU Availability

What is a GPU?

**GPU (Graphics Processing Unit)** contains thousands of small cores that perform many calculations in parallel.

Used For

* Deep Learning
* Neural Network Training
* Image Processing
* Large-scale matrix computations

Examples

* NVIDIA RTX 4090
* NVIDIA A100
* NVIDIA T4

---

What is a TPU?

**TPU (Tensor Processing Unit)** is a specialized processor developed by Google specifically for machine learning workloads.

Used For

* TensorFlow models
* Large AI model training
* High-speed matrix operations

Advantages over GPU

* Faster for some AI workloads
* More power efficient for TensorFlow-based training

---

## Availability

| Platform         | CPU                      | GPU                      | TPU        |
| ---------------- | ------------------------ | ------------------------ | ---------- |
| Local Jupyter    | Depends on your hardware | Depends on your hardware | Usually No |
| Google Colab     | ✅                        | ✅ (Free/Paid)            | ✅          |
| Kaggle Notebooks | ✅                        | ✅                        | ✅          |

---

## Cloud vs Local Execution

| Aspect            | Cloud Execution (Colab/Kaggle)             | Local Execution (Jupyter)                          |
| ----------------- | ------------------------------------------ | -------------------------------------------------- |
| Setup             | No installation needed                     | Installation required                              |
| Hardware Cost     | Free or subscription-based                 | User buys hardware                                 |
| GPU Access        | Often provided                             | Must own GPU                                       |
| TPU Access        | Available on some platforms                | Rarely available                                   |
| Internet Required | Yes                                        | No (after setup)                                   |
| Performance       | Depends on allocated resources             | Depends on local machine                           |
| Data Privacy      | Data stored on cloud servers               | Data remains on local machine                      |
| Collaboration     | Easy sharing                               | Manual sharing                                     |
| Storage Limits    | Limited cloud storage                      | Depends on local disk                              |
| Session Duration  | May disconnect after inactivity            | Runs continuously                                  |
| Best For          | Learning, experimentation, ML competitions | Large projects, sensitive data, long-running tasks |

## When to Use What?

### Use Cloud Execution When:

* Learning Data Science or ML.
* You need free GPU/TPU resources.
* Collaborating with others.
* Working from multiple devices.

### Use Local Execution When:

* Handling sensitive/private data.
* Running long-duration experiments.
* You have powerful hardware.
* Internet connectivity is unreliable.

**Rule of Thumb:**

* **Beginner → Google Colab**
* **Kaggle Competitions/Datasets → Kaggle Notebooks**
* **Professional Development & Full Control → Local Jupyter/JupyterLab**

---

## Key Takeaways

1. PowerShell syntax differs significantly from Linux Bash.
2. Repetitive tasks can be automated using loops.
3. Terminal-first workflows are faster than GUI workflows.
4. Custom PowerShell functions improve productivity.
5. GitHub repositories can be fully managed from terminal.
6. Jupyter shortcuts save considerable time during assignments.
7. Good folder organization prevents chaos later.

---