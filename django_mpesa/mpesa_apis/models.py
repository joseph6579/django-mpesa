from django.db import models

# Create your models here.
"""
{
   "Body":{
      "stkCallback":{
         "MerchantRequestID":"24048-2053106-1",
         "CheckoutRequestID":"ws_CO_291120201304065456",
         "ResultCode":0,
         "ResultDesc":"The service request is processed successfully.",
         "CallbackMetadata":{
            "Item":[
               {
                  "Name":"Amount",
                  "Value":1.00
               },
               {
                  "Name":"MpesaReceiptNumber",
                  "Value":"OKT1ZL1E05"
               },
               {
                  "Name":"Balance"
               },
               {
                  "Name":"TransactionDate",
                  "Value":20201129130437
               },
               {
                  "Name":"PhoneNumber",
                  "Value":254707170676
               }
            ]
         }
      }
   }
}

{
   "Body":{
      "stkCallback":{
         "MerchantRequestID":"2893-2060772-1",
         "CheckoutRequestID":"ws_CO_291120201300185608",
         "ResultCode":2001,
         "ResultDesc":"The initiator information is invalid."
      }
   }
}
"""

class LNMTransaction(models.Model):
    MerchantRequestID = models.CharField(max_length=20, unique=True)
    CheckoutRequestID = models.CharField(max_length=30)
    ResultCode = models.CharField(max_length=5)
    Amount = models.CharField(max_length=6)
    MpesaReceiptNumber = models.CharField(max_length=15,  unique=True)
    TransactionDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=16)

    def __str__(self):
        return self.MpesaReceiptNumber

    




