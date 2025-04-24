package com.test.aissemble;

/*-
 * #%L
 * aiSSEMBLE Demo::Pipelines::Spark Data Delivery Example
 * %%
 * Copyright (C) 2021 Booz Allen
 * %%
 * All Rights Reserved. You may not copy, reproduce, distribute, publish, display,
 * execute, modify, create derivative works of, transmit, sell or offer for resale,
 * or in any way exploit any part of this solution without Booz Allen Hamilton's
 * express written permission.
 * #L%
 */

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;



import jakarta.enterprise.inject.Any;
import jakarta.enterprise.inject.spi.CDI;

import com.test.aissemble.pipeline.PipelineBase;

/**
 * Configures the steps needed to run a Spark-based implementation for SparkDataDeliveryExample.
 *
 * This pipeline serves the following purpose: ${pipeline.description}.
 *
 * Please **DO** modify with your customizations, as appropriate.
 *
 * Originally generated from: templates/pipeline.driver.impl.java.vm 
 */
public class SparkDataDeliveryExampleDriver extends SparkDataDeliveryExampleBaseDriver {

  private static final Logger logger = LoggerFactory.getLogger(SparkDataDeliveryExampleDriver.class);
  
  public static void main(String[] args) {
    logger.info("STARTED: {} driver", "SparkDataDeliveryExample");
    SparkDataDeliveryExampleBaseDriver.main(args);



    final IngestData ingestData = CDI.current().select(IngestData.class, new Any.Literal()).get();
    ingestData.executeStep();
  }
}
