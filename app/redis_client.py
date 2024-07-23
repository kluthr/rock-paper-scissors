from redis import Redis


# TODO: redis security + config for non-local deployments?
redis_client = Redis(host="redis", port=6379)
