---
title: Notebook
parent: "Module 1: Measure"
nav_order: 2
permalink: /modules/module-1-measure/notebook/
---

# Notebook — Module 1

Use the embedded notebook below or download a copy to run locally in Jupyter.

<a href="https://colab.research.google.com/github/ariavasulin/critical-thinking-with-data/blob/main/assets/notebooks/module-1-notebook.ipynb" target="_blank" rel="noopener noreferrer">Open Module 1 Notebook in Google Colab</a>

<button type="button" id="download-module-1-notebook">Download Module 1 Notebook (.ipynb)</button>

<script>
  (function () {
    const btn = document.getElementById("download-module-1-notebook");
    if (!btn) return;
    btn.addEventListener("click", async function () {
      const url = "{{ site.baseurl }}/assets/notebooks/module-1-notebook.ipynb";
      const response = await fetch(url, { mode: "cors", cache: "no-store" });
      const blob = await response.blob();
      const objectUrl = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = objectUrl;
      link.download = "module-1-notebook.ipynb";
      document.body.appendChild(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(objectUrl);
    });
  })();
</script>

{% include notebook_viewer.html url="{{ site.baseurl }}/assets/notebooks/module-1-notebook.ipynb" %}
