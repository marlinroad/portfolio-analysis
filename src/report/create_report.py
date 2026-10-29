"""Execute the analysis notebook and export it as a clean HTML report."""

from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor


def create_report_file() -> None:
    project_root = Path.cwd()
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    notebook = nbformat.read(
        project_root / "src/analysis/analysis_pipeline.ipynb",
        as_version=4,
    )

    executor = ExecutePreprocessor(timeout=600, kernel_name="python3")
    executor.preprocess(
        notebook,
        {"metadata": {"path": str(project_root)}},
    )

    exporter = HTMLExporter(
        exclude_input=True,
        exclude_input_prompt=True,
        exclude_output_prompt=True,
    )
    html, _ = exporter.from_notebook_node(notebook)

    (output_dir / "analysis.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    create_report_file()