import wandb

run = wandb.init(project="nyc_airbnb", job_type="upload_sample")

artifact = wandb.Artifact(
    'sample1.csv',
    type='raw_data'
)

artifact.add_file("components/get_data/data/sample1.csv")
run.log_artifact(artifact)
run.finish()
