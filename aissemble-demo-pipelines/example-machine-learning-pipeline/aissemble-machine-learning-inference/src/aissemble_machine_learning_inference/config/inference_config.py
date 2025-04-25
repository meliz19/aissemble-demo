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
Configurations for inference, read from the inference properties file.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/general-mlflow/inference.config.py.vm 
"""

from krausening.properties import PropertyManager


class InferenceConfig:
    """
    Configurations for inference, read from the inference properties file.
    """

    def __init__(self):
        self.properties = PropertyManager.get_instance().get_properties(
            "inference.properties"
        )

    def model_directory(self):
        """
        Returns the location of the model to load
        """
        return self.properties["model_directory"]
