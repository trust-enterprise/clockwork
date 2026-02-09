import request 
data = {
    "username":"aman",
    "password": 1234
}

response = request.post( 
    "https://example.com/login", 
    json = data
)

print(response.status_code)
print(response.json)