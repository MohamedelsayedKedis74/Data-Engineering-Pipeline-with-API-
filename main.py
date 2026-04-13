from pipeline.extract import extract
from pipeline.transform import transform
from pipeline.load import load

def run_pipeline():
    df = extract()
    df = transform(df)
    load(df)
    print("Pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()
