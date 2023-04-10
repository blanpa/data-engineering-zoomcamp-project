# 🚧 Currently under construction,read at your own risk 🚧

# data-engineering-zoomcamp-

This Repository contains my submission for the data engineering zoomcamp cohort 2023

## Problem statement

To prove what I have learned in the past weeks, I would like to use both stream and batch processing for my project. The search for suitable data has turned out to be somewhat problematic. I work in industrial engineering and wanted to work with production related data. Unfortunately, there are only very few open data sets. To push it to the extreme I wanted to process a lot of data. So I decided to simulate the stream processing data with mqtt and use the Bosch Production Line performance dataset for batch processing.

For those who dont know MQTT:
MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol that enables communication between devices connected to the Internet of Things (IoT). It is designed to be simple and efficient, making it well-suited for use in low-power, low-bandwidth environments. MQTT uses a publish/subscribe messaging model, where devices publish messages to a broker and subscribe to receive messages from the broker. This makes it easy to distribute data to multiple devices and enables real-time communication between devices. MQTT is widely used in IoT applications, including home automation, industrial automation, and healthcare.

You think that sounds like Apache Kafka, yes? MQTT and Kafka are both messaging systems, but they have different architectures and use cases.

MQTT is a lightweight messaging protocol designed for IoT and M2M communication. It is simple and efficient, with low overhead, making it well-suited for use in low-power, low-bandwidth environments. MQTT uses a publish/subscribe model, where devices publish messages to a broker and subscribe to receive messages from the broker.

Kafka, on the other hand, is a distributed streaming platform designed for processing high-volume, real-time data streams. It is used for building real-time data pipelines and streaming applications. Kafka uses a distributed publish/subscribe model, where producers write data to topics, and consumers read data from topics.

The main differences between MQTT and Kafka are:

Architecture: MQTT is a client-server protocol, where devices communicate with a central broker. Kafka is a distributed system, with multiple brokers and consumers.

Use Case: MQTT is designed for lightweight communication between IoT devices, whereas Kafka is designed for handling high-volume, real-time data streams.

Message Semantics: MQTT provides at-most-once, at-least-once, and exactly-once delivery semantics, whereas Kafka provides at-least-once delivery semantics.

Message Ordering: MQTT does not guarantee message ordering, whereas Kafka guarantees message ordering within a partition.

Overall, MQTT is suitable for simple, lightweight communication, while Kafka is more suited to complex, high-volume data processing and stream processing applications.


The goal of this project is to better evaluate the simulated data. It is often the case that raw data is not well evaluated in production. There are many current key figures in industrial engineering that are easy to calculate. Often these key figures are calculated only sporadically. In our modern world it is possible to calculate and evaluate them in real time. Thus it is always possible to say whether a process is running well or badly.


## Batch processing Data

## Stream processing Data

# Data Pipeline

![Data Pipeline](https://lucid.app/publicSegments/view/b17ae762-c294-4201-b0d7-8f2f5d238cd7/image.png)

## Used Technologies
- Mqtt
- Apache Kafka
- Prefect
- Google Cloud Storage
- Google big query
- Dbt
- Google Data Studio
- Jupyter Notebook
- Grafana
- Apache Superset?


# Dashboard
As a dashobard solution I decided to use Grafan in addition to Google Data Studio. Grafana because it is a widely used tool in the iiot area and offers the possibility to update the data relatively quickly.

https://umh.docs.umh.app/docs/features/analytics/


# Peer review criteria 

* Problem description
    * 0 points: Problem is not described
    * 1 point: Problem is described but shortly or not clearly 
    * 2 points: Problem is well described and it's clear what the problem the project solves
* Cloud
    * 0 points: Cloud is not used, things run only locally
    * 2 points: The project is developed in the cloud
    * 4 points: The project is developed in the cloud and IaC tools are used
* Data ingestion (choose either batch or stream)
    * Batch / Workflow orchestration
        * 0 points: No workflow orchestration
        * 2 points: Partial workflow orchestration: some steps are orchestrated, some run manually
        * 4 points: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake
    * Stream
        * 0 points: No streaming system (like Kafka, Pulsar, etc)
        * 2 points: A simple pipeline with one consumer and one producer
        * 4 points: Using consumer/producers and streaming technologies (like Kafka streaming, Spark streaming, Flink, etc)
* Data warehouse
    * 0 points: No DWH is used
    * 2 points: Tables are created in DWH, but not optimized
    * 4 points: Tables are partitioned and clustered in a way that makes sense for the upstream queries (with explanation)
* Transformations (dbt, spark, etc)
    * 0 points: No tranformations
    * 2 points: Simple SQL transformation (no dbt or similar tools)
    * 4 points: Tranformations are defined with dbt, Spark or similar technologies
* Dashboard
    * 0 points: No dashboard
    * 2 points: A dashboard with 1 tile
    * 4 points: A dashboard with 2 tiles
* Reproducibility
    * 0 points: No instructions how to run code at all
    * 2 points: Some instructions are there, but they are not complete
    * 4 points: Instructions are clear, it's easy to run the code, and the code works
