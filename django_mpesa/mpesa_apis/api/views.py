from .serializers import LNMSerializer
from rest_framework.views import APIView
from mpesa_apis.models import LNMTransaction
from datetime import datetime
from rest_framework.response import Response

class CreateLNMTransaction(APIView):

    def post(self, request):
        result_code = request.data['Body']['stkCallback']['ResultCode']
        if int(result_code) == 0 :
            trans_date = request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
            trans_date_time = datetime.strptime(str(trans_date), "%Y%m%d%H%M%S")
            LNMTransaction.objects.create(
                MerchantRequestID= request.data['Body']['stkCallback']['MerchantRequestID'],
                CheckoutRequestID= request.data['Body']['stkCallback']['CheckoutRequestID'],
                ResultCode= request.data['Body']['stkCallback']['ResultCode'],
                Amount= request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'],
                MpesaReceiptNumber= request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'],
                TransactionDate= trans_date_time,
                PhoneNumber= request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']
            )
        
        return Response({
            'result_code' : result_code
        })
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
"""
