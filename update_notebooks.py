import json
import os

def update_notebook(file_path, base_raw, required_files, csv_replacements):
    with open(file_path, 'r') as f:
        nb = json.load(f)

    # Prepare bootstrap cell
    bootstrap_source = [
        "# Environment bootstrap for Colab/local use\n",
        "# Fetches required data/image assets into expected paths.\n",
        "\n",
        "import os\n",
        "import sys\n",
        "import subprocess\n",
        "from pathlib import Path\n",
        "from urllib.request import urlretrieve\n",
        "\n",
        f"base_raw = \"{base_raw}\"\n",
        "required_files = {\n"
    ]
    for local, remote in required_files.items():
        bootstrap_source.append(f"    \"{local}\": f\"{{base_raw}}/{local}\",\n")
    
    bootstrap_source.extend([
        "}\n",
        "\n",
        "Path(\"data\").mkdir(exist_ok=True)\n",
        "Path(\"images\").mkdir(exist_ok=True)\n",
        "Path(\"figures\").mkdir(exist_ok=True)\n",
        "\n",
        "for local_path, remote_url in required_files.items():\n",
        "    path = Path(local_path)\n",
        "    if not path.exists():\n",
        "        urlretrieve(remote_url, local_path)\n",
        "\n",
        "missing = [p for p in required_files if not Path(p).exists()]\n",
        "if missing:\n",
        "    raise FileNotFoundError(f\"Missing required notebook assets: {missing}\")\n",
        "\n",
        "print(\"Bootstrap complete: module assets are ready.\")"
    ])

    bootstrap_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": "bootstrap-cell",
        "metadata": {
            "colab": {
                "base_uri": "https://localhost:8080/"
            },
            "id": "bootstrap-cell",
            "outputId": "bootstrap-output"
        },
        "outputs": [],
        "source": bootstrap_source
    }

    # Check if bootstrap cell already exists and remove it if it does
    nb['cells'] = [cell for cell in nb['cells'] if cell.get('id') != 'bootstrap-cell']
    
    # Insert bootstrap cell after the first markdown cell (usually title/intro)
    nb['cells'].insert(1, bootstrap_cell)

    # Update CSV paths in code cells
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            for line in cell['source']:
                for old_val, new_val in csv_replacements.items():
                    line = line.replace(f"'{old_val}'", f"'{new_val}'").replace(f"\"{old_val}\"", f"\"{new_val}\"")
                new_source.append(line)
            cell['source'] = new_source

    with open(file_path, 'w') as f:
        json.dump(nb, f, indent=2)

# Module 1
update_notebook(
    'assets/notebooks/module-1-notebook.ipynb',
    'https://raw.githubusercontent.com/ariavasulin/critical-thinking-with-data/main/assets/notebooks/module-1',
    {
        'data/Galton_Family_Heights.csv': '',
        'figures/Francis_Galton2.jpg': '',
        'figures/Francis_Galton_1850s.jpg': '',
        'figures/Sir_Francis_Galton,_1890s.jpg': '',
        'figures/child_height_distributions.png': '',
        'figures/correlation_heatmap.png': '',
        'figures/correlation_heatmap_nb.png': '',
        'figures/eda_combined_display.png': '',
        'figures/height_boxplots.png': '',
        'figures/module1_summary_display.png': '',
        'figures/module1_summary_figure.png': '',
        'figures/regression_to_mean.png': '',
        'figures/regression_to_mean_nb.png': '',
        'figures/residual_analysis.png': '',
        'figures/residual_analysis_nb.png': '',
        'figures/scatter_regression_plots.png': '',
        'figures/scatter_regression_plots_nb.png': '',
        'figures/transmutation_comparison.png': '',
        'figures/transmutation_comparison_nb.png': '',
    },
    {'Galton_Family_Heights.csv': 'data/Galton_Family_Heights.csv'}
)

# Module 2
update_notebook(
    'assets/notebooks/module-2-notebook.ipynb',
    'https://raw.githubusercontent.com/ariavasulin/critical-thinking-with-data/main/assets/notebooks/module-2',
    {
        "data/diagnoses_top10.csv": "",
        "data/novak_2018_contingency.csv": "",
        "data/novak_2018_rate_ratios.csv": "",
        "data/plate25_household_furniture.csv": "",
        "data/stern_2017_ages.csv": "",
        "data/stern_2017_sex.csv": "",
        "data/stern_2017_timeseries.csv": "",
        "images/carrillo_ab1764_author.jpg": "",
        "images/kallikak_chart7.jpg": "",
        "images/kallikak_deborah_frontispiece.jpg": "",
        "images/kallikak_pedigree_1912.jpg": "",
        "images/original-plate-25.jpg": "",
        "images/plate25_defaults.png": "",
        "images/plate25_dubois_style.png": "",
        "images/plate25_side_by_side.png": "",
        "images/popenoe_1931.jpg": "",
        "images/recommendation_form_redacted.jpg": "",
        "images/side_by_side_dubois_kallikak.png": "",
        "images/sonoma_state_home.jpg": "",
    },
    {
        'diagnoses_top10.csv': 'data/diagnoses_top10.csv',
        'novak_2018_contingency.csv': 'data/novak_2018_contingency.csv',
        'novak_2018_rate_ratios.csv': 'data/novak_2018_rate_ratios.csv',
        'plate25_household_furniture.csv': 'data/plate25_household_furniture.csv',
        'stern_2017_ages.csv': 'data/stern_2017_ages.csv',
        'stern_2017_sex.csv': 'data/stern_2017_sex.csv',
        'stern_2017_timeseries.csv': 'data/stern_2017_timeseries.csv',
        'carrillo_ab1764_author.jpg': 'images/carrillo_ab1764_author.jpg',
        'kallikak_chart7.jpg': 'images/kallikak_chart7.jpg',
        'kallikak_deborah_frontispiece.jpg': 'images/kallikak_deborah_frontispiece.jpg',
        'kallikak_pedigree_1912.jpg': 'images/kallikak_pedigree_1912.jpg',
        'original-plate-25.jpg': 'images/original-plate-25.jpg',
        'plate25_defaults.png': 'images/plate25_defaults.png',
        'plate25_dubois_style.png': 'images/plate25_dubois_style.png',
        'plate25_side_by_side.png': 'images/plate25_side_by_side.png',
        'popenoe_1931.jpg': 'images/popenoe_1931.jpg',
        'recommendation_form_redacted.jpg': 'images/recommendation_form_redacted.jpg',
        'side_by_side_dubois_kallikak.png': 'images/side_by_side_dubois_kallikak.png',
        'sonoma_state_home.jpg': 'images/sonoma_state_home.jpg',
    }
)
