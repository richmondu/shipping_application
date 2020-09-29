# Shipping Fee Application

Note: 
Python was used in this exercise instead of Java


# Unit testing

1. Run unittest.bat. This will run 

   unittest_parcel.py - test Parcel module
   unittest_voucher.py - test Voucher module
   unittest_shipping_fee.py - test Shipping Fee module (uses Parcel and Voucher modules)


# System testing


### How to test using Swagger:

1. Go to https://petstore.swagger.io/

2. In the textbox above, type https://myntshippingfeeapplication.s3.amazonaws.com/swagger_openapi.json

3. Click Explore button.

4. Choose Server

   a. local testing - http://127.0.0.1:8000
   b. live testing - https://richmondu.com

5. Test the API

   a. Input weight, height, width and length
   b. Choose code (voucher code for discount)


### How to test using Curl:

1. Refer to shipping_application/_curltest for sample batch scripts


