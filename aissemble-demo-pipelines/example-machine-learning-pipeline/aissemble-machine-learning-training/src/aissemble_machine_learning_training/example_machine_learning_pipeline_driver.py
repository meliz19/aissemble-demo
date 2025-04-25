###
# #%L
# aiSSEMBLE Demo::Pipelines::Aissemble Machine Learning Training
# %%
# Copyright (C) 2021 Booz Allen
# %%
# All Rights Reserved. You may not copy, reproduce, distribute, publish, display,
# execute, modify, create derivative works of, transmit, sell or offer for resale,
# or in any way exploit any part of this solution without Booz Allen Hamilton's
# express written permission.
# #L%
###
"""
Driver to run this pipeline.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/general-mlflow/training.driver.py.vm
"""
import os
import sys

from aissemble_machine_learning_training.impl.example_machine_learning_pipeline import (
    ExampleMachineLearningPipeline,
)
from aissemble_machine_learning_training.config.pipeline_config import PipelineConfig
from kafka import KafkaConsumer

if __name__ == "__main__":
    if os.getenv("MODE") == "no-op":
        print("Training job successfully registered.")
        sys.exit()

    kafka_server = PipelineConfig().kafka_server()
    training_alert_consumer = KafkaConsumer(
        "train",
        group_id="Train",
        bootstrap_servers=[kafka_server],
        auto_offset_reset="earliest",
        api_version=(2, 0, 2),
        max_poll_records=100,
        max_poll_interval_ms=500000,
        enable_auto_commit=False,
    )
    pipeline = ExampleMachineLearningPipeline()

    print("Waiting for training alert from Kafka (%s)..." % kafka_server)

    for alert in training_alert_consumer:
        pipeline.acknowledge_training_alert(alert)
        pipeline.run()
