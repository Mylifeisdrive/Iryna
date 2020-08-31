
import requests


# response=requests.get("https://www.qa.saatchiart.com/easel_api/artwork/753751/676018")
# print(response)

# response.status_code
# print(response.status_code)
# print(response.json())
# print(response.cookies)
# print(response.headers)

body={
  "budget":"1500",
  "email":"nobug@gamol.com",
  "firstName":"Iryna",
  "lastName":"Scott"
}

enough=requests.post("https://www.qa.saatchiart.com/easel_api/aaquiz",json=body)

print(enough)

print(enough.json())

# Press the green button in the gutter to run the script.
