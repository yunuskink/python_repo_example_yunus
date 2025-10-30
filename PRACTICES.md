# VS Code Setup Guide for Data Scientists & Researchers

**Purpose:** Empower data scientists and researchers to work more efficiently with modern development tools  
**Audience:** Data cleaning, analysis, and visualization professionals  
**Duration:** 60-90 minute meeting

---

## 📋 Table of Contents

2. [Managing Python Environments](#python-environments)
3. [GitHub Integration](#github-integration)
4. [GitHub Copilot for Data Work](#copilot-integration)
5. [Project Folder Structure](#folder-structure)
6. [Roadmaps & Task Tracking](#roadmaps-and-issues)
7. [Quick Reference](#quick-reference)

---

## 🎯 Why VS Code for Data Science? {#why-vs-code}

## 🐍 Managing Python Environments {#python-environments}

### **Why Multiple Environments?**

**The Problem:**
```python
# Project A needs pandas 1.5
pip install pandas==1.5

# Project B needs pandas 2.0
pip install pandas==2.0  # This breaks Project A! 😱
```

**The Solution: Virtual Environments**
```
📁 Project A
   └── venv/ (pandas 1.5)
   
📁 Project B  
   └── venv/ (pandas 2.0)
```

Each project has its own isolated Python environment.

### **Setting Up Environments in VS Code**

#### **Step 1: Create a Virtual Environment**

```bash
# Open VS Code terminal (Ctrl + `)
cd /path/to/your/project

# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# You should see (venv) in your terminal now
```

#### **Step 2: Tell VS Code to Use It**

1. Press `Ctrl+Shift+P` (Command Palette)
2. Type: `Python: Select Interpreter`
3. Choose the one with `./venv/bin/python`
4. VS Code will now use this environment automatically!

#### **Step 3: Install Your Packages**

```bash
# With venv activated:
pip install pandas numpy matplotlib seaborn scikit-learn

# Save your requirements so others can replicate:
pip freeze > requirements.txt
```

#### **Step 4: Share with Your Team**

When a colleague clones your project:
```bash
# They just run:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Now they have the exact same setup as you!
```

### **VS Code Environment Features**

**Status Bar Shows Active Environment:**
```
Bottom-left corner: Python 3.11.5 ('venv')
Click it to switch environments!
```

**Auto-Activation:**
- When you open a terminal, VS Code activates the venv automatically
- When you run Python files, it uses the selected environment
- When using Jupyter notebooks, kernel connects to your venv

**Environment Indicator in Files:**
```python
# Top-right corner shows: venv (Python 3.11.5)
import pandas as pd  # This imports from your venv, not system Python
```

### **Best Practices**

✅ **DO:**
- Create a new venv for each project
- Use descriptive names: `venv`, `env`, or `.venv`
- Add `venv/` to `.gitignore` (environments are big, don't commit them)
- Use `requirements.txt` to document dependencies
- Update requirements regularly: `pip freeze > requirements.txt`

❌ **DON'T:**
- Install packages globally (always activate venv first)
- Commit the `venv/` folder to Git (waste of space)
- Forget which environment you're using (check status bar!)
- Mix conda and venv (pick one and stick with it)

---

## 🔗 GitHub Integration {#github-integration}

### **Git Basics in VS Code**

#### **The Three-Step Process**

Every change you make goes through three stages:

```
Working Directory  →  Staging Area  →  Repository  →  GitHub
(your files)          (ready to save)   (saved)       (backed up)
     │                     │                │              │
     │                     │                │              │
  [Edit]  ────────────→ [Stage] ──────→ [Commit] ────→ [Push]
                         (git add)      (git commit)  (git push)
```

#### **Visual Workflow in VS Code**

**1. Make Changes:**
```python
# You edit: clean_data.py
df = pd.read_csv('housing.csv')
df = df.dropna()  # Added this line
```

**2. See Changes:**
- Click Source Control icon (left sidebar, 3rd from top)
- You'll see `clean_data.py` with an "M" (Modified)
- Click the file to see diff (red = removed, green = added)

**3. Stage Changes:**
- Click `+` next to the file (or click "Stage All Changes")
- File moves to "Staged Changes" section
- This says: "I want to save these changes"

**4. Commit (Save):**
- Type a commit message in the text box at top:
  ```
  Add data cleaning step to remove missing values
  ```
- Click checkmark (✓) or press `Ctrl+Enter`
- Changes are now saved to your local Git history!

**5. Push (Backup to GitHub):**
- Click `...` menu → Push
- Or click ↑ arrow in status bar
- Your changes are now on GitHub! 🎉

### **Reading the Diff View**

```python
# Red (removed):
- df = pd.read_csv('housing.csv')  # Old version

# Green (added):
+ df = pd.read_csv('housing.csv')
+ df = df.dropna()  # New version with cleaning step
```
### **Common Workflows**

#### **Scenario 1: Starting a New Project**

Use VS Code:
1. `Ctrl+Shift+P` → "Publish to GitHub"
2. Choose public/private
3. Done!

#### **Scenario 2: Daily Work**

```
Morning:
1. Click ↓ (Pull) to get teammate's changes
2. Make your edits
3. Stage → Commit → Push

Afternoon:
4. More edits
5. Stage → Commit → Push

Evening:
6. Pull again before going home
```
#### **Scenario 3: "Oh no, I broke everything!"**

**Going back in time:**
1. Click Source Control icon
2. Click clock icon (View History)
3. Right-click a previous commit
4. "Restore File" or "Revert Commit"
5. Your code is back to that version! 🎉

### **GitHub Integration Features**

#### **View File History**

```
Right-click any file → "Open Timeline"

You can see:
- Every change made to this file
- Who made each change
- When it was changed
- Click to view that version
```

#### **Blame (Who wrote this code?)**

```
Right-click in any file → "Git: View Line History"

Shows:
- Who wrote each line
- When they wrote it
- The commit message explaining why
```

Useful for: "Why did we remove outliers this way?" → Check the commit message!

#### **Compare Versions**

```
Timeline → Right-click any version → "Compare with Working File"

See exactly what changed between then and now
```

### **Collaboration Features**

#### **Pull Requests (Advanced)**

When you want to suggest changes to a project:
1. Create a branch: `git checkout -b my-analysis`
2. Make changes
3. Push: `git push origin my-analysis`
4. Go to GitHub → Create Pull Request
5. Team reviews and discusses your changes
6. Merge when approved

#### **Issues (Task Tracking)**

Create issues directly in VS Code:
1. Click GitHub icon (sidebar)
2. Click `+` next to "Issues"
3. Fill in title and description
4. Assign to yourself
5. Track in VS Code as you work

### **Best Practices**

✅ **DO:**
- Commit often (every logical change)
- Write descriptive commit messages
- Pull before you start working (get latest changes)
- Push at end of day (backup your work)
- Use branches for experiments

❌ **DON'T:**
- Commit large data files (use .gitignore)
- Commit sensitive data (passwords, API keys)
- Make huge commits with 50 changes
- Work for days without committing
- Force push (you'll overwrite teammates' work)

### **.gitignore for Data Science**

Create a `.gitignore` file in your project root:

```gitignore
# Python
venv/
env/
__pycache__/
*.pyc
.ipynb_checkpoints/

# Data files (don't commit data to Git!)
*.csv
*.xlsx
*.parquet
*.hdf5
data/raw/
data/processed/

# Output files
*.png
*.pdf
plots/
results/

# Sensitive
.env
config/secrets.json
*.key

# OS
.DS_Store
Thumbs.db
```

**Important:** Git is for code, not data. Store data elsewhere (S3, shared drive, etc.)

### **Common Git Issues**

**"Merge conflict":**
```
Both you and teammate edited the same line.
VS Code shows:
<<<<<<< HEAD
your version
=======
their version
>>>>>>> 

Choose which to keep, delete the conflict markers, commit.
```

**"Detached HEAD":**
```
You're looking at an old commit.
To get back: git checkout main
```

**"Fatal: not a git repository":**
```
You're not in a Git project folder.
Run: git init
```

---

## 🤖 GitHub Copilot for Data Work {#copilot-integration}

### **What is Copilot?**

**Think of it as:**
- Pair programming with an AI that knows millions of code patterns
- Autocomplete on steroids
- A coding assistant that suggests entire functions

**What it's NOT:**
- Magic that writes perfect code every time
- A replacement for understanding your data
- Always correct (you still need to review!)

### **Why Copilot for Data Science?**

**Traditional Workflow:**
```
1. Remember pandas syntax → Google it → Find Stack Overflow → Copy-paste → Modify
2. Write boilerplate data cleaning code for the 100th time
3. Forget matplotlib parameters → Check documentation → Trial and error
```

**With Copilot:**
```
1. Start typing what you want → Copilot suggests it → Accept → Done
2. Write a comment describing what you need → Copilot writes the code
3. Type "plt.figure" → Copilot completes with sensible defaults
```

### **Installing Copilot**

**Prerequisites:**
- GitHub account (free or paid)
- VS Code

**Installation:**
1. Press `Ctrl+Shift+X` (Extensions)
2. Search: "GitHub Copilot"
3. Install
4. Sign in with GitHub when prompted
5. You should see Copilot icon in status bar (bottom-right)

**Cost:**
- Free for students and open-source maintainers
- $10/month for individuals
- $19/month for businesses
- Free trial available

### **How to Use Copilot**

#### **1. Inline Suggestions (Ghost Text)**

As you type, Copilot suggests completions in gray text:

```python
# You type:
import pandas as pd
df = pd.read_csv('housing.csv')
df_clean = df.dropna

# Copilot suggests (in gray):
df_clean = df.dropna()  # Press Tab to accept
```

**Accept:** `Tab`  
**Reject:** Keep typing or `Esc`  
**Next suggestion:** `Alt+]`  
**Previous suggestion:** `Alt+[`

#### **2. Comment-Driven Development**

Write a comment describing what you want:

```python
# Load housing data and remove rows where price is missing or negative
```

Press `Enter`, and Copilot suggests:

```python
# Load housing data and remove rows where price is missing or negative
df = pd.read_csv('housing_data.csv')
df = df[df['price'].notna()]
df = df[df['price'] > 0]
```

Press `Tab` to accept!

#### **3. Function Generation**

Start a function signature:

```python
def calculate_affordability_burden(energy_cost, income):
```

Copilot suggests the body:

```python
def calculate_affordability_burden(energy_cost, income):
    """Calculate energy burden as percentage of income."""
    if income == 0:
        return None
    return (energy_cost / income) * 100
```

#### **4. Copilot Chat (Ask Questions)**

Press `Ctrl+I` to open Copilot Chat inline:

**Example conversations:**

```
You: "How do I remove outliers using IQR method?"

Copilot: 
```python
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_clean = df[(df['column'] >= lower_bound) & (df['column'] <= upper_bound)]
```
```

```
You: "Explain this code"
[Select some complex code]

Copilot: "This code performs a left join between two dataframes, 
merging on the 'id' column. It keeps all rows from the left dataframe 
and adds matching columns from the right dataframe..."
```

```
You: "Fix this bug"
[Select broken code]

Copilot: [Suggests corrected version with explanation]
```

### **Real Data Science Examples**

#### **Example 1: Data Cleaning Pipeline**

**You write:**
```python
# Create a function to clean housing data:
# - Remove rows with missing values in critical columns
# - Convert year_built to building_age
# - Cap outliers in price at 99th percentile
# - Create price_per_sqft column
```

**Copilot suggests:**
```python
def clean_housing_data(df):
    # Remove rows with missing critical values
    critical_cols = ['price', 'sqft', 'year_built', 'location']
    df = df.dropna(subset=critical_cols)
    
    # Convert year_built to age
    current_year = pd.Timestamp.now().year
    df['building_age'] = current_year - df['year_built']
    
    # Cap outliers
    cap_value = df['price'].quantile(0.99)
    df['price'] = df['price'].clip(upper=cap_value)
    
    # Create price per sqft
    df['price_per_sqft'] = df['price'] / df['sqft']
    
    return df
```

#### **Example 2: Visualization**

**You write:**
```python
# Create a subplot with 2 charts:
# 1. Histogram of energy burden distribution
# 2. Scatter plot of income vs energy cost, colored by burden category
```

**Copilot suggests:**
```python
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Histogram
axes[0].hist(df['energy_burden'], bins=50, color='skyblue', edgecolor='black')
axes[0].set_xlabel('Energy Burden (%)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Distribution of Energy Burden')

# Scatter plot
scatter = axes[1].scatter(df['income'], df['energy_cost'], 
                          c=df['burden_category'], cmap='RdYlGn_r', alpha=0.6)
axes[1].set_xlabel('Household Income ($)')
axes[1].set_ylabel('Energy Cost ($)')
axes[1].set_title('Income vs Energy Cost')
plt.colorbar(scatter, ax=axes[1], label='Burden Category')

plt.tight_layout()
plt.show()
```

#### **Example 3: Statistical Analysis**

**You write:**
```python
# Calculate correlation between housing characteristics and energy burden
# Show top 10 most correlated features
```

**Copilot suggests:**
```python
# Calculate correlations with energy burden
correlations = df.corr()['energy_burden'].sort_values(ascending=False)

# Remove self-correlation and show top 10
top_correlations = correlations[correlations.index != 'energy_burden'].head(10)

print("Top 10 Features Correlated with Energy Burden:")
print(top_correlations)

# Visualize
top_correlations.plot(kind='barh', figsize=(10, 6))
plt.xlabel('Correlation Coefficient')
plt.title('Features Most Correlated with Energy Burden')
plt.tight_layout()
plt.show()
```

### **Copilot Best Practices**

✅ **DO:**
- **Write detailed comments** - More context = better suggestions
- **Review suggestions carefully** - Copilot isn't always right
- **Use descriptive variable names** - Helps Copilot understand context
- **Break complex tasks into steps** - Comment each step
- **Use Copilot Chat for explanations** - Great learning tool
- **Accept partial suggestions** - Tab accepts, then modify

❌ **DON'T:**
- **Blindly accept everything** - Always review code
- **Use Copilot for sensitive operations** - Review security-critical code carefully
- **Expect perfect code** - It's a tool, not a replacement for thinking
- **Forget to test** - Copilot suggestions still need testing
- **Copy code you don't understand** - Use Chat to ask for explanation

### **Copilot Keyboard Shortcuts**

| Action | Shortcut |
|--------|----------|
| Accept suggestion | `Tab` |
| Reject suggestion | `Esc` |
| Next suggestion | `Alt + ]` |
| Previous suggestion | `Alt + [` |
| Open Copilot Chat | `Ctrl + I` |
| Open Copilot panel | `Ctrl + Shift + I` |
| Trigger suggestion | `Alt + \` |

### **Copilot Chat Commands**

```
/explain - Explain selected code
/fix - Suggest fixes for problems
/tests - Generate unit tests
/help - Show all commands
```

**Example:**
```
Select code → Ctrl+I → Type "/explain" → Enter
Copilot explains what the code does line by line
```

### **When Copilot Shines**

🌟 **Great for:**
- Boilerplate data cleaning code
- Common pandas operations
- Matplotlib/seaborn styling
- Regex patterns
- Error handling
- Documentation strings
- Unit tests
- SQL queries
- File I/O operations

⚠️ **Use caution for:**
- Domain-specific calculations (verify formulas)
- Statistical methods (check assumptions)
- Production code (needs thorough review)
- Security-sensitive operations
- Custom business logic

### **Troubleshooting**

**Copilot not showing suggestions:**
1. Check status bar (bottom-right) - Is Copilot enabled?
2. Try `Alt + \` to manually trigger
3. Check your internet connection
4. Restart VS Code

**Suggestions are wrong:**
1. Add more context in comments
2. Use descriptive variable names
3. Try asking Copilot Chat for explanation
4. Reject (`Esc`) and write manually

**Copilot suggests code from wrong language:**
1. Check file extension (.py for Python)
2. Set language mode: Click bottom-right → Select "Python"

---

## 📁 Project Folder Structure {#folder-structure}

### **Why Structure Matters**

**Bad structure:**
```
my_project/
├── analysis.py
├── analysis_v2.py
├── analysis_FINAL.py
├── analysis_FINAL_REALLY.py
├── data.csv
├── data_clean.csv
├── plot1.png
├── plot2.png
└── some_script.py
```
😱 Which file is current? Where's the original data? What does `some_script.py` do?

**Good structure:**
```
energy_affordability/
├── data/
│   ├── raw/                 # Never modify these!
│   ├── processed/           # Cleaned data
│   └── results/             # Analysis outputs
├── notebooks/               # Jupyter notebooks for exploration
├── scripts/                 # Python scripts for production
│   ├── 01_clean_data.py
│   ├── 02_feature_engineering.py
│   └── 03_analyze.py
├── reports/                 # Generated reports, figures
│   ├── figures/
│   └── paper_draft.pdf
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── .gitignore
├── README.md
├── requirements.txt
└── environment.yml
```
✅ Clear organization! Easy to find everything!

### **Recommended Structure for Data Science Projects**

#### **Template 1: Basic Analysis Project**

```
project_name/
│
├── data/
│   ├── raw/                      # Original, immutable data
│   │   ├── recs_2020.csv
│   │   └── acs_data.csv
│   ├── interim/                  # Intermediate, transformed data
│   │   └── recs_cleaned.csv
│   └── processed/                # Final datasets for modeling
│       └── model_ready.csv
│
├── notebooks/                    # Jupyter notebooks
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_visualizations.ipynb
│
├── scripts/                      # Python scripts
│   ├── __init__.py
│   ├── data_processing.py       # Data loading and cleaning
│   ├── features.py              # Feature engineering
│   ├── visualization.py         # Plotting functions
│   └── utils.py                 # Helper functions
│
├── reports/                      # Generated analysis outputs
│   ├── figures/                 # Saved plots
│   │   ├── income_distribution.png
│   │   └── burden_by_state.png
│   └── final_report.html        # Generated from notebook
│
├── tests/                        # Unit tests (optional but good!)
│   ├── test_data_processing.py
│   └── test_features.py
│
├── .gitignore                    # Files to ignore in Git
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── config.py                     # Configuration settings
```

#### **Template 2: Research Project**

```
research_project/
│
├── data/
│   ├── raw/                      # Original data (never modify!)
│   ├── processed/                # Cleaned, analysis-ready
│   └── README.md                 # Data dictionary
│
├── analysis/
│   ├── exploratory/              # Initial explorations
│   ├── main/                     # Core analysis notebooks
│   └── sensitivity/              # Robustness checks
│
├── paper/                        # Manuscript
│   ├── manuscript.tex
│   ├── figures/                  # Paper figures
│   └── tables/                   # Paper tables
│
├── presentations/
│   ├── conference_2024.pptx
│   └── lab_meeting.pdf
│
├── src/                          # Source code
│   ├── data/                     # Data processing
│   ├── models/                   # Statistical models
│   ├── visualization/            # Plotting
│   └── utils/                    # Helper functions
│
├── results/                      # Model outputs
│   ├── model_outputs/
│   └── statistical_tests/
│
├── docs/                         # Documentation
│   ├── methodology.md
│   └── data_sources.md
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

#### **Template 3: Dashboard/App Project**

```
dashboard_project/
│
├── backend/                      # API server
│   ├── app.py                   # Flask/FastAPI app
│   ├── data_processing.py       # Data processing
│   ├── config.py                # Configuration
│   └── requirements.txt         # Backend dependencies
│
├── frontend/                     # Web interface
│   ├── src/
│   │   ├── components/          # UI components
│   │   ├── pages/               # Page routes
│   │   └── utils/               # Helper functions
│   ├── public/                  # Static assets
│   └── package.json             # Frontend dependencies
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
│   ├── backend/
│   └── frontend/
│
├── docs/                         # Documentation
│   ├── api_reference.md
│   └── user_guide.md
│
├── .gitignore
├── README.md
├── docker-compose.yml           # For deployment
└── ROADMAP.md                   # Project roadmap
```

### **Best Practices for Each Folder**

#### **📂 data/**

✅ **DO:**
- Keep `raw/` data completely unchanged (treat as read-only)
- Add `data/README.md` explaining each dataset
- Document data sources and collection dates
- Use descriptive filenames: `recs_2020_public_use.csv`

❌ **DON'T:**
- Commit large data files to Git (add `data/` to `.gitignore`)
- Mix raw and processed data
- Store data in repository root

**Example data/README.md:**
```markdown
# Data Dictionary

## raw/recs_2020.csv
- **Source:** U.S. EIA Residential Energy Consumption Survey
- **Downloaded:** 2024-03-15
- **URL:** https://www.eia.gov/consumption/residential/data/2020/
- **Rows:** 18,496 households
- **Columns:** 784 variables

## processed/households_clean.csv
- **Created by:** scripts/01_clean_data.py
- **Date:** 2024-10-15
- **Description:** Cleaned RECS data with outliers removed
- **Rows:** 18,234 (262 outliers removed)
```

#### **📓 notebooks/**

✅ **DO:**
- Number notebooks in order: `01_`, `02_`, `03_`
- Use descriptive names: `02_income_distribution_analysis.ipynb`
- Add markdown cells explaining your thinking
- Clear outputs before committing (keeps Git clean)
- Use notebooks for exploration, scripts for production

❌ **DON'T:**
- Have 50 untitled notebooks
- Leave notebooks in random execution order
- Commit notebooks with massive outputs (slows Git)
- Use notebooks for code that will run in production

**VS Code Settings for Notebooks:**
```json
// settings.json
{
  "notebook.output.textLineLimit": 30,
  "notebook.cellToolbarVisibility": "visible",
  "jupyter.askForKernelRestart": false
}
```

#### **📜 scripts/**

✅ **DO:**
- Use clear, descriptive names: `calculate_energy_burden.py`
- Add docstrings to all functions
- Number scripts if they run in sequence
- Make scripts runnable: `if __name__ == "__main__":`
- Import from other scripts: `from data_processing import clean_data`

❌ **DON'T:**
- Have scripts with unclear names: `script1.py`, `test.py`
- Duplicate code across scripts (make utility functions)
- Hardcode file paths (use config or arguments)

**Example script structure:**
```python
"""
Clean and prepare RECS housing data for analysis.

This script loads raw RECS data, removes outliers, creates derived
variables, and exports analysis-ready dataset.

Usage:
    python scripts/01_clean_data.py
"""

import pandas as pd
from pathlib import Path

# Configuration
DATA_DIR = Path(__file__).parent.parent / 'data'
RAW_DATA = DATA_DIR / 'raw' / 'recs_2020.csv'
OUTPUT_DATA = DATA_DIR / 'processed' / 'recs_clean.csv'

def load_raw_data(filepath):
    """Load raw RECS data with proper dtypes."""
    return pd.read_csv(filepath)

def remove_outliers(df, column, n_std=3):
    """Remove outliers beyond n standard deviations."""
    mean = df[column].mean()
    std = df[column].std()
    return df[
        (df[column] >= mean - n_std * std) & 
        (df[column] <= mean + n_std * std)
    ]

def main():
    """Main execution function."""
    print("Loading data...")
    df = load_raw_data(RAW_DATA)
    
    print(f"Loaded {len(df)} rows")
    
    print("Removing outliers...")
    df = remove_outliers(df, 'energy_cost')
    
    print(f"After cleaning: {len(df)} rows")
    
    print(f"Saving to {OUTPUT_DATA}")
    df.to_csv(OUTPUT_DATA, index=False)
    
    print("Done!")

if __name__ == "__main__":
    main()
```

#### **📊 reports/**

✅ **DO:**
- Save high-resolution figures: `plt.savefig('figure.png', dpi=300)`
- Use descriptive names: `burden_by_income_quintile.png`
- Keep figures separate from other outputs
- Generate reports programmatically (Jupyter → HTML/PDF)

#### **🧪 tests/**

✅ **DO:**
- Name test files: `test_*.py`
- Test critical functions (data cleaning, calculations)
- Run tests before committing: `pytest tests/`

**Example test:**
```python
# tests/test_calculations.py
import pytest
from scripts.features import calculate_energy_burden

def test_energy_burden_calculation():
    """Test energy burden percentage calculation."""
    cost = 2400  # $2400/year
    income = 40000  # $40k/year
    
    result = calculate_energy_burden(cost, income)
    
    assert result == 6.0  # Should be 6%

def test_energy_burden_zero_income():
    """Test handling of zero income edge case."""
    result = calculate_energy_burden(2400, 0)
    
    assert result is None  # Should return None, not error
```

#### **📖 docs/**

✅ **DO:**
- Create `README.md` in project root (first thing people see)
- Add methodology documentation
- Document data sources
- Include setup instructions

**Example README.md:**
```markdown
# Energy Affordability Analysis

Analysis of residential energy cost burdens across U.S. households.

## Setup

```bash
# Create environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Data Sources

- RECS 2020: Residential energy consumption
- ACS 5-Year: Household demographics

## Project Structure

- `data/`: Raw and processed datasets
- `notebooks/`: Exploratory analysis
- `scripts/`: Production code
- `reports/`: Generated figures and reports

## Usage

Run analysis pipeline:
```bash
python scripts/01_clean_data.py
python scripts/02_analysis.py
```

## Contact

Questions? Email: your.email@university.edu
```

### **VS Code Features for Project Organization**

#### **1. Workspace Settings**

Save project-specific settings:

```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/.ipynb_checkpoints": true
  },
  "python.analysis.extraPaths": [
    "${workspaceFolder}/scripts"
  ]
}
```

This allows imports like:
```python
from data_processing import clean_data  # Works!
```

#### **2. Multi-Root Workspaces**

Working on frontend + backend? Add both to one workspace:

```
File → Add Folder to Workspace
Save as: energy_affordability.code-workspace
```

Now you see both in one window!

#### **3. File Explorer Organization**

Right-click folders → Create:
- `New File`
- `New Folder`
- Drag and drop to reorganize

#### **4. Quick File Navigation**

- `Ctrl+P` → Type filename → Jump directly
- `Ctrl+Shift+E` → File explorer
- `Ctrl+B` → Toggle sidebar

### **Common Mistakes to Avoid**

❌ **Flat structure (everything in root):**
```
project/
├── analysis1.py
├── analysis2.py
├── data.csv
├── data_clean.csv
├── plot.png
└── test.py
```

❌ **Too many nested levels:**
```
project/
└── src/
    └── python/
        └── scripts/
            └── data/
                └── processing/
                    └── clean.py  # Too deep!
```

❌ **Unclear naming:**
```
project/
├── stuff/
├── old/
├── temp/
└── misc/
```

### **When to Refactor Structure**

🚨 **Warning signs:**
- Can't find files quickly
- Same code in multiple places
- Notebooks named "Untitled1", "Untitled2"...
- No one else can run your code
- "Where did I put that analysis?"

✅ **Solution:** Take 30 minutes to reorganize using templates above

---

## 🗺️ Roadmaps & Task Tracking {#roadmaps-and-issues}

### **Why Track Tasks?**

**The Problem:**
```
❌ "What was I working on again?"
❌ "Did I finish that analysis?"
❌ "What should I do next?"
❌ Constantly switching between 10 priorities
❌ Forgetting to document decisions
```

**The Solution:**
```
✅ Clear roadmap of priorities
✅ Track progress visually
✅ Remember context for each task
✅ Know what's blocking what
✅ Document decisions in issues
```

### **Two-Level System**

**Level 1: ROADMAP.md** (Strategic, high-level)
- Where are we going?
- What are the big milestones?
- What's the priority?

**Level 2: GitHub Issues** (Tactical, detailed)
- What specific tasks need doing?
- Who's working on what?
- What's the status of each task?

### **Creating a Roadmap**

#### **Location:**
```
project/
├── ROADMAP.md              # Overall project roadmap
├── backend/
│   └── ROADMAP.md          # Backend-specific
└── frontend/
    └── ROADMAP.md          # Frontend-specific
```

#### **Format: Quarterly Timeline**

```markdown
# Energy Affordability Analysis - Roadmap

**Last Updated:** 2025-10-29

---

## 🎯 Q4 2024 (✅ Complete)

- [x] Collect RECS 2020 data
- [x] Initial exploratory analysis
- [x] Identify research questions

## 🚀 Q1 2025 (🚧 In Progress - 60%)

**Goal:** Complete affordability burden analysis

### High Priority
- [x] Clean RECS data and remove outliers [#1]
- [ ] Calculate energy burden metrics [#2] 
- [ ] Create state-level visualizations [#3]
- [ ] Draft methodology section [#4]

### Medium Priority
- [ ] Compare to previous studies [#5]
- [ ] Sensitivity analysis [#6]

### Low Priority
- [ ] Interactive dashboard prototype

**Blockers:**
- Waiting for updated ACS data release (Feb 2025)

## 📋 Q2 2025 (Planned)

**Goal:** Finalize paper and submit

- [ ] Complete all analyses
- [ ] Write results section
- [ ] Create publication-quality figures
- [ ] Submit to Energy Policy journal
- [ ] Present at ACEEE conference

## 💡 Future Ideas (Backlog)

- Time series analysis (multi-year)
- Machine learning predictions
- Policy scenario modeling
- Public-facing web tool

---

## 📊 Progress Tracking

Use GitHub Issues for detailed task tracking:
[View All Issues](https://github.com/username/project/issues)
```

#### **Format: Epic-Based (For Complex Projects)**

```markdown
# Roadmap - Feature Epics

## 🎯 Epic 1: Data Cleaning Pipeline (✅ Complete)

**Goal:** Reproducible, documented data cleaning process

### Tasks
- [x] Load raw RECS data [#10]
- [x] Handle missing values [#11]
- [x] Remove outliers [#12]
- [x] Create derived variables [#13]
- [x] Document data dictionary [#14]
- [x] Write unit tests [#15]

**Outcome:** Clean dataset ready for analysis

---

## 🎯 Epic 2: Energy Burden Analysis (🚧 60% Complete)

**Goal:** Calculate and visualize energy burden metrics

### Tasks
- [x] Calculate household-level burdens [#20]
- [ ] Aggregate to census tract level [#21]
- [ ] Create burden categories (low/med/high) [#22]
- [ ] Statistical tests by demographics [#23]
- [ ] Visualizations (maps, charts) [#24]

**Acceptance Criteria:**
- [ ] Burden calculated for all households
- [ ] Results validated against DOE LEAD tool
- [ ] Publication-quality figures generated

**Blockers:**
- Need census tract boundaries (waiting on GIS data)

---

## 🎯 Epic 3: Policy Scenarios (📋 Not Started)

**Goal:** Model impact of policy interventions

### Tasks
- [ ] Implement scenario framework [#30]
- [ ] Model rate changes [#31]
- [ ] Model efficiency improvements [#32]
- [ ] Compare scenarios [#33]
- [ ] Write policy recommendations [#34]
```

### **GitHub Issues: Detailed Task Tracking**

Issues are like sticky notes for your code. Each issue represents one specific task.

#### **When to Create an Issue**

✅ **Create issues for:**
- Features to implement
- Bugs to fix
- Data to collect
- Analyses to run
- Papers to write
- Questions to answer

**Example issues for data science:**
```
Issue #1: Remove outliers from income variable
Issue #2: Create visualization of burden by state
Issue #3: Bug: Energy burden calculation fails for zero income
Issue #4: Update methodology documentation with new formula
Issue #5: Question: Should we use median or mean for aggregation?
```

#### **Creating Issues in VS Code**

**Method 1: From GitHub Extension**

1. Install "GitHub Pull Requests and Issues" extension
2. Click GitHub icon in sidebar
3. Click `+` next to "Issues"
4. Fill in form:

```markdown
Title: Calculate energy burden for all households

Description:
Implement energy burden calculation (cost / income * 100) 
for each household in cleaned dataset.

Tasks:
- [ ] Load cleaned data
- [ ] Calculate burden
- [ ] Handle edge cases (zero income)
- [ ] Add unit tests
- [ ] Document formula

Labels: analysis, priority-high
Assignee: @yourusername
```

5. Press `Ctrl+Enter` to create

**Method 2: From TODO Comments**

```python
# TODO: Add visualization of burden distribution by income quintile
# This should be a box plot showing median and IQR for each quintile
def visualize_burden_by_income(df):
    pass
```

Right-click the TODO → "Create Issue from TODO"  
Automatically creates issue with code context!

**Method 3: On GitHub Website**

1. Go to your repo on GitHub
2. Click "Issues" tab
3. Click "New Issue"
4. Fill in details

#### **Issue Best Practices**

**✅ Good Issue:**
```markdown
Title: Add energy burden calculation function

## Description
Create a reusable function to calculate household energy burden
as percentage of income.

## Background
Energy burden = (annual energy cost / household income) × 100
DOE considers >6% to be "energy burdened"

## Tasks
- [ ] Create calculate_burden() function in scripts/calculations.py
- [ ] Handle edge cases:
  - [ ] Zero or negative income
  - [ ] Missing values
  - [ ] Non-numeric inputs
- [ ] Add docstring with examples
- [ ] Write unit tests
- [ ] Update documentation

## Acceptance Criteria
- Function returns None for invalid inputs
- Function passes all test cases
- Documented in README

## Related
- Depends on: #10 (data cleaning)
- Blocks: #25 (burden visualization)

## Resources
- DOE LEAD methodology: https://example.com/lead
```

**❌ Bad Issue:**
```markdown
Title: Fix stuff

Description: The thing doesn't work

```

#### **Linking Issues to Roadmap**

In your `ROADMAP.md`:
```markdown
### Q1 2025 Tasks
- [x] Clean RECS data [#10](https://github.com/user/repo/issues/10)
- [ ] Calculate burdens [#20](https://github.com/user/repo/issues/20)
- [ ] Create visualizations [#24](https://github.com/user/repo/issues/24)
```

Clicking the issue number takes you to full details!

#### **Linking Commits to Issues**

When you commit code related to an issue:

```bash
git commit -m "Add energy burden calculation function

Implements calculation of household energy burden as
percentage of income. Handles edge cases for zero
income and missing values.

Closes #20"
```

The `Closes #20` automatically:
1. Links commit to issue
2. Closes issue when merged to main branch
3. Creates a paper trail

**Other keywords that work:**
- `Closes #20`
- `Fixes #20`
- `Resolves #20`
- `Related to #20` (links but doesn't close)

#### **Issue Labels for Organization**

Create consistent labels:

**Priority:**
- `priority-critical` 🔴
- `priority-high` 🟠
- `priority-medium` 🟡
- `priority-low` 🟢

**Type:**
- `type-feature` (new functionality)
- `type-bug` (something broken)
- `type-analysis` (data analysis task)
- `type-documentation` (docs)
- `type-question` (needs discussion)

**Status:**
- `status-blocked` (waiting on something)
- `status-in-progress` (actively working)
- `status-needs-review` (done, needs checking)

**Component:**
- `component-data` (data-related)
- `component-analysis` (statistical analysis)
- `component-visualization` (plots/figures)
- `component-paper` (manuscript writing)

**Example filtering:**
```markdown
Show me: High-priority analysis tasks that are not blocked
Filter: is:open label:priority-high label:type-analysis -label:status-blocked
```

### **Workflow: Roadmap → Issues → Code → Done**

#### **Step-by-Step Process**

**Monday Morning:**

1. **Review Roadmap**
   ```
   Open ROADMAP.md
   What's the priority for this week?
   → "Calculate energy burden metrics"
   ```

2. **Check Existing Issues**
   ```
   Open GitHub Issues in VS Code
   Any issues for this task? #20
   Read issue details, accept criteria
   ```

3. **Start Working**
   ```
   Assign issue to yourself
   Move to "In Progress" (if using project board)
   
   Create branch (optional):
   git checkout -b calculate-burden
   ```

4. **Write Code**
   ```python
   # scripts/calculations.py
   
   # Working on issue #20
   def calculate_energy_burden(cost, income):
       """Calculate energy burden percentage.
       
       Related to issue #20.
       """
       if income <= 0:
           return None
       return (cost / income) * 100
   ```

5. **Commit with Issue Reference**
   ```bash
   git add scripts/calculations.py
   git commit -m "Add energy burden calculation
   
   Implements calculation of household energy burden
   as percentage of income. Handles zero income edge case.
   
   Progress on #20"
   ```

6. **Push and Continue**
   ```bash
   git push
   
   # Issue #20 now shows your commit in its timeline!
   ```

7. **Mark Complete**
   ```bash
   # When fully done:
   git commit -m "Complete energy burden implementation
   
   - Added calculation function
   - Added unit tests
   - Updated documentation
   
   Closes #20"
   
   git push
   ```

8. **Update Roadmap**
   ```markdown
   # ROADMAP.md
   - [x] Calculate energy burden metrics [#20] ✅ Completed 2025-01-15
   ```

**Friday Afternoon:**

9. **Weekly Review**
   ```
   What did I accomplish? (Check closed issues)
   What's still in progress? (Check open issues)
   What's next week's priority? (Check roadmap)
   Any blockers to note? (Update roadmap)
   ```

### **VS Code Setup for Issues**

#### **GitHub Issues View**

Once you install "GitHub Pull Requests and Issues":

```
Sidebar → GitHub icon

You'll see:
├── 🔔 Notifications
├── 📋 Issues
│   ├── Assigned to Me (2)
│   ├── Created by Me (5)
│   ├── Mentioned Me (0)
│   └── All Issues (8)
└── 🔀 Pull Requests
```

Click any issue to see details in VS Code!

#### **Quick Issue Creation from Selection**

```
1. Select text in your code or notes
2. Right-click → "GitHub: Create Issue from Selection"
3. Selected text becomes issue body
4. Add title and labels
5. Create!
```

#### **View Issue in Code**

Hover over `#20` in any file → See issue preview
Click `#20` → Jump to issue details

### **Team Collaboration**

**For small teams (2-5 people):**

1. **Create shared roadmap** in main repo
2. **Assign issues** to team members
3. **Use labels** for coordination:
   ```
   @john is working on: label:assigned-john
   @sarah needs to review: label:needs-sarah-review
   ```
4. **Weekly sync:** Review roadmap together
5. **Comment on issues** to discuss approach

**Communication in issues:**
```markdown
Comment on issue #20:

"@sarah I'm implementing this using the DOE formula 
(cost / income * 100). Does that match your analysis? 
Should we cap outliers at 99th percentile?"

@sarah replies:
"Yes, that formula is correct. For outliers, let's 
cap at 50% burden - anything higher is likely data error."
```

### **GitHub Projects (Optional - Visual Board)**

For visual task management (like Trello):

1. Go to your repo → "Projects" tab
2. Create new project (Board view)
3. Add columns: To Do | In Progress | Done
4. Add issues as cards
5. Drag cards between columns

Can also do this in VS Code with "GitHub Project Manager" extension

### **Example: Real Research Workflow**

**Monday:** Planning
```markdown
ROADMAP says: "Q1 Goal - Complete income analysis"

Create issues:
#30: Load and clean income data
#31: Calculate income quintiles
#32: Energy burden by income group
#33: Statistical significance tests
#34: Visualizations for paper
```

**Tuesday-Thursday:** Execution
```python
# Working on #30
df = pd.read_csv('data/raw/acs_income.csv')
df_clean = clean_income_data(df)

# Commit
git commit -m "Clean income data, progress on #30"

# Working on #31
df['income_quintile'] = pd.qcut(df['income'], 5)

git commit -m "Add income quintile calculation, closes #31"
```

**Friday:** Review & Plan
```
Review closed issues: ✅ #30, #31 done
Still open: #32, #33, #34
Next week: Focus on #32 (analysis)

Update ROADMAP:
- [x] Load and clean income data [#30]
- [x] Calculate income quintiles [#31]
- [ ] Energy burden by income group [#32] - Starting next week
```

**Next Monday:** Context is saved!
```
Read issue #32:
"Calculate mean and median energy burden for each 
income quintile. Check for statistical differences 
between groups using ANOVA."

Oh right, that's what I need to do!
```

---

## 🎯 Quick Reference {#quick-reference}

### **Daily Workflow Checklist**

```
Morning:
□ Open VS Code
□ Check Python interpreter (bottom-left)
□ Activate venv (terminal should show (venv))
□ Pull latest changes (Sync button)
□ Check today's issues in GitHub panel
□ Let Copilot help you code!

During Work:
□ Commit after each logical change
□ Write descriptive commit messages
□ Reference issue numbers in commits
□ Use Copilot for boilerplate code
□ Comment your code (helps Copilot too!)

End of Day:
□ Commit any uncommitted work
□ Push to GitHub (backup!)
□ Update issue status if tasks completed
□ Make note of tomorrow's priorities
```

### **Keyboard Shortcuts Cheat Sheet**

| Action | Windows/Linux | Mac | Description |
|--------|---------------|-----|-------------|
| **File Navigation** |
| Open file | `Ctrl+P` | `Cmd+P` | Quick open any file |
| Command palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Run any command |
| File explorer | `Ctrl+Shift+E` | `Cmd+Shift+E` | Show/hide files |
| Search | `Ctrl+Shift+F` | `Cmd+Shift+F` | Search across files |
| **Editing** |
| Multi-cursor | `Ctrl+D` | `Cmd+D` | Select next occurrence |
| Line comment | `Ctrl+/` | `Cmd+/` | Toggle comment |
| Format document | `Shift+Alt+F` | `Shift+Opt+F` | Auto-format code |
| Run selection | `Shift+Enter` | `Shift+Enter` | Run in Python REPL |
| **Git** |
| Source control | `Ctrl+Shift+G` | `Cmd+Shift+G` | View Git panel |
| Commit | `Ctrl+Enter` | `Cmd+Enter` | (in commit message) |
| **Terminal** |
| Toggle terminal | `` Ctrl+` `` | `` Cmd+` `` | Show/hide terminal |
| New terminal | ``Ctrl+Shift+` `` | ``Cmd+Shift+` `` | Create new terminal |
| **Copilot** |
| Accept suggestion | `Tab` | `Tab` | Accept Copilot code |
| Next suggestion | `Alt+]` | `Opt+]` | Cycle suggestions |
| Open Chat | `Ctrl+I` | `Cmd+I` | Ask Copilot question |
| **Other** |
| Toggle sidebar | `Ctrl+B` | `Cmd+B` | Show/hide sidebar |
| Zen mode | `Ctrl+K Z` | `Cmd+K Z` | Distraction-free |

### **Git Commands Quick Reference**

```bash
# Setup
git init                          # Start tracking a folder
git clone <url>                   # Copy a repo from GitHub

# Daily workflow
git status                        # See what changed
git add .                         # Stage all changes
git add file.py                   # Stage specific file
git commit -m "message"           # Save changes
git push                          # Upload to GitHub
git pull                          # Download from GitHub

# Branches (advanced)
git branch feature-name           # Create branch
git checkout feature-name         # Switch to branch
git checkout -b feature-name      # Create and switch
git merge feature-name            # Merge branch

# Time travel
git log                           # See commit history
git checkout <commit-hash> file   # Restore old version
git reset --hard HEAD~1           # Undo last commit (careful!)

# Troubleshooting
git stash                         # Temporarily save changes
git stash pop                     # Restore stashed changes
```

### **Python Environment Commands**

```bash
# Create environment
python -m venv venv               # Create venv
python -m venv --system-site-packages venv  # Inherit system packages

# Activate
source venv/bin/activate          # Linux/Mac
venv\Scripts\activate             # Windows

# Check what's installed
pip list                          # Show all packages
pip show pandas                   # Details about one package

# Install packages
pip install pandas                # Install one
pip install -r requirements.txt   # Install from file
pip install pandas==1.5.0         # Specific version

# Save environment
pip freeze > requirements.txt     # Save current packages
pip freeze | grep pandas          # Check one package version

# Deactivate
deactivate                        # Exit venv
```

### **Useful VS Code Extensions**

**Essential:**
- Python (Microsoft) - Python support
- Pylance - Fast Python intellisense
- GitHub Pull Requests and Issues - GitHub integration
- GitHub Copilot - AI code completion

**Data Science:**
- Jupyter - Notebook support
- Python Environment Manager - Manage venvs
- Rainbow CSV - Colorize CSV files
- Data Wrangler - Visual data viewer

**Quality of Life:**
- GitLens - Enhanced Git features
- Path Intellisense - Autocomplete file paths
- Better Comments - Colored comments
- Error Lens - Inline error messages
- Markdown All in One - Better markdown editing

### **Copilot Prompts That Work Well**

```python
# Good prompts (Copilot understands these well):

# "Create a function to..."
# Create a function to remove outliers using IQR method

# "Load data from..."
# Load housing data from CSV and handle missing values

# "Calculate..."
# Calculate energy burden as percentage of income for each household

# "Create a visualization of..."
# Create a histogram of energy burden distribution with proper labels

# "Generate test data for..."
# Generate 100 rows of synthetic housing data for testing

# "Handle edge case where..."
# Handle edge case where income is zero or negative

# "Convert this to a function"
[Select code] → Copilot Chat → "/fix Convert to function"

# "Explain this code"
[Select code] → Copilot Chat → "/explain"
```

### **Common Pitfalls & Solutions**

| Problem | Solution |
|---------|----------|
| **"Module not found"** | Check Python interpreter (bottom-left), activate venv |
| **"Command not found: git"** | Install Git: `sudo apt install git` (Linux) or download for Windows/Mac |
| **Large files slow Git** | Add to `.gitignore`, don't commit data files |
| **"Your branch is behind"** | Pull before you push: Git panel → ... → Pull |
| **Lost uncommitted changes** | Use `git stash` before switching branches |
| **Merge conflicts** | VS Code shows conflicts inline, choose which version to keep |
| **Copilot not working** | Check status bar (bottom-right), sign in, check internet |
| **Jupyter kernel won't start** | Select correct Python interpreter in notebook |
| **VS Code slow** | Disable extensions you don't use, close unused files |

### **Getting Help**

**Within VS Code:**
- `F1` or `Ctrl+Shift+P` → Type what you want to do
- Hover over any code element → See documentation
- Right-click → Context menu with options
- Help menu → Welcome, Tutorials, Documentation

**Copilot:**
- `Ctrl+I` → Ask any coding question
- Select code → Copilot Chat → "/explain"
- Type comment → Let Copilot suggest code

**External Resources:**
- VS Code Docs: https://code.visualstudio.com/docs
- GitHub Docs: https://docs.github.com
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Python Docs: https://docs.python.org/3/

---

## 🎓 Practice Exercise

**Try This 30-Minute Exercise:**

1. **Setup (5 min)**
   - Create folder: `my_test_project`
   - Open in VS Code
   - Create venv: `python -m venv venv`
   - Activate venv
   - Install pandas: `pip install pandas`
   - Create `requirements.txt`: `pip freeze > requirements.txt`

2. **Write Code with Copilot (10 min)**
   - Create `analyze.py`
   - Write comment: `# Load iris dataset and calculate mean petal length by species`
   - Let Copilot suggest code
   - Accept with Tab
   - Run the code: `Shift+Enter`

3. **Version Control (5 min)**
   - Initialize Git: `git init`
   - Create `.gitignore` (add `venv/`)
   - Stage all: Source Control → Stage All
   - Commit: "Initial analysis script"
   - Create GitHub repo and push

4. **Create Issue (5 min)**
   - Install GitHub Issues extension
   - Create issue: "Add visualization of petal length"
   - Add TODO comment in code: `# TODO: Add box plot visualization`
   - Right-click TODO → Create Issue

5. **Roadmap (5 min)**
   - Create `ROADMAP.md`
   - Add Q1 goal: "Complete iris analysis"
   - Link to your issue: `- [ ] Add visualization [#1]`
   - Commit: "Add project roadmap"

**You now have:**
✅ Properly structured project  
✅ Virtual environment  
✅ Git version control  
✅ GitHub backup  
✅ Copilot-assisted coding  
✅ Issue tracking  
✅ Project roadmap  

This is the foundation for all future projects!

---

## 📚 Additional Resources

### **Official Documentation**
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Getting Started](https://docs.github.com/en/get-started)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Copilot Documentation](https://docs.github.com/en/copilot)

### **Video Tutorials**
- [VS Code for Data Science (YouTube)](https://www.youtube.com/results?search_query=vs+code+python+data+science)
- [Git & GitHub Crash Course](https://www.youtube.com/results?search_query=git+github+crash+course)

### **Cheat Sheets**
- [VS Code Keyboard Shortcuts PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [Git Cheat Sheet](https://education# VS Code Setup Guide for Data Scientists & Researchers

**Purpose:** Empower data scientists and researchers to work more efficiently with modern development tools  
**Audience:** Data cleaning, analysis, and visualization professionals  
**Duration:** 60-90 minute meeting

---

## 📋 Table of Contents

1. [Why VS Code for Data Science?](#why-vs-code)
2. [Managing Python Environments](#python-environments)
3. [GitHub Integration](#github-integration)
4. [GitHub Copilot for Data Work](#copilot-integration)
5. [Project Folder Structure](#folder-structure)
6. [Roadmaps & Task Tracking](#roadmaps-and-issues)
7. [Quick Reference](#quick-reference)

---

## 🎯 Why VS Code for Data Science? {#why-vs-code}

### **The Problem with Traditional Workflows**

**Traditional Setup:**
```
Jupyter Notebook (analysis) 
  → Manual file management
    → Email scripts back and forth
      → Version confusion ("final_v3_FINAL.py")
        → Lost work when laptop crashes
```

**The VS Code Way:**
```
VS Code (write + run + version control in one place)
  → Git (automatic version history)
    → GitHub (collaborate + backup)
      → Copilot (AI assistance)
        → Never lose work again
```

### **Key Benefits for Data Scientists**

| What You Do | Old Way | VS Code Way |
|-------------|---------|-------------|
| **Write Python scripts** | Jupyter + separate .py files | Integrated notebooks + scripts |
| **Test code** | Copy-paste between windows | Run inline with `Ctrl+Enter` |
| **Manage packages** | Terminal commands, forget what you installed | Integrated terminal, requirements.txt |
| **Share with team** | Email files, "Did you get my latest version?" | Push to GitHub, everyone syncs |
| **Find old versions** | "backup_folder_2024_oct_maybe?" | Git history, see every change |
| **Get help coding** | Google, Stack Overflow, wait | Copilot suggests code as you type |

### **Real-World Example**

**Scenario:** You're cleaning a housing dataset with 50 columns, need to remove outliers, create new features, and visualize results.

**Jupyter Notebook approach:**
- ❌ Runs cells out of order, hard to reproduce
- ❌ If you close it, you lose your workflow
- ❌ Hard to turn into a production script
- ❌ No version control unless you manually save copies

**VS Code approach:**
- ✅ Write a Python script that runs top-to-bottom (reproducible)
- ✅ Use Jupyter notebooks in VS Code when you want interactive exploration
- ✅ Git tracks every change automatically
- ✅ Easy to convert notebook → script → production pipeline
- ✅ Copilot suggests data cleaning patterns

---

## 🐍 Managing Python Environments {#python-environments}

### **Why Multiple Environments?**

**The Problem:**
```python
# Project A needs pandas 1.5
pip install pandas==1.5

# Project B needs pandas 2.0
pip install pandas==2.0  # This breaks Project A! 😱
```

**The Solution: Virtual Environments**
```
📁 Project A
   └── venv/ (pandas 1.5)
   
📁 Project B  
   └── venv/ (pandas 2.0)
```

Each project has its own isolated Python environment.

### **Setting Up Environments in VS Code**

#### **Step 1: Create a Virtual Environment**

```bash
# Open VS Code terminal (Ctrl + `)
cd /path/to/your/project

# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# You should see (venv) in your terminal now
```

#### **Step 2: Tell VS Code to Use It**

1. Press `Ctrl+Shift+P` (Command Palette)
2. Type: `Python: Select Interpreter`
3. Choose the one with `./venv/bin/python`
4. VS Code will now use this environment automatically!

#### **Step 3: Install Your Packages**

```bash
# With venv activated:
pip install pandas numpy matplotlib seaborn scikit-learn

# Save your requirements so others can replicate:
pip freeze > requirements.txt
```

#### **Step 4: Share with Your Team**

When a colleague clones your project:
```bash
# They just run:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Now they have the exact same setup as you!
```

### **VS Code Environment Features**

**Status Bar Shows Active Environment:**
```
Bottom-left corner: Python 3.11.5 ('venv')
Click it to switch environments!
```

**Auto-Activation:**
- When you open a terminal, VS Code activates the venv automatically
- When you run Python files, it uses the selected environment
- When using Jupyter notebooks, kernel connects to your venv

**Environment Indicator in Files:**
```python
# Top-right corner shows: venv (Python 3.11.5)
import pandas as pd  # This imports from your venv, not system Python
```

### **Best Practices**

✅ **DO:**
- Create a new venv for each project
- Use descriptive names: `venv`, `env`, or `.venv`
- Add `venv/` to `.gitignore` (environments are big, don't commit them)
- Use `requirements.txt` to document dependencies
- Update requirements regularly: `pip freeze > requirements.txt`

❌ **DON'T:**
- Install packages globally (always activate venv first)
- Commit the `venv/` folder to Git (waste of space)
- Forget which environment you're using (check status bar!)
- Mix conda and venv (pick one and stick with it)

### **Troubleshooting**

**"Module not found" error:**
```python
ImportError: No module named 'pandas'
```
**Solution:** Check your Python interpreter (bottom-left) - is it using your venv?

**"Permission denied" when installing:**
```bash
# Don't use sudo! Just activate venv:
source venv/bin/activate
pip install pandas  # Now it works
```

**VS Code not finding venv:**
```bash
# Make sure it's in your project root:
your_project/
├── venv/
├── data/
└── scripts/
```

---

## 🔗 GitHub Integration {#github-integration}

### **Why GitHub for Data Scientists?**

**Common Data Science Workflow Problems:**

| Problem | GitHub Solution |
|---------|-----------------|
| "I broke my analysis script, can't undo" | Every version saved in Git history |
| "Which version did I send to the PI?" | Tagged releases, commit messages |
| "Collaborator overwrote my changes" | Merge conflicts detected automatically |
| "Lost a week of work when laptop died" | Everything backed up on GitHub |
| "Can't remember what this script does" | Commit messages document your thought process |

### **Installing GitHub Extension**

1. **Install Extension:**
   - Press `Ctrl+Shift+X` (Extensions)
   - Search: "GitHub Pull Requests and Issues"
   - Install the official GitHub extension

2. **Sign In:**
   - Click GitHub icon in sidebar (or `Ctrl+Shift+G`)
   - Click "Sign in to GitHub"
   - Authorize VS Code in your browser
   - Done! ✅

### **Git Basics in VS Code**

#### **The Three-Step Process**

Every change you make goes through three stages:

```
Working Directory  →  Staging Area  →  Repository  →  GitHub
(your files)          (ready to save)   (saved)       (backed up)
     │                     │                │              │
     │                     │                │              │
  [Edit]  ────────────→ [Stage] ──────→ [Commit] ────→ [Push]
                         (git add)      (git commit)  (git push)
```

#### **Visual Workflow in VS Code**

**1. Make Changes:**
```python
# You edit: clean_data.py
df = pd.read_csv('housing.csv')
df = df.dropna()  # Added this line
```

**2. See Changes:**
- Click Source Control icon (left sidebar, 3rd from top)
- You'll see `clean_data.py` with an "M" (Modified)
- Click the file to see diff (red = removed, green = added)

**3. Stage Changes:**
- Click `+` next to the file (or click "Stage All Changes")
- File moves to "Staged Changes" section
- This says: "I want to save these changes"

**4. Commit (Save):**
- Type a commit message in the text box at top:
  ```
  Add data cleaning step to remove missing values
  ```
- Click checkmark (✓) or press `Ctrl+Enter`
- Changes are now saved to your local Git history!

**5. Push (Backup to GitHub):**
- Click `...` menu → Push
- Or click ↑ arrow in status bar
- Your changes are now on GitHub! 🎉

### **Reading the Diff View**

```python
# Red (removed):
- df = pd.read_csv('housing.csv')  # Old version

# Green (added):
+ df = pd.read_csv('housing.csv')
+ df = df.dropna()  # New version with cleaning step
```

### **Commit Message Best Practices**

**❌ Bad Messages:**
```
"Updated file"
"Fix"
"Changes"
"asdfasdf"
```

**✅ Good Messages:**
```
"Remove outliers from housing price column"
"Add visualization for income distribution"
"Fix bug in date parsing for RECS data"
"Update README with installation instructions"
```

**Format:**
```
Short summary (50 chars or less)

Optional longer explanation:
- What changed
- Why you changed it
- Any important notes
```

### **Common Workflows**

#### **Scenario 1: Starting a New Project**

```bash
# In VS Code terminal:
cd /path/to/your/project
git init
git add .
git commit -m "Initial commit with data cleaning scripts"

# Create repo on GitHub (github.com/new)
git remote add origin https://github.com/yourusername/project.git
git push -u origin main
```

Or use VS Code:
1. `Ctrl+Shift+P` → "Publish to GitHub"
2. Choose public/private
3. Done!

#### **Scenario 2: Daily Work**

```
Morning:
1. Click ↓ (Pull) to get teammate's changes
2. Make your edits
3. Stage → Commit → Push

Afternoon:
4. More edits
5. Stage → Commit → Push

Evening:
6. Pull again before going home
```

#### **Scenario 3: "Oh no, I broke everything!"**

**Going back in time:**
1. Click Source Control icon
2. Click clock icon (View History)
3. Right-click a previous commit
4. "Restore File" or "Revert Commit"
5. Your code is back to that version! 🎉

### **GitHub Integration Features**

#### **View File History**

```
Right-click any file → "Open Timeline"

You can see:
- Every change made to this file
- Who made each change
- When it was changed
- Click to view that version
```

#### **Blame (Who wrote this code?)**

```
Right-click in any file → "Git: View Line History"

Shows:
- Who wrote each line
- When they wrote it
- The commit message explaining why
```

Useful for: "Why did we remove outliers this way?" → Check the commit message!

#### **Compare Versions**

```
Timeline → Right-click any version → "Compare with Working File"

See exactly what changed between then and now
```

### **Collaboration Features**

#### **Pull Requests (Advanced)**

When you want to suggest changes to a project:
1. Create a branch: `git checkout -b my-analysis`
2. Make changes
3. Push: `git push origin my-analysis`
4. Go to GitHub → Create Pull Request
5. Team reviews and discusses your changes
6. Merge when approved

#### **Issues (Task Tracking)**

Create issues directly in VS Code:
1. Click GitHub icon (sidebar)
2. Click `+` next to "Issues"
3. Fill in title and description
4. Assign to yourself
5. Track in VS Code as you work

### **Best Practices**

✅ **DO:**
- Commit often (every logical change)
- Write descriptive commit messages
- Pull before you start working (get latest changes)
- Push at end of day (backup your work)
- Use branches for experiments

❌ **DON'T:**
- Commit large data files (use .gitignore)
- Commit sensitive data (passwords, API keys)
- Make huge commits with 50 changes
- Work for days without committing
- Force push (you'll overwrite teammates' work)

### **.gitignore for Data Science**

Create a `.gitignore` file in your project root:

```gitignore
# Python
venv/
env/
__pycache__/
*.pyc
.ipynb_checkpoints/

# Data files (don't commit data to Git!)
*.csv
*.xlsx
*.parquet
*.hdf5
data/raw/
data/processed/

# Output files
*.png
*.pdf
plots/
results/

# Sensitive
.env
config/secrets.json
*.key

# OS
.DS_Store
Thumbs.db
```

**Important:** Git is for code, not data. Store data elsewhere (S3, shared drive, etc.)

### **Common Git Issues**

**"Merge conflict":**
```
Both you and teammate edited the same line.
VS Code shows:
<<<<<<< HEAD
your version
=======
their version
>>>>>>> 

Choose which to keep, delete the conflict markers, commit.
```

**"Detached HEAD":**
```
You're looking at an old commit.
To get back: git checkout main
```

**"Fatal: not a git repository":**
```
You're not in a Git project folder.
Run: git init
```

---

## 🤖 GitHub Copilot for Data Work {#copilot-integration}

### **What is Copilot?**

**Think of it as:**
- Pair programming with an AI that knows millions of code patterns
- Autocomplete on steroids
- A coding assistant that suggests entire functions

**What it's NOT:**
- Magic that writes perfect code every time
- A replacement for understanding your data
- Always correct (you still need to review!)

### **Why Copilot for Data Science?**

**Traditional Workflow:**
```
1. Remember pandas syntax → Google it → Find Stack Overflow → Copy-paste → Modify
2. Write boilerplate data cleaning code for the 100th time
3. Forget matplotlib parameters → Check documentation → Trial and error
```

**With Copilot:**
```
1. Start typing what you want → Copilot suggests it → Accept → Done
2. Write a comment describing what you need → Copilot writes the code
3. Type "plt.figure" → Copilot completes with sensible defaults
```

### **Installing Copilot**

**Prerequisites:**
- GitHub account (free or paid)
- VS Code

**Installation:**
1. Press `Ctrl+Shift+X` (Extensions)
2. Search: "GitHub Copilot"
3. Install
4. Sign in with GitHub when prompted
5. You should see Copilot icon in status bar (bottom-right)

**Cost:**
- Free for students and open-source maintainers
- $10/month for individuals
- $19/month for businesses
- Free trial available

### **How to Use Copilot**

#### **1. Inline Suggestions (Ghost Text)**

As you type, Copilot suggests completions in gray text:

```python
# You type:
import pandas as pd
df = pd.read_csv('housing.csv')
df_clean = df.dropna

# Copilot suggests (in gray):
df_clean = df.dropna()  # Press Tab to accept
```

**Accept:** `Tab`  
**Reject:** Keep typing or `Esc`  
**Next suggestion:** `Alt+]`  
**Previous suggestion:** `Alt+[`

#### **2. Comment-Driven Development**

Write a comment describing what you want:

```python
# Load housing data and remove rows where price is missing or negative
```

Press `Enter`, and Copilot suggests:

```python
# Load housing data and remove rows where price is missing or negative
df = pd.read_csv('housing_data.csv')
df = df[df['price'].notna()]
df = df[df['price'] > 0]
```

Press `Tab` to accept!

#### **3. Function Generation**

Start a function signature:

```python
def calculate_affordability_burden(energy_cost, income):
```

Copilot suggests the body:

```python
def calculate_affordability_burden(energy_cost, income):
    """Calculate energy burden as percentage of income."""
    if income == 0:
        return None
    return (energy_cost / income) * 100
```

#### **4. Copilot Chat (Ask Questions)**

Press `Ctrl+I` to open Copilot Chat inline:

**Example conversations:**

```
You: "How do I remove outliers using IQR method?"

Copilot: 
```python
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_clean = df[(df['column'] >= lower_bound) & (df['column'] <= upper_bound)]
```
```

```
You: "Explain this code"
[Select some complex code]

Copilot: "This code performs a left join between two dataframes, 
merging on the 'id' column. It keeps all rows from the left dataframe 
and adds matching columns from the right dataframe..."
```

```
You: "Fix this bug"
[Select broken code]

Copilot: [Suggests corrected version with explanation]
```

### **Real Data Science Examples**

#### **Example 1: Data Cleaning Pipeline**

**You write:**
```python
# Create a function to clean housing data:
# - Remove rows with missing values in critical columns
# - Convert year_built to building_age
# - Cap outliers in price at 99th percentile
# - Create price_per_sqft column
```

**Copilot suggests:**
```python
def clean_housing_data(df):
    # Remove rows with missing critical values
    critical_cols = ['price', 'sqft', 'year_built', 'location']
    df = df.dropna(subset=critical_cols)
    
    # Convert year_built to age
    current_year = pd.Timestamp.now().year
    df['building_age'] = current_year - df['year_built']
    
    # Cap outliers
    cap_value = df['price'].quantile(0.99)
    df['price'] = df['price'].clip(upper=cap_value)
    
    # Create price per sqft
    df['price_per_sqft'] = df['price'] / df['sqft']
    
    return df
```

#### **Example 2: Visualization**

**You write:**
```python
# Create a subplot with 2 charts:
# 1. Histogram of energy burden distribution
# 2. Scatter plot of income vs energy cost, colored by burden category
```

**Copilot suggests:**
```python
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Histogram
axes[0].hist(df['energy_burden'], bins=50, color='skyblue', edgecolor='black')
axes[0].set_xlabel('Energy Burden (%)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Distribution of Energy Burden')

# Scatter plot
scatter = axes[1].scatter(df['income'], df['energy_cost'], 
                          c=df['burden_category'], cmap='RdYlGn_r', alpha=0.6)
axes[1].set_xlabel('Household Income ($)')
axes[1].set_ylabel('Energy Cost ($)')
axes[1].set_title('Income vs Energy Cost')
plt.colorbar(scatter, ax=axes[1], label='Burden Category')

plt.tight_layout()
plt.show()
```

#### **Example 3: Statistical Analysis**

**You write:**
```python
# Calculate correlation between housing characteristics and energy burden
# Show top 10 most correlated features
```

**Copilot suggests:**
```python
# Calculate correlations with energy burden
correlations = df.corr()['energy_burden'].sort_values(ascending=False)

# Remove self-correlation and show top 10
top_correlations = correlations[correlations.index != 'energy_burden'].head(10)

print("Top 10 Features Correlated with Energy Burden:")
print(top_correlations)

# Visualize
top_correlations.plot(kind='barh', figsize=(10, 6))
plt.xlabel('Correlation Coefficient')
plt.title('Features Most Correlated with Energy Burden')
plt.tight_layout()
plt.show()
```

### **Copilot Best Practices**

✅ **DO:**
- **Write detailed comments** - More context = better suggestions
- **Review suggestions carefully** - Copilot isn't always right
- **Use descriptive variable names** - Helps Copilot understand context
- **Break complex tasks into steps** - Comment each step
- **Use Copilot Chat for explanations** - Great learning tool
- **Accept partial suggestions** - Tab accepts, then modify

❌ **DON'T:**
- **Blindly accept everything** - Always review code
- **Use Copilot for sensitive operations** - Review security-critical code carefully
- **Expect perfect code** - It's a tool, not a replacement for thinking
- **Forget to test** - Copilot suggestions still need testing
- **Copy code you don't understand** - Use Chat to ask for explanation

### **Copilot Keyboard Shortcuts**

| Action | Shortcut |
|--------|----------|
| Accept suggestion | `Tab` |
| Reject suggestion | `Esc` |
| Next suggestion | `Alt + ]` |
| Previous suggestion | `Alt + [` |
| Open Copilot Chat | `Ctrl + I` |
| Open Copilot panel | `Ctrl + Shift + I` |
| Trigger suggestion | `Alt + \` |

### **Copilot Chat Commands**

```
/explain - Explain selected code
/fix - Suggest fixes for problems
/tests - Generate unit tests
/help - Show all commands
```

**Example:**
```
Select code → Ctrl+I → Type "/explain" → Enter
Copilot explains what the code does line by line
```

### **When Copilot Shines**

🌟 **Great for:**
- Boilerplate data cleaning code
- Common pandas operations
- Matplotlib/seaborn styling
- Regex patterns
- Error handling
- Documentation strings
- Unit tests
- SQL queries
- File I/O operations

⚠️ **Use caution for:**
- Domain-specific calculations (verify formulas)
- Statistical methods (check assumptions)
- Production code (needs thorough review)
- Security-sensitive operations
- Custom business logic

### **Troubleshooting**

**Copilot not showing suggestions:**
1. Check status bar (bottom-right) - Is Copilot enabled?
2. Try `Alt + \` to manually trigger
3. Check your internet connection
4. Restart VS Code

**Suggestions are wrong:**
1. Add more context in comments
2. Use descriptive variable names
3. Try asking Copilot Chat for explanation
4. Reject (`Esc`) and write manually

**Copilot suggests code from wrong language:**
1. Check file extension (.py for Python)
2. Set language mode: Click bottom-right → Select "Python"

---

## 📁 Project Folder Structure {#folder-structure}

### **Why Structure Matters**

**Bad structure:**
```
my_project/
├── analysis.py
├── analysis_v2.py
├── analysis_FINAL.py
├── analysis_FINAL_REALLY.py
├── data.csv
├── data_clean.csv
├── plot1.png
├── plot2.png
└── some_script.py
```
😱 Which file is current? Where's the original data? What does `some_script.py` do?

**Good structure:**
```
energy_affordability/
├── data/
│   ├── raw/                 # Never modify these!
│   ├── processed/           # Cleaned data
│   └── results/             # Analysis outputs
├── notebooks/               # Jupyter notebooks for exploration
├── scripts/                 # Python scripts for production
│   ├── 01_clean_data.py
│   ├── 02_feature_engineering.py
│   └── 03_analyze.py
├── reports/                 # Generated reports, figures
│   ├── figures/
│   └── paper_draft.pdf
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── .gitignore
├── README.md
├── requirements.txt
└── environment.yml
```
✅ Clear organization! Easy to find everything!

### **Recommended Structure for Data Science Projects**

#### **Template 1: Basic Analysis Project**

```
project_name/
│
├── data/
│   ├── raw/                      # Original, immutable data
│   │   ├── recs_2020.csv
│   │   └── acs_data.csv
│   ├── interim/                  # Intermediate, transformed data
│   │   └── recs_cleaned.csv
│   └── processed/                # Final datasets for modeling
│       └── model_ready.csv
│
├── notebooks/                    # Jupyter notebooks
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_visualizations.ipynb
│
├── scripts/                      # Python scripts
│   ├── __init__.py
│   ├── data_processing.py       # Data loading and cleaning
│   ├── features.py              # Feature engineering
│   ├── visualization.py         # Plotting functions
│   └── utils.py                 # Helper functions
│
├── reports/                      # Generated analysis outputs
│   ├── figures/                 # Saved plots
│   │   ├── income_distribution.png
│   │   └── burden_by_state.png
│   └── final_report.html        # Generated from notebook
│
├── tests/                        # Unit tests (optional but good!)
│   ├── test_data_processing.py
│   └── test_features.py
│
├── .gitignore                    # Files to ignore in Git
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── config.py                     # Configuration settings
```

#### **Template 2: Research Project**

```
research_project/
│
├── data/
│   ├── raw/                      # Original data (never modify!)
│   ├── processed/                # Cleaned, analysis-ready
│   └── README.md                 # Data dictionary
│
├── analysis/
│   ├── exploratory/              # Initial explorations
│   ├── main/                     # Core analysis notebooks
│   └── sensitivity/              # Robustness checks
│
├── paper/                        # Manuscript
│   ├── manuscript.tex
│   ├── figures/                  # Paper figures
│   └── tables/                   # Paper tables
│
├── presentations/
│   ├── conference_2024.pptx
│   └── lab_meeting.pdf
│
├── src/                          # Source code
│   ├── data/                     # Data processing
│   ├── models/                   # Statistical models
│   ├── visualization/            # Plotting
│   └── utils/                    # Helper functions
│
├── results/                      # Model outputs
│   ├── model_outputs/
│   └── statistical_tests/
│
├── docs/                         # Documentation
│   ├── methodology.md
│   └── data_sources.md
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

#### **Template 3: Dashboard/App Project**

```
dashboard_project/
│
├── backend/                      # API server
│   ├── app.py                   # Flask/FastAPI app
│   ├── data_processing.py       # Data processing
│   ├── config.py                # Configuration
│   └── requirements.txt         # Backend dependencies
│
├── frontend/                     # Web interface
│   ├── src/
│   │   ├── components/          # UI components
│   │   ├── pages/               # Page routes
│   │   └── utils/               # Helper functions
│   ├── public/                  # Static assets
│   └── package.json             # Frontend dependencies
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
│   ├── backend/
│   └── frontend/
│
├── docs/                         # Documentation
│   ├── api_reference.md
│   └── user_guide.md
│
├── .gitignore
├── README.md
├── docker-compose.yml           # For deployment
└── ROADMAP.md                   # Project roadmap
```

### **Best Practices for Each Folder**

#### **📂 data/**

✅ **DO:**
- Keep `raw/` data completely unchanged (treat as read-only)
- Add `data/README.md` explaining each dataset
- Document data sources and collection dates
- Use descriptive filenames: `recs_2020_public_use.csv`

❌ **DON'T:**
- Commit large data files to Git (add `data/` to `.gitignore`)
- Mix raw and processed data
- Store data in repository root

**Example data/README.md:**
```markdown
# Data Dictionary

## raw/recs_2020.csv
- **Source:** U.S. EIA Residential Energy Consumption Survey
- **Downloaded:** 2024-03-15
- **URL:** https://www.eia.gov/consumption/residential/data/2020/
- **Rows:** 18,496 households
- **Columns:** 784 variables

## processed/households_clean.csv
- **Created by:** scripts/01_clean_data.py
- **Date:** 2024-10-15
- **Description:** Cleaned RECS data with outliers removed
- **Rows:** 18,234 (262 outliers removed)
```

#### **📓 notebooks/**

✅ **DO:**
- Number notebooks in order: `01_`, `02_`, `03_`
- Use descriptive names: `02_income_distribution_analysis.ipynb`
- Add markdown cells explaining your thinking
- Clear outputs before committing (keeps Git clean)
- Use notebooks for exploration, scripts for production

❌ **DON'T:**
- Have 50 untitled notebooks
- Leave notebooks in random execution order
- Commit notebooks with massive outputs (slows Git)
- Use notebooks for code that will run in production

**VS Code Settings for Notebooks:**
```json
// settings.json
{
  "notebook.output.textLineLimit": 30,
  "notebook.cellToolbarVisibility": "visible",
  "jupyter.askForKernelRestart": false
}
```

#### **📜 scripts/**

✅ **DO:**
- Use clear, descriptive names: `calculate_energy_burden.py`
- Add docstrings to all functions
- Number scripts if they run in sequence
- Make scripts runnable: `if __name__ == "__main__":`
- Import from other scripts: `from data_processing import clean_data`

❌ **DON'T:**
- Have scripts with unclear names: `script1.py`, `test.py`
- Duplicate code across scripts (make utility functions)
- Hardcode file paths (use config or arguments)

**Example script structure:**
```python
"""
Clean and prepare RECS housing data for analysis.

This script loads raw RECS data, removes outliers, creates derived
variables, and exports analysis-ready dataset.

Usage:
    python scripts/01_clean_data.py
"""

import pandas as pd
from pathlib import Path

# Configuration
DATA_DIR = Path(__file__).parent.parent / 'data'
RAW_DATA = DATA_DIR / 'raw' / 'recs_2020.csv'
OUTPUT_DATA = DATA_DIR / 'processed' / 'recs_clean.csv'

def load_raw_data(filepath):
    """Load raw RECS data with proper dtypes."""
    return pd.read_csv(filepath)

def remove_outliers(df, column, n_std=3):
    """Remove outliers beyond n standard deviations."""
    mean = df[column].mean()
    std = df[column].std()
    return df[
        (df[column] >= mean - n_std * std) & 
        (df[column] <= mean + n_std * std)
    ]

def main():
    """Main execution function."""
    print("Loading data...")
    df = load_raw_data(RAW_DATA)
    
    print(f"Loaded {len(df)} rows")
    
    print("Removing outliers...")
    df = remove_outliers(df, 'energy_cost')
    
    print(f"After cleaning: {len(df)} rows")
    
    print(f"Saving to {OUTPUT_DATA}")
    df.to_csv(OUTPUT_DATA, index=False)
    
    print("Done!")

if __name__ == "__main__":
    main()
```

#### **📊 reports/**

✅ **DO:**
- Save high-resolution figures: `plt.savefig('figure.png', dpi=300)`
- Use descriptive names: `burden_by_income_quintile.png`
- Keep figures separate from other outputs
- Generate reports programmatically (Jupyter → HTML/PDF)

#### **🧪 tests/**

✅ **DO:**
- Name test files: `test_*.py`
- Test critical functions (data cleaning, calculations)
- Run tests before committing: `pytest tests/`

**Example test:**
```python
# tests/test_calculations.py
import pytest
from scripts.features import calculate_energy_burden

def test_energy_burden_calculation():
    """Test energy burden percentage calculation."""
    cost = 2400  # $2400/year
    income = 40000  # $40k/year
    
    result = calculate_energy_burden(cost, income)
    
    assert result == 6.0  # Should be 6%

def test_energy_burden_zero_income():
    """Test handling of zero income edge case."""
    result = calculate_energy_burden(2400, 0)
    
    assert result is None  # Should return None, not error
```

#### **📖 docs/**

✅ **DO:**
- Create `README.md` in project root (first thing people see)
- Add methodology documentation
- Document data sources
- Include setup instructions

**Example README.md:**
```markdown
# Energy Affordability Analysis

Analysis of residential energy cost burdens across U.S. households.

## Setup

```bash
# Create environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Data Sources

- RECS 2020: Residential energy consumption
- ACS 5-Year: Household demographics

## Project Structure

- `data/`: Raw and processed datasets
- `notebooks/`: Exploratory analysis
- `scripts/`: Production code
- `reports/`: Generated figures and reports

## Usage

Run analysis pipeline:
```bash
python scripts/01_clean_data.py
python scripts/02_analysis.py
```

## Contact

Questions? Email: your.email@university.edu
```

### **VS Code Features for Project Organization**

#### **1. Workspace Settings**

Save project-specific settings:

```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/.ipynb_checkpoints": true
  },
  "python.analysis.extraPaths": [
    "${workspaceFolder}/scripts"
  ]
}
```

This allows imports like:
```python
from data_processing import clean_data  # Works!
```

#### **2. Multi-Root Workspaces**

Working on frontend + backend? Add both to one workspace:

```
File → Add Folder to Workspace
Save as: energy_affordability.code-workspace
```

Now you see both in one window!

#### **3. File Explorer Organization**

Right-click folders → Create:
- `New File`
- `New Folder`
- Drag and drop to reorganize

#### **4. Quick File Navigation**

- `Ctrl+P` → Type filename → Jump directly
- `Ctrl+Shift+E` → File explorer
- `Ctrl+B` → Toggle sidebar

### **Common Mistakes to Avoid**

❌ **Flat structure (everything in root):**
```
project/
├── analysis1.py
├── analysis2.py
├── data.csv
├── data_clean.csv
├── plot.png
└── test.py
```

❌ **Too many nested levels:**
```
project/
└── src/
    └── python/
        └── scripts/
            └── data/
                └── processing/
                    └── clean.py  # Too deep!
```

❌ **Unclear naming:**
```
project/
├── stuff/
├── old/
├── temp/
└── misc/
```

### **When to Refactor Structure**

🚨 **Warning signs:**
- Can't find files quickly
- Same code in multiple places
- Notebooks named "Untitled1", "Untitled2"...
- No one else can run your code
- "Where did I put that analysis?"

✅ **Solution:** Take 30 minutes to reorganize using templates above

---

## 🗺️ Roadmaps & Task Tracking {#roadmaps-and-issues}

### **Why Track Tasks?**

**The Problem:**
```
❌ "What was I working on again?"
❌ "Did I finish that analysis?"
❌ "What should I do next?"
❌ Constantly switching between 10 priorities
❌ Forgetting to document decisions
```

**The Solution:**
```
✅ Clear roadmap of priorities
✅ Track progress visually
✅ Remember context for each task
✅ Know what's blocking what
✅ Document decisions in issues
```

### **Two-Level System**

**Level 1: ROADMAP.md** (Strategic, high-level)
- Where are we going?
- What are the big milestones?
- What's the priority?

**Level 2: GitHub Issues** (Tactical, detailed)
- What specific tasks need doing?
- Who's working on what?
- What's the status of each task?

### **Creating a Roadmap**

#### **Location:**
```
project/
├── ROADMAP.md              # Overall project roadmap
├── backend/
│   └── ROADMAP.md          # Backend-specific
└── frontend/
    └── ROADMAP.md          # Frontend-specific
```

#### **Format: Quarterly Timeline**

```markdown
# Energy Affordability Analysis - Roadmap

**Last Updated:** 2025-10-29

---

## 🎯 Q4 2024 (✅ Complete)

- [x] Collect RECS 2020 data
- [x] Initial exploratory analysis
- [x] Identify research questions

## 🚀 Q1 2025 (🚧 In Progress - 60%)

**Goal:** Complete affordability burden analysis

### High Priority
- [x] Clean RECS data and remove outliers [#1]
- [ ] Calculate energy burden metrics [#2] 
- [ ] Create state-level visualizations [#3]
- [ ] Draft methodology section [#4]

### Medium Priority
- [ ] Compare to previous studies [#5]
- [ ] Sensitivity analysis [#6]

### Low Priority
- [ ] Interactive dashboard prototype

**Blockers:**
- Waiting for updated ACS data release (Feb 2025)

## 📋 Q2 2025 (Planned)

**Goal:** Finalize paper and submit

- [ ] Complete all analyses
- [ ] Write results section
- [ ] Create publication-quality figures
- [ ] Submit to Energy Policy journal
- [ ] Present at ACEEE conference

## 💡 Future Ideas (Backlog)

- Time series analysis (multi-year)
- Machine learning predictions
- Policy scenario modeling
- Public-facing web tool

---

## 📊 Progress Tracking

Use GitHub Issues for detailed task tracking:
[View All Issues](https://github.com/username/project/issues)
```

#### **Format: Epic-Based (For Complex Projects)**

```markdown
# Roadmap - Feature Epics

## 🎯 Epic 1: Data Cleaning Pipeline (✅ Complete)

**Goal:** Reproducible, documented data cleaning process

### Tasks
- [x] Load raw RECS data [#10]
- [x] Handle missing values [#11]
- [x] Remove outliers [#12]
- [x] Create derived variables [#13]
- [x] Document data dictionary [#14]
- [x] Write unit tests [#15]

**Outcome:** Clean dataset ready for analysis

---

## 🎯 Epic 2: Energy Burden Analysis (🚧 60% Complete)

**Goal:** Calculate and visualize energy burden metrics

### Tasks
- [x] Calculate household-level burdens [#20]
- [ ] Aggregate to census tract level [#21]
- [ ] Create burden categories (low/med/high) [#22]
- [ ] Statistical tests by demographics [#23]
- [ ] Visualizations (maps, charts) [#24]

**Acceptance Criteria:**
- [ ] Burden calculated for all households
- [ ] Results validated against DOE LEAD tool
- [ ] Publication-quality figures generated

**Blockers:**
- Need census tract boundaries (waiting on GIS data)

---

## 🎯 Epic 3: Policy Scenarios (📋 Not Started)

**Goal:** Model impact of policy interventions

### Tasks
- [ ] Implement scenario framework [#30]
- [ ] Model rate changes [#31]
- [ ] Model efficiency improvements [#32]
- [ ] Compare scenarios [#33]
- [ ] Write policy recommendations [#34]
```

### **GitHub Issues: Detailed Task Tracking**

Issues are like sticky notes for your code. Each issue represents one specific task.

#### **When to Create an Issue**

✅ **Create issues for:**
- Features to implement
- Bugs to fix
- Data to collect
- Analyses to run
- Papers to write
- Questions to answer

**Example issues for data science:**
```
Issue #1: Remove outliers from income variable
Issue #2: Create visualization of burden by state
Issue #3: Bug: Energy burden calculation fails for zero income
Issue #4: Update methodology documentation with new formula
Issue #5: Question: Should we use median or mean for aggregation?
```

#### **Creating Issues in VS Code**

**Method 1: From GitHub Extension**

1. Install "GitHub Pull Requests and Issues" extension
2. Click GitHub icon in sidebar
3. Click `+` next to "Issues"
4. Fill in form:

```markdown
Title: Calculate energy burden for all households

Description:
Implement energy burden calculation (cost / income * 100) 
for each household in cleaned dataset.

Tasks:
- [ ] Load cleaned data
- [ ] Calculate burden
- [ ] Handle edge cases (zero income)
- [ ] Add unit tests
- [ ] Document formula

Labels: analysis, priority-high
Assignee: @yourusername
```

5. Press `Ctrl+Enter` to create

**Method 2: From TODO Comments**

```python
# TODO: Add visualization of burden distribution by income quintile
# This should be a box plot showing median and IQR for each quintile
def visualize_burden_by_income(df):
    pass
```

Right-click the TODO → "Create Issue from TODO"  
Automatically creates issue with code context!

**Method 3: On GitHub Website**

1. Go to your repo on GitHub
2. Click "Issues" tab
3. Click "New Issue"
4. Fill in details

#### **Issue Best Practices**

**✅ Good Issue:**
```markdown
Title: Add energy burden calculation function

## Description
Create a reusable function to calculate household energy burden
as percentage of income.

## Background
Energy burden = (annual energy cost / household income) × 100
DOE considers >6% to be "energy burdened"

## Tasks
- [ ] Create calculate_burden() function in scripts/calculations.py
- [ ] Handle edge cases:
  - [ ] Zero or negative income
  - [ ] Missing values
  - [ ] Non-numeric inputs
- [ ] Add docstring with examples
- [ ] Write unit tests
- [ ] Update documentation

## Acceptance Criteria
- Function returns None for invalid inputs
- Function passes all test cases
- Documented in README

## Related
- Depends on: #10 (data cleaning)
- Blocks: #25 (burden visualization)

## Resources
- DOE LEAD methodology: https://example.com/lead
```

**❌ Bad Issue:**
```markdown
Title: Fix stuff

Description: The thing doesn't work

```

#### **Linking Issues to Roadmap**

In your `ROADMAP.md`:
```markdown
### Q1 2025 Tasks
- [x] Clean RECS data [#10](https://github.com/user/repo/issues/10)
- [ ] Calculate burdens [#20](https://github.com/user/repo/issues/20)
- [ ] Create visualizations [#24](https://github.com/user/repo/issues/24)
```

Clicking the issue number takes you to full details!

#### **Linking Commits to Issues**

When you commit code related to an issue:

```bash
git commit -m "Add energy burden calculation function

Implements calculation of household energy burden as
percentage of income. Handles edge cases for zero
income and missing values.

Closes #20"
```

The `Closes #20` automatically:
1. Links commit to issue
2. Closes issue when merged to main branch
3. Creates a paper trail

**Other keywords that work:**
- `Closes #20`
- `Fixes #20`
- `Resolves #20`
- `Related to #20` (links but doesn't close)

#### **Issue Labels for Organization**

Create consistent labels:

**Priority:**
- `priority-critical` 🔴
- `priority-high` 🟠
- `priority-medium` 🟡
- `priority-low` 🟢

**Type:**
- `type-feature` (new functionality)
- `type-bug` (something broken)
- `type-analysis` (data analysis task)
- `type-documentation` (docs)
- `type-question` (needs discussion)

**Status:**
- `status-blocked` (waiting on something)
- `status-in-progress` (actively working)
- `status-needs-review` (done, needs checking)

**Component:**
- `component-data` (data-related)
- `component-analysis` (statistical analysis)
- `component-visualization` (plots/figures)
- `component-paper` (manuscript writing)

**Example filtering:**
```markdown
Show me: High-priority analysis tasks that are not blocked
Filter: is:open label:priority-high label:type-analysis -label:status-blocked
```

### **Workflow: Roadmap → Issues → Code → Done**

#### **Step-by-Step Process**

**Monday Morning:**

1. **Review Roadmap**
   ```
   Open ROADMAP.md
   What's the priority for this week?
   → "Calculate energy burden metrics"
   ```

2. **Check Existing Issues**
   ```
   Open GitHub Issues in VS Code
   Any issues for this task? #20
   Read issue details, accept criteria
   ```

3. **Start Working**
   ```
   Assign issue to yourself
   Move to "In Progress" (if using project board)
   
   Create branch (optional):
   git checkout -b calculate-burden
   ```

4. **Write Code**
   ```python
   # scripts/calculations.py
   
   # Working on issue #20
   def calculate_energy_burden(cost, income):
       """Calculate energy burden percentage.
       
       Related to issue #20.
       """
       if income <= 0:
           return None
       return (cost / income) * 100
   ```

5. **Commit with Issue Reference**
   ```bash
   git add scripts/calculations.py
   git commit -m "Add energy burden calculation
   
   Implements calculation of household energy burden
   as percentage of income. Handles zero income edge case.
   
   Progress on #20"
   ```

6. **Push and Continue**
   ```bash
   git push
   
   # Issue #20 now shows your commit in its timeline!
   ```

7. **Mark Complete**
   ```bash
   # When fully done:
   git commit -m "Complete energy burden implementation
   
   - Added calculation function
   - Added unit tests
   - Updated documentation
   
   Closes #20"
   
   git push
   ```

8. **Update Roadmap**
   ```markdown
   # ROADMAP.md
   - [x] Calculate energy burden metrics [#20] ✅ Completed 2025-01-15
   ```

**Friday Afternoon:**

9. **Weekly Review**
   ```
   What did I accomplish? (Check closed issues)
   What's still in progress? (Check open issues)
   What's next week's priority? (Check roadmap)
   Any blockers to note? (Update roadmap)
   ```

### **VS Code Setup for Issues**

#### **GitHub Issues View**

Once you install "GitHub Pull Requests and Issues":

```
Sidebar → GitHub icon

You'll see:
├── 🔔 Notifications
├── 📋 Issues
│   ├── Assigned to Me (2)
│   ├── Created by Me (5)
│   ├── Mentioned Me (0)
│   └── All Issues (8)
└── 🔀 Pull Requests
```

Click any issue to see details in VS Code!

#### **Quick Issue Creation from Selection**

```
1. Select text in your code or notes
2. Right-click → "GitHub: Create Issue from Selection"
3. Selected text becomes issue body
4. Add title and labels
5. Create!
```

#### **View Issue in Code**

Hover over `#20` in any file → See issue preview
Click `#20` → Jump to issue details

### **Team Collaboration**

**For small teams (2-5 people):**

1. **Create shared roadmap** in main repo
2. **Assign issues** to team members
3. **Use labels** for coordination:
   ```
   @john is working on: label:assigned-john
   @sarah needs to review: label:needs-sarah-review
   ```
4. **Weekly sync:** Review roadmap together
5. **Comment on issues** to discuss approach

**Communication in issues:**
```markdown
Comment on issue #20:

"@sarah I'm implementing this using the DOE formula 
(cost / income * 100). Does that match your analysis? 
Should we cap outliers at 99th percentile?"

@sarah replies:
"Yes, that formula is correct. For outliers, let's 
cap at 50% burden - anything higher is likely data error."
```

### **GitHub Projects (Optional - Visual Board)**

For visual task management (like Trello):

1. Go to your repo → "Projects" tab
2. Create new project (Board view)
3. Add columns: To Do | In Progress | Done
4. Add issues as cards
5. Drag cards between columns

Can also do this in VS Code with "GitHub Project Manager" extension

### **Example: Real Research Workflow**

**Monday:** Planning
```markdown
ROADMAP says: "Q1 Goal - Complete income analysis"

Create issues:
#30: Load and clean income data
#31: Calculate income quintiles
#32: Energy burden by income group
#33: Statistical significance tests
#34: Visualizations for paper
```

**Tuesday-Thursday:** Execution
```python
# Working on #30
df = pd.read_csv('data/raw/acs_income.csv')
df_clean = clean_income_data(df)

# Commit
git commit -m "Clean income data, progress on #30"

# Working on #31
df['income_quintile'] = pd.qcut(df['income'], 5)

git commit -m "Add income quintile calculation, closes #31"
```

**Friday:** Review & Plan
```
Review closed issues: ✅ #30, #31 done
Still open: #32, #33, #34
Next week: Focus on #32 (analysis)

Update ROADMAP:
- [x] Load and clean income data [#30]
- [x] Calculate income quintiles [#31]
- [ ] Energy burden by income group [#32] - Starting next week
```

**Next Monday:** Context is saved!
```
Read issue #32:
"Calculate mean and median energy burden for each 
income quintile. Check for statistical differences 
between groups using ANOVA."

Oh right, that's what I need to do!
```

---

## 🎯 Quick Reference {#quick-reference}

### **Daily Workflow Checklist**

```
Morning:
□ Open VS Code
□ Check Python interpreter (bottom-left)
□ Activate venv (terminal should show (venv))
□ Pull latest changes (Sync button)
□ Check today's issues in GitHub panel
□ Let Copilot help you code!

During Work:
□ Commit after each logical change
□ Write descriptive commit messages
□ Reference issue numbers in commits
□ Use Copilot for boilerplate code
□ Comment your code (helps Copilot too!)

End of Day:
□ Commit any uncommitted work
□ Push to GitHub (backup!)
□ Update issue status if tasks completed
□ Make note of tomorrow's priorities
```

### **Keyboard Shortcuts Cheat Sheet**

| Action | Windows/Linux | Mac | Description |
|--------|---------------|-----|-------------|
| **File Navigation** |
| Open file | `Ctrl+P` | `Cmd+P` | Quick open any file |
| Command palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Run any command |
| File explorer | `Ctrl+Shift+E` | `Cmd+Shift+E` | Show/hide files |
| Search | `Ctrl+Shift+F` | `Cmd+Shift+F`…