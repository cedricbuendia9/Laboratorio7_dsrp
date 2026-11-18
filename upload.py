from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="03bd29ee-b412-4e5a-bcdf-4f934d13d944",
    resource_group_name="DSRP",
    workspace_name="dsrp_workspace"
)

model = Model(
    path="Laboratorio-cicd/artifacts/model.pkl",
    name="diabetes-model",
    description="Modelo diabetes 3",
    type="custom_model"
)

ml_client.models.create_or_update(model)

print("Modelo registrado")