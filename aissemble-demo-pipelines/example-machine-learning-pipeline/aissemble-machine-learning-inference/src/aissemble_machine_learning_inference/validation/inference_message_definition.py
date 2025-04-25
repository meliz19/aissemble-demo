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
Defines the message envelope utilized to interact with an inference analytic.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/inference/inference.message.impl.py.vm
"""

from pandas import DataFrame

from ..generated.validation.inference_message_definition_base import (
    RequestBodyBase,
    ResponseBodyBase,
)


class RequestBody(RequestBodyBase):
    def prep_data(self) -> DataFrame:
        data = DataFrame(self.data_to_dict())

        # TODO: prep the data into the format needed for the predictions
        # data['prepped_field_example'] = np.where(data['raw_field_example'], 1, 0)
        # del data['raw_field_example']

        return data


class ResponseBody(ResponseBodyBase):
    pass
