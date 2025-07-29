import wandb

run = wandb.init(project="nyc_airbnb", job_type="upload_trainval")
artifact = wandb.Artifact(
    'trainval_data.csv',
    type='processed_data'
)
artifact.add_file("/full/path/to/trainval_data.csv")  # use actual path!
run.log_artifact(artifact)
run.finish()