# Use the official RabbitMQ image from Docker Hub
FROM rabbitmq:3.8

# Set the environment variables
ENV RABBITMQ_DEFAULT_USER rojan
ENV RABBITMQ_DEFAULT_PASS rojan
ENV RABBITMQ_DEFAULT_VHOST /

# Expose RabbitMQ ports
EXPOSE 5672 15672

# Define the entry point to start RabbitMQ server
CMD ["rabbitmq-server"]
