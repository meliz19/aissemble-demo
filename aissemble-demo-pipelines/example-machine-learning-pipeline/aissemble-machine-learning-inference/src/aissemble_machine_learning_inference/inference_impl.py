###
# #%L
# aiSSEMBLE Demo::Pipelines::Aissemble Machine Learning Inference
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
Implementation of the inference analytic.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/inference/inference.impl.py.vm
"""
import logging

from aissemble_machine_learning_inference.config.inference_config import InferenceConfig
from aissemble_machine_learning_inference.validation.inference_message_definition import (
    RequestBody,
    ResponseBody,
)
from aissemble_machine_learning_inference.validation.inference_payload_definition import (
    Inference,
)

model = None


def load_model():
    """
    Loads the trained model based on the configuration defined in InferenceConfig and make it available for
    utilization for inferencing.
    :return:
    """
    config = InferenceConfig()

    try:
        # Load the model from the model directory
        # model = mlflow.sklearn.load_model(config.model_directory())

        pass
    except Exception:
        logging.exception(f"Failed to load model at {config.model_directory()}")


def execute_inference(request: RequestBody):

    # Prep the data from the inference request
    prepped_data = request.prep_data()

    # Use the model to predict using the prepped data
    # if not model:
    #     load_model()
    #     predictions = model.predict(prepped_data)

    # Process single and batch requests as appropriate
    if len(request.data) > 1:
        pass
    else:
        pass

    return ResponseBody(
        inferences=[Inference(prediction="single-prediction", score=10)]
    )
