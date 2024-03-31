
# Split the URL into base and endpoint
base_url = "localhost"
base_endpoint = "api/v1" 

# Now you can use base_url, endpoint, and port in your code
comments_port="8080"
COMMENTS_API="http://{0}:{1}/{2}/".format(base_url,comments_port,base_endpoint)
