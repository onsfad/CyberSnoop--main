# app/metrics.py
from prometheus_client import Counter, REGISTRY

# Vérifie si le compteur existe déjà pour éviter la duplication
def get_or_create_counter(name, description):
    try:
        return Counter(name, description)
    except ValueError:
        for collector in REGISTRY._collector_to_names:
            if name in REGISTRY._collector_to_names[collector]:
                return collector
        raise

REQUEST_COUNT = get_or_create_counter('flask_requests_total', 'Total number of requests')
CREATED_COUNT = get_or_create_counter('flask_requests_created', 'Number of created resources')
