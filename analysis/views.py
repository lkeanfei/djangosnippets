from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import firebase_admin
import django.core.exceptions
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
import random
import os
import json
import time
import re
from datetime import datetime
from datetime import timedelta
from django.db.models.functions import Length
from .models import Counters
from .models import Trackerholderstable
from .models import Lastdone
from .models import Eodtable
from .models import Newhightable
from .models import Newlowtable
from .models import Unusualvolume
from .models import Topgainers
from .models import Topgainerspct
from .models import Toplosers
from .models import Toploserspct
from .models import Updateddatelist
from .models import Technicals
from .models import Rsitable
from .models import Gainersloserstable
from .models import Securitysummary
from .models import Tradingdays
from .models import Distshareholdingstable
from .models import Staticbox
from .models import Staticboxbreakout
from .models import Dynamicbox
from .models import Dynamicboxbreakout
from .models import Aggregatetradesummary
from .models import Aggregatepricerow
from .models import Shareholdingsummary
from .models import Ownership
from .models import Marketoverview
from .models import Financialinfo
from .models import Screenerview
from .models import Securityoverview
from .models import Corporateinfo
from .models import Balancesheettable
from .models import Profitlosstable
from .models import Cashflowtable
from .models import Quarterlies
from .models import Eodtableview
from .models import Turnover
from .models import Bullishbearishsummary
from .models import Bullishbearish
from .models import Candlestickspattern
from .models import Activecounters
from .models import Arimaforecast
from .models import Arimaforecastview
from .models import Arimaforecastaccuracy
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
import logging
from locale import atof
from enum import Enum
logger = logging.getLogger("app")
# Create your views here.

@csrf_protect
def index(request):
    # return HttpResponse('Hello from Python!')
    c = {}
    request.session.set_test_cookie();

    return render(request, 'index.html' ,c)

class Status(Enum):
    OK = True
    FAILED = False


class SessionCheck:

    @staticmethod
    def checkSession( request):

        res = {}
        dirpath = os.path.dirname(os.path.abspath(__file__))
        #  Read from environment variables
        credDict = {}
        credDict["type"] = os.environ["type"]
        credDict["project_id"] = os.environ["project_id"]
        credDict["private_key_id"] = os.environ["private_key_id"]
        credDict["private_key"] = os.environ["private_key"].replace('\\n', '\n')
        credDict["client_email"] = os.environ["client_email"]
        credDict["client_id"] = os.environ["client_id"]
        credDict["auth_uri"] = os.environ["auth_uri"]
        credDict["token_uri"] = os.environ["token_uri"]
        credDict["auth_provider_x509_cert_url"] = os.environ["auth_provider_x509_cert_url"]
        credDict["client_x509_cert_url"] = os.environ["client_x509_cert_url"]

        logger.info(credDict.__str__())
        cred = credentials.Certificate(credDict)
        appLength = len(firebase_admin._apps)

        if appLength == 0:
            app = firebase_admin.initialize_app(cred)
        else:
            for appName in firebase_admin._apps:
                app = firebase_admin.get_app(appName)

        try:
            session_cookie = request.COOKIES['session']
            decoded_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)


            uid = decoded_claims['sub']
            user = auth.get_user(uid)

            displayName = ""
            if user.display_name != None:
                displayName = user.display_name

            photoURL = ""

            if user.photo_url != None:
                photoURL = user.photo_url



            res['status'] = Status.OK
            res['name'] = displayName
            res['email'] = user.email
            res['photourl'] = photoURL

        except KeyError as kErr:
            # Session cookie is unavailable or invalid. Force user to login.
            logger.info('Key Error!')
            logger.info(kErr.args)
            res['status'] = Status.FAILED
            res['details'] = 'KeyError'

        except ValueError as vErr:
            # return flask.abort(401, 'Invalid ID token')


            # Session cookie is unavailable or invalid. Force user to login.

            logger.info('Value Error!')
            logger.info(vErr.args)
            res['status'] = Status.FAILED
            res['details'] = 'ValueError'

        except auth.AuthError:
            logger.info('Auth Error!')
            # Session revoked. Force user to login.
            res['status'] = Status.FAILED
            res['details'] = ' SessionRevoked'


        return res

class OwnerShareholdingsView(APIView):

    def post(self, request):

        res = {}

        if  "name" in request.data.keys():

            toTradingDateObj = Tradingdays.objects.filter(Q(country='MY')).order_by('-tradingdate').first()

            screenerkwargs = {}
            screenerkwargs["tradedate"] = toTradingDateObj.tradingdate
            screenerkwargs["name__icontains"] = request.data['name']

            toRows = Ownership.objects.filter(**screenerkwargs).values('counterfullid__name', 'counterfullid__symbol',
                                                                       'rank', 'name', 'numshares', 'percentage',
                                                                       'sharesworth')

            toResultList = []
            toSymbolList = []


            for row in toRows:
                resDict = {}
                resDict['Symbol'] = row["counterfullid__name"]
                resDict["Code"] = row["counterfullid__symbol"]
                resDict["Name"] = row["name"]
                resDict["Rank"] = row["rank"]
                resDict["Shares"] = row['numshares']
                resDict["Percentage"] = row["percentage"]

                toResultList.append(resDict)

        res["results"] = toResultList

        return JsonResponse(res)

    def Archivepost(self , request):

        res = {}


        if "fromdate" in request.data.keys() and "todate" in request.data.keys() and "name" in request.data.keys():

            logger.info('IOnsesee! ' +  request.data['fromdate'] + ' ' +  request.data['todate'] + ' '+  request.data['name'])
            tradeKeyStr = '{0}__{1}'.format('tradingdate', 'gte')
            tradeargs = {}
            tradeargs[tradeKeyStr] = request.data['fromdate']
            row = Tradingdays.objects.filter(**tradeargs).order_by('tradingdate').first()

            keyStr = '{0}'.format('tradedate')
            screenerkwargs = {}
            screenerkwargs[keyStr] = row.tradingdate.strftime('%Y-%m-%d')
            screenerkwargs["name__icontains"] = request.data['name']

            fromRows = Ownership.objects.filter(**screenerkwargs).values('counterfullid__name' , 'counterfullid__symbol', 'rank' , 'name' , 'sharesworth' ,'numshares' , 'percentage')

            fromResultList = []
            fromSymbolList = []
            for row in fromRows:
                resDict = {}
                resDict['Symbol'] = row["counterfullid__name"]
                resDict["Code"] = row["counterfullid__symbol"]
                resDict["Name"] = row["name"]
                resDict["Rank"] = row["rank"]
                resDict["Shares"] = row['numshares']
                resDict["Percentage"] = row["percentage"]
                fromSymbolList.append(resDict['Symbol'])
                fromResultList.append(resDict)

            # to date
            tradeKeyStr = '{0}__{1}'.format('tradingdate', 'lte')
            tradeargs = {}
            tradeargs[tradeKeyStr] = request.data['todate']
            row = Tradingdays.objects.filter(**tradeargs).order_by('-tradingdate').first()

            keyStr = '{0}'.format('tradedate')
            screenerkwargs = {}
            screenerkwargs[keyStr] = row.tradingdate.strftime('%Y-%m-%d')
            screenerkwargs["name__icontains"] = request.data['name']

            toRows = Ownership.objects.filter(**screenerkwargs).values('counterfullid__name' ,'counterfullid__symbol', 'rank', 'name', 'numshares' , 'percentage',
                                                                         'sharesworth')

            toResultList = []
            toSymbolList = []
            for row in toRows:
                resDict = {}
                resDict['Symbol'] = row["counterfullid__name"]
                resDict["Code"] = row["counterfullid__symbol"]
                resDict["Name"] = row["name"]
                resDict["Rank"] = row["rank"]
                resDict["Shares"] = row['numshares']
                resDict["Percentage"] = row["percentage"]
                fromSymbolList.append(resDict['Symbol'])
                toResultList.append(resDict)

            finalList = []


            combineSymbolList = list(set(fromSymbolList).union(set(toSymbolList)))

            for symbol in combineSymbolList:
                finalDict = {}
                fromDict = next( (item for item in fromResultList if item["Symbol"] == symbol), None)
                toDict = next( (item for item in toResultList if item["Symbol"] == symbol) , None)

                fromHasShares = False

                finalDict["FromHasShares"] = fromHasShares
                finalDict["FromShares"] = 0
                finalDict["FromPercentage"] = 0
                if fromDict is not None:
                    fromHasShares = True
                    finalDict["Symbol"] = fromDict["Symbol"]
                    finalDict["Code"] = fromDict["Code"]
                    finalDict["Name"] = fromDict["Name"]
                    finalDict["FromHasShares"] = fromHasShares
                    finalDict["FromShares"] = fromDict['Shares']
                    finalDict["FromPercentage"] = fromDict['Percentage']

                toHasShares = False
                finalDict["ToShares"] = 0
                finalDict["ToPercentage"] = 0
                finalDict["ToHasShares"] = toHasShares

                if toDict is not None:
                    toHasShares = True
                    finalDict["Symbol"] = toDict["Symbol"]
                    finalDict["Code"] = toDict["Code"]
                    finalDict["Name"] = toDict["Name"]
                    finalDict["ToHasShares"] = toHasShares
                    finalDict["Symbol"] = toDict["Symbol"]
                    finalDict["Name"] = toDict["Name"]
                    finalDict["ToShares"] = toDict['Shares']
                    finalDict["ToPercentage"] = toDict['Percentage']

                finalDict["SharesDiff"] = finalDict["ToShares"] - finalDict["FromShares"]
                finalDict["PctDiff"] = finalDict["ToPercentage"] - finalDict["FromPercentage"]

                finalList.append(finalDict)



        sortedFinalList = sorted(finalList , key= lambda k:k["SharesDiff"] , reverse=True)

        res["results"] = sortedFinalList


        return JsonResponse(res)


class ForecastAnalysisView(APIView):

    def post(self, request):

        res = {}

        toTradingDateObj = Tradingdays.objects.filter(Q(country='MY')).order_by('-tradingdate').first()

        forecastCounterkwargs = {}
        forecastCounterkwargs["tradedate"] = toTradingDateObj.tradingdate

        forecastCounters = Arimaforecast.objects.filter(**forecastCounterkwargs).values('counterfullid__name',
                                                                                     'counterfullid__fullname',
                                                                                     'counterfullid' , "forecastdate")

        bucket = {}

        for cnt in range(48, 58):
            bucket[chr(cnt)] = []

        for cnt in range(65, 91):
            bucket[chr(cnt)] = []

        print(bucket.keys())

        forecastDate = None

        for activeCounter in forecastCounters:
            forecastDate = activeCounter["forecastdate"]
            counterDict = {}
            counterDict["Symbol"] = activeCounter["counterfullid"]

            firstCharacter = activeCounter["counterfullid__name"][0]

            counterDict["Name"] = activeCounter["counterfullid__name"]
            counterDict["FullName"] = activeCounter["counterfullid__fullname"]

            bucket[firstCharacter].append(counterDict)

        for cnt in range(65, 91):
            bucket[chr(cnt)] = sorted( bucket[chr(cnt)] , key= lambda k:k["Name"] )

        res["results"] = bucket
        res["forecastdate"] = forecastDate.strftime("%d-%b-%Y")

        return JsonResponse(res)









class ActiveCountersView(APIView):

    def post(self, request):

        res = {}

        tradeargs = {}
        tradeargs["country"] = "MY"
        # row = Tradingdays.objects.filter(**tradeargs).order_by('-tradingdate').first()
        row = Activecounters.objects.order_by("tradedate").last()

        activeCounterkwargs = {}
        activeCounterkwargs["tradedate"] = row.tradedate


        activeCounters = Activecounters.objects.filter(**activeCounterkwargs).values('counterfullid__name', 'counterfullid__fullname', 'counterfullid' )

        bucket = {}

        for cnt in range(48,58):
            bucket[chr(cnt)] = []

        for cnt in range(65,91):

            bucket[chr(cnt)] = []


        print(bucket.keys())

        for activeCounter in activeCounters:

            counterDict = {}
            counterDict["Symbol"] = activeCounter["counterfullid"]

            firstCharacter = activeCounter["counterfullid__name"][0]

            counterDict["Name"] = activeCounter["counterfullid__name"]
            counterDict["FullName"] = activeCounter["counterfullid__fullname"]

            bucket[firstCharacter].append(counterDict)

        for cnt in range(65,91):
            bucket[chr(cnt)] = sorted(bucket[chr(cnt)] , key = lambda k:k["Name"])

        res["results"] = bucket


        return JsonResponse(res)






class CompanySharesView(APIView):

    def post(self , request):

        res = {}

        if "fromdate" in request.data.keys() and "todate" in request.data.keys():

            if "fromdate" in request.data.keys():
                tradeKeyStr = '{0}__{1}'.format('tradingdate' , 'gte')
                tradeargs = {}
                tradeargs[tradeKeyStr] = request.data['fromdate']
                row = Tradingdays.objects.filter(**tradeargs).order_by('tradingdate').first()

                keyStr = '{0}'.format('tradedate')
                screenerkwargs = {}

                screenerkwargs[keyStr] = row.tradingdate.strftime('%Y-%m-%d')
                fromrows = Financialinfo.objects.select_related("counterfullid").filter(**screenerkwargs).values(
                    'tradedate', 'numshares', 'counterfullid__symbol')

                # logger.info('from list ' + str(len(fromrows)))
            if "todate" in request.data.keys():
                tradeKeyStr = '{0}__{1}'.format('tradingdate', 'lte')
                tradeargs = {}
                tradeargs[tradeKeyStr] = request.data['todate']
                row = Tradingdays.objects.filter(**tradeargs).order_by('-tradingdate').first()

                screenerkwargs = {}
                keyStr = '{0}'.format('tradedate')
                screenerkwargs[keyStr] = row.tradingdate.strftime('%Y-%m-%d')
                torows = Financialinfo.objects.select_related("counterfullid").filter(**screenerkwargs).values(
                    'tradedate', 'numshares', 'counterfullid__symbol')

                # logger.info('to list ' + str(len(torows)))

            startTime = time.time()
            fromResList = []
            fromSymbolList = []
            toResList = []
            toSymbolList = []
            for row in fromrows:
                resDict = {}
                resDict['TradeDate'] = row['tradedate']
                resDict['NumShares'] = row['numshares']
                resDict['Symbol'] = row['counterfullid__symbol']
                fromSymbolList.append(row['counterfullid__symbol'])
                fromResList.append(resDict)

            for row in torows:
                resDict = {}
                resDict['TradeDate'] = row['tradedate']
                resDict['NumShares'] = row['numshares']
                resDict['Symbol'] = row['counterfullid__symbol']
                toSymbolList.append(row['counterfullid__symbol'])
                toResList.append(resDict)

            intersectSymbolList = list(set(fromSymbolList).intersection(set(toSymbolList)))

            resList = []
            for symbol in intersectSymbolList:
                resDict = {}
                fromDict = next(item for item in fromResList if item["Symbol"] == symbol)
                toDict = next(item for item in toResList if item["Symbol"] == symbol)
                sharesDiff = toDict['NumShares'] - fromDict['NumShares']
                resDict['Symbol'] = fromDict['Symbol']
                resDict['SharesDiff'] = sharesDiff
                resDict['SharesDiffPct'] = 100.0*sharesDiff/fromDict['NumShares']
                resDict['FromShares'] = fromDict['NumShares']
                resDict['ToShares'] = toDict['NumShares']
                resList.append(resDict)


            dur = time.time() - startTime
            sortedResList =  sorted(resList , key= lambda k:k['SharesDiffPct'] , reverse=True)
            res["results"] = sortedResList
            logger.info(dur)

        return JsonResponse(res)
