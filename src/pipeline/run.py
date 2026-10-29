#%%
from pipeline.fetch_data import fetch_all
from pipeline.prepare_data import run_prepare_data_pipeline
from analysis.analysis_pipeline import run_analysis_pipeline
from report.create_report import create_report_file

def run_pipeline(output_report=False):
    fetch_all()
    run_prepare_data_pipeline()
    if output_report:
        create_report_file()
    else:
        run_analysis_pipeline()    
    print("Pipeline execution completed.")

if __name__ == "__main__":
    run_pipeline(output_report=True)

