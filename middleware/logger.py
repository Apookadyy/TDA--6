import logging

logging.basicConfig(
    filename="enterprise.log",
    level=logging.INFO
)

def log_request(endpoint):
    logging.info(f"Endpoint Hit: {endpoint}")