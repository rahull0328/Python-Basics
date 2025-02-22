email = input("Enter your email ID: ")

username, domain = email.split("@")
service_provider, domain_name = domain.split(".")

print("\n===== Extracted Email Details =====")
print(f"Username         : {username}")
print(f"Service Provider : {service_provider}")
print(f"Domain Name      : {domain_name}")
