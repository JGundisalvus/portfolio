import nbformat as nbf

# Load the current notebook
with open('polish_marriage_demographics/data_exploration.ipynb') as f:
    notebook = nbf.read(f, as_version=4)

# Create a new notebook with specific cells suppressed
new_notebook = notebook.copy()
new_notebook['cells'] = [cell for cell in notebook['cells'] if 'hide' not in cell.get('metadata', {}).get('tags', [])]

# Save the new notebook
with open('polish_marriage_demographics/data_exploration_no_code.ipynb', 'w') as f:
    nbf.write(new_notebook, f)

print("Notebook exported with hidden cells removed.")
