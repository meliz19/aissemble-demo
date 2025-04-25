allow_k8s_contexts('local')
docker_prune_settings(num_builds=1, keep_recent=1)

aissemble_version = '1.12.1'

build_args = { 'DOCKER_BASELINE_REPO_ID': 'ghcr.io/',
               'VERSION_AISSEMBLE': aissemble_version}

# Kafka
yaml = helm(
    'aissemble-demo-deploy/src/main/resources/apps/kafka-cluster',
    values=['aissemble-demo-deploy/src/main/resources/apps/kafka-cluster/values.yaml',
        'aissemble-demo-deploy/src/main/resources/apps/kafka-cluster/values-dev.yaml']
)
k8s_yaml(yaml)

# Add deployment resources here
k8s_kind('SparkApplication', image_json_path='{.spec.image}')


yaml = local('helm template oci://ghcr.io/boozallen/aissemble-spark-application-chart --version %s\
        --values aissemble-demo-pipelines/py-spark-data-delivery-example/src/py_spark_data_delivery_example/resources/apps/py-spark-data-delivery-example-base-values.yaml\
        --values aissemble-demo-pipelines/py-spark-data-delivery-example/src/py_spark_data_delivery_example/resources/apps/py-spark-data-delivery-example-dev-values.yaml' % aissemble_version)
k8s_yaml(yaml)
k8s_resource('py-spark-data-delivery-example', port_forwards=[port_forward(4747, 4747, 'debug')], auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)

yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/metadata',
   name='metadata',
   values=['aissemble-demo-deploy/src/main/resources/apps/metadata/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/metadata/values-dev.yaml']
)
k8s_yaml(yaml)

yaml = local('helm template oci://ghcr.io/boozallen/aissemble-spark-application-chart --version %s\
        --values aissemble-demo-pipelines/spark-data-delivery-example/src/main/resources/apps/spark-data-delivery-example-base-values.yaml\
        --values aissemble-demo-pipelines/spark-data-delivery-example/src/main/resources/apps/spark-data-delivery-example-dev-values.yaml' % aissemble_version)
k8s_yaml(yaml)
k8s_resource('spark-data-delivery-example', port_forwards=[port_forward(4747, 4747, 'debug')], auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/spark-operator',
   name='spark-operator',
   values=['aissemble-demo-deploy/src/main/resources/apps/spark-operator/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/spark-operator/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/policy-decision-point',
   name='policy-decision-point',
   values=['aissemble-demo-deploy/src/main/resources/apps/policy-decision-point/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/policy-decision-point/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/spark-infrastructure',
   name='spark-infrastructure',
   values=['aissemble-demo-deploy/src/main/resources/apps/spark-infrastructure/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/spark-infrastructure/values-dev.yaml']
)
k8s_yaml(yaml)

yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/s3-local',
   name='s3-local',
   values=['aissemble-demo-deploy/src/main/resources/apps/s3-local/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/s3-local/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/pipeline-invocation-service',
   name='pipeline-invocation-service',
   values=['aissemble-demo-deploy/src/main/resources/apps/pipeline-invocation-service/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/pipeline-invocation-service/values-dev.yaml']
)
k8s_yaml(yaml)

yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/aissemble-machine-learning-inference',
   name='aissemble-machine-learning-inference',
   values=['aissemble-demo-deploy/src/main/resources/apps/aissemble-machine-learning-inference/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/aissemble-machine-learning-inference/values-dev.yaml']
)
k8s_yaml(yaml)

yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/shared-infrastructure',
   name='shared-infrastructure',
   values=['aissemble-demo-deploy/src/main/resources/apps/shared-infrastructure/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/shared-infrastructure/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/model-training-api',
   name='model-training-api',
   values=['aissemble-demo-deploy/src/main/resources/apps/model-training-api/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/model-training-api/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/mlflow-ui',
   name='mlflow-ui',
   values=['aissemble-demo-deploy/src/main/resources/apps/mlflow-ui/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/mlflow-ui/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'aissemble-demo-deploy/src/main/resources/apps/postgres',
   name='postgres',
   values=['aissemble-demo-deploy/src/main/resources/apps/postgres/values.yaml',
       'aissemble-demo-deploy/src/main/resources/apps/postgres/values-dev.yaml']
)
k8s_yaml(yaml)
