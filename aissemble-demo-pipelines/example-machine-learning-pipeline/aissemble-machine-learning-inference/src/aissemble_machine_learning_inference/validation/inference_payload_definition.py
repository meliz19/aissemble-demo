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
Defines the request/response payloads utilized in an inference analytic for capturing input data records upon
which inferencing will be executed as well as the structure of inference results.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/inference/inference.payload.impl.py.vm
"""

from ..generated.validation.inference_payload_definition_base import (
    RecordBase,
    InferenceBase,
)


class Record(RecordBase):
    """
    Represents an input data record utilized within an inference request.
    NOTE: If this input data record definition is updated (i.e. fields are added/removed/updated), the equivalent
    changes MUST be made to the corresponding request/response payload definition in
    src/main/resource/proto/inference_payload_definition.proto, which is used to expose the relevant inference
    analytic as a gRPC endpoint.
    """

    pass


class Inference(InferenceBase):
    """
    Represents an inference result of the model prediction.
    NOTE: If this result inference definition is updated (i.e. fields are added/removed/updated), the equivalent
    changes MUST be made to the corresponding request/response payload definition in
    src/main/resource/proto/inference_payload_definition.proto, which is used to expose the relevant inference
    analytic as a gRPC endpoint.
    """

    pass
