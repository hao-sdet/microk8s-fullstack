# Generate a private-public key pair
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=example Inc./CN=example.com' -keyout example.com.key.pem -out example.com.pem

# Create a TLS secret
microk8s kubectl create secret tls example-com-tls --cert=example.com.pem --key=example.com.key.pem
