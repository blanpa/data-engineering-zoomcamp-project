Kafka
https://docs.confluent.io/platform/current/platform-quickstart.html#step-1-download-and-start-cp


set-up enviorment
    sudo docker-compose -p "data_ingestion" up -d 

topics


MQTT Conector:
    confluent-hub install confluentinc/kafka-connect-mqtt:latest
https://docs.confluent.io/kafka-connectors/mqtt/current/mqtt-source-connector/overview.html#mqtt-source-connector-for-cp

Sinks:
Big Query:
    confluent-hub install wepay/kafka-connect-bigquery:latest
https://docs.confluent.io/kafka-connectors/bigquery/current/overview.html#google-bigquery-sink-connector-for-cp

Google Cloud Storage:
    confluent-hub install confluentinc/kafka-connect-gcs:latest
https://docs.confluent.io/kafka-connectors/gcs-sink/current/overview.html