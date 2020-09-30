# Shipping Fee Application

Notes: 

- Python was used in this exercise instead of Java due to preference
- But I still designed code to be clean and maintanable by utilizing OOP 
- And more importantly testing the code with unit tests and system tests


To cover up for using Python instead of Java, I've added the following features:

- AWS cloud for live deployment
- Swagger for documentation and system testing
- Jenkins CI/CD for automated build and deployment
- Docker and Docker-Compose for containerization


# Design

### Parcel class

This computes the shipping cost given the item's weight and volume.

### Voucher class

This retrieves the percentage discount given a voucher code.

### Shipping Fee class

This integrates both Parcel and Voucher classes to compute the discounted price.


# Unit testing

1. Run unittest.bat. This will run 

	- unittest_parcel.py - test Parcel module
	- unittest_voucher.py - test Voucher module
	- unittest_shipping_fee.py - test Shipping Fee module (uses Parcel and Voucher modules)


# System testing


### How to test using Swagger:

1. Go to https://petstore.swagger.io/

2. In the textbox above, type https://myntshippingfeeapplication.s3.amazonaws.com/swagger_openapi.json

3. Click Explore button.

4. Choose Server

	- local testing - http://127.0.0.1:8000
	- live testing - https://richmondu.com

5. Test the API

	- Input weight, height, width and length
	- Choose code (voucher code) for discount


### How to test using Curl:

1. curl -X GET "%GET_API%?code=random&weight=51&height=1&width=1&length=1" -H "accept: application/json"

2. Refer to shipping_application/_curltest for batch scripts for automated system testing

	- test_curl_live.bat
	- test_curl_live_MYNT.bat
	- test_curl_live_GFI.bat
	- test_curl_live_skdlks
