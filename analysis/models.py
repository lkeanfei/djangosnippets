
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aggregatepricerow(models.Model):
    pricelevelindex = models.IntegerField(db_column='PriceLevelIndex')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    mostbuyupranking = models.IntegerField(db_column='MostBuyUpRanking', blank=True, null=True)  # Field name made lowercase.
    mostselldownranking = models.IntegerField(db_column='MostSellDownRanking', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trades = models.IntegerField(db_column='Trades', blank=True, null=True)  # Field name made lowercase.
    averagebuyuptrades = models.DecimalField(db_column='AverageBuyUpTrades', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    averageselldowntrades = models.DecimalField(db_column='AverageSellDownTrades', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    buyup = models.IntegerField(db_column='BuyUp', blank=True, null=True)  # Field name made lowercase.
    mid = models.IntegerField(db_column='Mid', blank=True, null=True)  # Field name made lowercase.
    selldown = models.IntegerField(db_column='Selldown', blank=True, null=True)  # Field name made lowercase.
    preopen = models.IntegerField(db_column='Preopen', blank=True, null=True)  # Field name made lowercase.
    preclose = models.IntegerField(db_column='Preclose', blank=True, null=True)  # Field name made lowercase.
    unknown = models.IntegerField(db_column='Unknown', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    aggregatetradesummaryid = models.ForeignKey('Aggregatetradesummary', models.DO_NOTHING, db_column='AggregateTradeSummaryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AggregatePriceRow'
        unique_together = (('pricelevelindex', 'aggregatetradesummaryid'),)


class Aggregatetradesummary(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    mostbuyupprice = models.DecimalField(db_column='MostBuyUpPrice', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mostbuyuppriceaveragetrades = models.DecimalField(db_column='MostBuyUpPriceAverageTrades', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    secondmostbuyupprice = models.DecimalField(db_column='SecondMostBuyUpPrice', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    secondmostbuyuppriceaveragetrades = models.DecimalField(db_column='SecondMostBuyUpPriceAverageTrades', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mostselldownprice = models.DecimalField(db_column='MostSellDownPrice', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mostselldownpriceaveragetrades = models.DecimalField(db_column='MostSellDownPriceAverageTrades', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    secondmostselldownprice = models.DecimalField(db_column='SecondMostSellDownPrice', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    secondmostselldownpriceaveragetrades = models.DecimalField(db_column='SecondMostSellDownPriceAverageTrades', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aggregatedays = models.IntegerField(db_column='AggregateDays', blank=True, null=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AggregateTradeSummary'
        unique_together = (('counterfullid', 'fromdate', 'todate'),)


class Corporateinfo(models.Model):
    website = models.CharField(db_column='Website', max_length=355, blank=True, null=True)  # Field name made lowercase.
    corporatename = models.CharField(db_column='CorporateName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='Counterfullid', blank=True, null=True)  # Field name made lowercase.
    board = models.CharField(db_column='Board', max_length=45, blank=True, null=True)  # Field name made lowercase.
    shariah = models.CharField(db_column='Shariah', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subsector = models.CharField(db_column='SubSector', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CorporateInfo'


class Financialinfo(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    marketcap = models.BigIntegerField(db_column='MarketCap', blank=True, null=True)  # Field name made lowercase.
    numshares = models.BigIntegerField(db_column='NumShares', blank=True, null=True)  # Field name made lowercase.
    eps = models.FloatField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    peratio = models.FloatField(db_column='PERatio', blank=True, null=True)  # Field name made lowercase.
    roeratio = models.FloatField(db_column='ROERatio', blank=True, null=True)  # Field name made lowercase.
    dividend = models.FloatField(db_column='Dividend', blank=True, null=True)  # Field name made lowercase.
    dividendyield = models.FloatField(db_column='DividendYield', blank=True, null=True)  # Field name made lowercase.
    dividendpolicy = models.FloatField(db_column='DividendPolicy', blank=True, null=True)  # Field name made lowercase.
    nta = models.FloatField(db_column='NTA', blank=True, null=True)  # Field name made lowercase.
    parvalue = models.FloatField(db_column='PARValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialInfo'
        unique_together = (('counterfullid', 'tradedate'),)


class Marketoverview(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    marketcap = models.BigIntegerField(db_column='MarketCap', blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subsector = models.CharField(db_column='SubSector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    turnover1day = models.DecimalField(db_column='TurnOver1Day', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    validmoneyflow5days = models.IntegerField(db_column='ValidMoneyFlow5Days', blank=True, null=True)  # Field name made lowercase.
    moneyflow5days = models.DecimalField(db_column='MoneyFlow5Days', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    validmoneyflow15days = models.IntegerField(db_column='ValidMoneyFlow15Days', blank=True, null=True)  # Field name made lowercase.
    moneyflow15days = models.DecimalField(db_column='MoneyFlow15Days', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    moneyflowin5days = models.DecimalField(db_column='MoneyFlowIn5Days', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    moneyflowout5days = models.DecimalField(db_column='MoneyFlowOut5Days', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    moneyflowin15days = models.DecimalField(db_column='MoneyFlowIn15Days', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    moneyflowout15days = models.DecimalField(db_column='MoneyFlowOut15Days', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketOverview'
        unique_together = (('tradedate', 'counterfullid'),)


class Moneyflow(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    moneyflowin = models.FloatField(db_column='MoneyFlowIn', blank=True, null=True)  # Field name made lowercase.
    moneyflowout = models.FloatField(db_column='MoneyFlowOut', blank=True, null=True)  # Field name made lowercase.
    netmoneyflow = models.FloatField(db_column='NetMoneyFlow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MoneyFlow'
        unique_together = (('counterfullid', 'tradedate'),)


class Ownership(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=455, blank=True, null=True)  # Field name made lowercase.
    numshares = models.BigIntegerField(db_column='NumShares', blank=True, null=True)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.
    sharesworth = models.BigIntegerField(db_column='SharesWorth', blank=True, null=True)  # Field name made lowercase.
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ownership'
        unique_together = (('rank', 'tradedate', 'counterfullid'),)


class Tradesummary(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    trades = models.IntegerField(db_column='Trades', blank=True, null=True)  # Field name made lowercase.
    buyup = models.IntegerField(db_column='BuyUp', blank=True, null=True)  # Field name made lowercase.
    mid = models.IntegerField(db_column='Mid', blank=True, null=True)  # Field name made lowercase.
    selldown = models.IntegerField(db_column='Selldown', blank=True, null=True)  # Field name made lowercase.
    preopen = models.IntegerField(db_column='Preopen', blank=True, null=True)  # Field name made lowercase.
    preclose = models.IntegerField(db_column='Preclose', blank=True, null=True)  # Field name made lowercase.
    unknown = models.IntegerField(db_column='Unknown', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    isempty = models.IntegerField(db_column='IsEmpty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TradeSummary'
        unique_together = (('tradedate', 'counterfullid', 'price'),)


class Tradesummaryprogress(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TradeSummaryProgress'


class Turnover(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    totalturnover = models.FloatField(db_column='TotalTurnOver', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TurnOver'
        unique_together = (('counterfullid', 'tradedate'),)


class Arcsvtable(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    b30 = models.IntegerField(blank=True, null=True)
    bthirty = models.IntegerField(db_column='bThirty', blank=True, null=True)  # Field name made lowercase.
    csvfullpath = models.CharField(db_column='csvfullPath', max_length=555, blank=True, null=True)  # Field name made lowercase.
    bdepositor = models.IntegerField(db_column='bDepositor', blank=True, null=True)  # Field name made lowercase.
    bholder = models.IntegerField(db_column='bHolder', blank=True, null=True)  # Field name made lowercase.
    bshareholder = models.IntegerField(db_column='bShareholder', blank=True, null=True)  # Field name made lowercase.
    linenum = models.IntegerField(db_column='lineNum', blank=True, null=True)  # Field name made lowercase.
    linetext = models.CharField(db_column='lineText', max_length=555, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'arcsvtable'


class Arhreftable(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    href = models.CharField(max_length=555, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arhreftable'
        unique_together = (('counterfullid', 'year'),)


class Arpdfinfo(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    pages = models.CharField(max_length=555, blank=True, null=True)
    fullpdfpath = models.CharField(max_length=555, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arpdfinfo'
        unique_together = (('counterfullid', 'year'),)


class Arprogress(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    arcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arprogress'
        unique_together = (('counterfullid', 'year'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Balancesheettable(models.Model):
    fullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    cashsecurities = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    stocks = models.IntegerField(blank=True, null=True)
    debtors = models.IntegerField(blank=True, null=True)
    otherassets = models.IntegerField(blank=True, null=True)
    totalcurrentassets = models.IntegerField(blank=True, null=True)
    shorttermloans = models.IntegerField(blank=True, null=True)
    creditors = models.IntegerField(blank=True, null=True)
    taxation = models.IntegerField(blank=True, null=True)
    dividends = models.IntegerField(blank=True, null=True)
    otherliabilities = models.IntegerField(blank=True, null=True)
    totalcurrentliabilities = models.IntegerField(blank=True, null=True)
    netcurrentassets = models.IntegerField(blank=True, null=True)
    landbuilding = models.IntegerField(blank=True, null=True)
    plantmachinery = models.IntegerField(blank=True, null=True)
    investments = models.IntegerField(blank=True, null=True)
    intangibleassets = models.IntegerField(blank=True, null=True)
    totallongtermassets = models.IntegerField(blank=True, null=True)
    paidupcapital = models.IntegerField(blank=True, null=True)
    sharepremium = models.IntegerField(blank=True, null=True)
    accumulatedearnings = models.IntegerField(blank=True, null=True)
    otherreserves = models.IntegerField(blank=True, null=True)
    totalshareholdersfund = models.IntegerField(blank=True, null=True)
    minorityinterest = models.IntegerField(blank=True, null=True)
    totallongtermliabilities = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balancesheettable'


class Bonushistory(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    exdate = models.DateTimeField(blank=True, null=True)
    entitledate = models.DateTimeField(blank=True, null=True)
    transferdate = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=35)
    ratio = models.CharField(max_length=8, blank=True, null=True)
    rightissueprice = models.FloatField(blank=True, null=True)
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid')

    class Meta:
        managed = False
        db_table = 'bonushistory'


class Buyqueue(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    volstr = models.CharField(max_length=45, blank=True, null=True)
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyqueue'


class Cashflowtable(models.Model):
    year = models.IntegerField(blank=True, null=True)
    fullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    operatingactivities = models.IntegerField(blank=True, null=True)
    investingactivities = models.IntegerField(blank=True, null=True)
    financialactivities = models.IntegerField(blank=True, null=True)
    netcash = models.IntegerField(blank=True, null=True)
    cashbf = models.IntegerField(blank=True, null=True)
    cashbankbalance = models.IntegerField(blank=True, null=True)
    deposits = models.IntegerField(blank=True, null=True)
    overdraft = models.IntegerField(blank=True, null=True)
    cashcf = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cashflowtable'


class Counters(models.Model):
    name = models.CharField(max_length=55)
    symbol = models.CharField(max_length=55)
    type = models.CharField(max_length=45, blank=True, null=True)
    fullid = models.CharField(primary_key=True, max_length=55)
    category = models.CharField(max_length=45, blank=True, null=True)
    fullname = models.CharField(max_length=355, blank=True, null=True)
    sector = models.CharField(max_length=95, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counters'


class Distshareholdingstable(models.Model):
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    leveltype = models.IntegerField(blank=True, null=True)
    levelname = models.CharField(max_length=355, blank=True, null=True)
    numshareholders = models.IntegerField(blank=True, null=True)
    numshares = models.BigIntegerField(blank=True, null=True)
    financialyear = models.IntegerField(blank=True, null=True)
    sharespercentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distshareholdingstable'


class Dividendhistory(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    finyear = models.DateTimeField(blank=True, null=True)
    exdate = models.DateTimeField(blank=True, null=True)
    entitleddate = models.DateTimeField(blank=True, null=True)
    paymentdate = models.DateTimeField(blank=True, null=True)
    entitletype = models.CharField(max_length=75)
    dividendcent = models.FloatField(blank=True, null=True)
    dividendpercent = models.FloatField(blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid')

    class Meta:
        managed = False
        db_table = 'dividendhistory'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Dynamicbox(models.Model):
    fromdate = models.DateTimeField(blank=True, null=True)
    todate = models.DateTimeField(blank=True, null=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    lowestlow = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    highesthigh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamicbox'


class Dynamicboxbreakout(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    breakoutcompare = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamicboxbreakout'


class Technicals(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    volumechangepct = models.FloatField(db_column='volumeChangePct', blank=True, null=True)  # Field name made lowercase.
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    sma20 = models.FloatField(db_column='Sma20', blank=True, null=True)  # Field name made lowercase.
    sma50 = models.FloatField(db_column='Sma50', blank=True, null=True)  # Field name made lowercase.
    rsi14 = models.FloatField(db_column='Rsi14', blank=True, null=True)  # Field name made lowercase.
    vwap14 = models.FloatField(blank=True, null=True)
    atr14 = models.FloatField(blank=True, null=True)
    hasgap = models.IntegerField(db_column='hasGap', blank=True, null=True)  # Field name made lowercase.
    gappct = models.FloatField(db_column='gapPct', blank=True, null=True)  # Field name made lowercase.
    hasvwap = models.IntegerField(db_column='hasVWAP', blank=True, null=True)  # Field name made lowercase.
    hasrsi = models.IntegerField(db_column='hasRSI', blank=True, null=True)  # Field name made lowercase.
    hasunusualvolume = models.IntegerField(db_column='hasUnusualVolume', blank=True, null=True)  # Field name made lowercase.
    sma20compare = models.FloatField(db_column='Sma20Compare', blank=True, null=True)  # Field name made lowercase.
    sma50compare = models.FloatField(db_column='Sma50Compare', blank=True, null=True)  # Field name made lowercase.
    sma20sma50diff = models.FloatField(db_column='Sma20Sma50Diff', blank=True, null=True)  # Field name made lowercase.
    changedprice = models.FloatField(db_column='ChangedPrice', blank=True, null=True)  # Field name made lowercase.
    changedpct = models.FloatField(db_column='ChangedPCT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Technicals'
        unique_together = (('counterfullid', 'tradedate'),)


class Eodtable(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(blank=True, null=True)
    open = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    high = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    low = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    close = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eodtable'
        unique_together = (('counterfullid', 'datetime'),)

class Securityoverview(models.Model):
    symbol = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    year = models.IntegerField(blank=True, null=True)
    top30shares = models.BigIntegerField(blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.CharField(max_length=55, blank=True, null=True)
    marketcap = models.BigIntegerField(db_column='MarketCap', blank=True, null=True)  # Field name made lowercase.
    numshares = models.BigIntegerField(db_column='NumShares', blank=True, null=True)  # Field name made lowercase.
    eps = models.FloatField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    peratio = models.FloatField(db_column='PERatio', blank=True, null=True)  # Field name made lowercase.
    roeratio = models.FloatField(db_column='ROERatio', blank=True, null=True)  # Field name made lowercase.
    dividend = models.FloatField(db_column='Dividend', blank=True, null=True)  # Field name made lowercase.
    dividendyield = models.FloatField(db_column='DividendYield', blank=True, null=True)  # Field name made lowercase.
    dividendpolicy = models.FloatField(db_column='DividendPolicy', blank=True, null=True)  # Field name made lowercase.
    nta = models.FloatField(db_column='NTA', blank=True, null=True)  # Field name made lowercase.
    parvalue = models.FloatField(db_column='ParValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecurityOverview'

class Fininfo(models.Model):
    marketcap = models.CharField(max_length=15, blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid')
    numshare = models.CharField(max_length=15, blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    peratio = models.FloatField(blank=True, null=True)
    roe = models.FloatField(blank=True, null=True)
    dividendcent = models.FloatField(blank=True, null=True)
    dividendyield = models.FloatField(blank=True, null=True)
    nta = models.FloatField(blank=True, null=True)
    parvalue = models.FloatField(blank=True, null=True)
    dividentpolicy = models.FloatField(blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=85, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fininfo'


class Highlist(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'highlist'


class Holdingstrialtable(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    linestart = models.IntegerField(blank=True, null=True)
    lineend = models.IntegerField(blank=True, null=True)
    file = models.CharField(max_length=455, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holdingstrialtable'


class Lastdone(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    typestr = models.CharField(db_column='typeStr', max_length=55, blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    turnover = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lastdone'


class Lowlist(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lowlist'


class Marketsummary(models.Model):
    marketname = models.CharField(max_length=50, blank=True, null=True)
    highcount = models.IntegerField(blank=True, null=True)
    lowcount = models.IntegerField(blank=True, null=True)
    dtime = models.DateTimeField(db_column='dTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marketSummary'


class Marketdepth(models.Model):
    stockid = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    isbid = models.IntegerField(db_column='isBid', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    hash = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketdepth'


class Msiawarrantsmapping(models.Model):
    underlyingname = models.CharField(unique=True, max_length=55, blank=True, null=True)
    counterfullid = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msiawarrantsmapping'


class Newhightable(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    newhighdays = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newhightable'


class Newlowtable(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    newlowdays = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newlowtable'


class Nomineestable(models.Model):
    nomineename = models.CharField(max_length=255, blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    numshares = models.IntegerField(blank=True, null=True)
    holderid = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomineestable'


class Obv(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    obv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obv'


class Oppa(models.Model):
    linetext = models.CharField(db_column='lineText', max_length=555, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oppa'


class Profitlosstable(models.Model):
    year = models.IntegerField(blank=True, null=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    operatingprofit = models.IntegerField(blank=True, null=True)
    profitlossbeforetax = models.IntegerField(blank=True, null=True)
    shareholdernetprofitloss = models.IntegerField(blank=True, null=True)
    basiceps = models.FloatField(blank=True, null=True)
    grossdividend = models.FloatField(blank=True, null=True)
    depreciation = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    taxation = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profitlosstable'


class Progresstable(models.Model):
    quarterreport = models.IntegerField(blank=True, null=True)
    quartercount = models.IntegerField(blank=True, null=True)
    dividendhistory = models.IntegerField(blank=True, null=True)
    dividendcount = models.IntegerField(blank=True, null=True)
    bonushistory = models.IntegerField(blank=True, null=True)
    bonuscount = models.IntegerField(blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid')
    fundamentalinfo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'progresstable'


class Quarterlies(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    quarter = models.CharField(max_length=45, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    turnover = models.BigIntegerField(blank=True, null=True)
    profitbeforetax = models.IntegerField(blank=True, null=True)
    netprofit = models.IntegerField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    dividendcurrency = models.CharField(max_length=5, blank=True, null=True)
    dps = models.FloatField(blank=True, null=True)
    specialdps = models.FloatField(blank=True, null=True)
    quarterdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quarterlies'


class Gainersloserstable(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    pricechange = models.FloatField(db_column='PriceChange', blank=True, null=True)  # Field name made lowercase.
    pricechangepct = models.FloatField(db_column='PriceChangePCT', blank=True, null=True)  # Field name made lowercase.
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GainersLosersTable'
        unique_together = (('counterfullid', 'tradedate'),)

class Eodtableview(models.Model):

    symbol = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.CharField(max_length=55, blank=True, null=True)
    close = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    high = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    low = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    open = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EODTableView'


class Rsitable(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    rsi = models.FloatField(db_column='Rsi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RsiTable'
        unique_together = (('tradedate', 'counterfullid'),)

class Reporthistory(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    finyear = models.DateTimeField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    finquarter = models.DateTimeField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    pbt = models.IntegerField(blank=True, null=True)
    netprofit = models.IntegerField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    dividend = models.FloatField(blank=True, null=True)
    nta = models.FloatField(blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid')

    class Meta:
        managed = False
        db_table = 'reporthistory'


class Round2Table(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    holderid = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=455, blank=True, null=True)
    numshare = models.BigIntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    fullcsvpath = models.CharField(max_length=45, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'round2table'


class Scrapeprogresstable(models.Model):
    fullid = models.CharField(max_length=55, blank=True, null=True)
    stockdate = models.DateTimeField(db_column='stockDate', blank=True, null=True)  # Field name made lowercase.
    progress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrapeprogresstable'

class Screenerview(models.Model):
    name = models.CharField(max_length=55)
    symbol = models.CharField(max_length=55)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.CharField(max_length=55, blank=True, null=True)
    close = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    marketcap = models.BigIntegerField(db_column='MarketCap', blank=True, null=True)  # Field name made lowercase.
    numshares = models.BigIntegerField(db_column='NumShares', blank=True, null=True)  # Field name made lowercase.
    eps = models.FloatField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    peratio = models.FloatField(db_column='PERatio', blank=True, null=True)  # Field name made lowercase.
    roeratio = models.FloatField(db_column='ROERatio', blank=True, null=True)  # Field name made lowercase.
    dividend = models.FloatField(db_column='Dividend', blank=True, null=True)  # Field name made lowercase.
    dividendyield = models.FloatField(db_column='DividendYield', blank=True, null=True)  # Field name made lowercase.
    dividendpolicy = models.FloatField(db_column='DividendPolicy', blank=True, null=True)  # Field name made lowercase.
    nta = models.FloatField(db_column='NTA', blank=True, null=True)  # Field name made lowercase.
    parvalue = models.FloatField(db_column='ParValue', blank=True, null=True)  # Field name made lowercase.
    sma20 = models.FloatField(blank=True, null=True)
    sma50 = models.FloatField(db_column='Sma50', blank=True, null=True)  # Field name made lowercase.
    rsi14 = models.FloatField(db_column='Rsi14', blank=True, null=True)  # Field name made lowercase.
    vwap14 = models.FloatField(blank=True, null=True)
    atr14 = models.FloatField(blank=True, null=True)
    hasgap = models.IntegerField(db_column='hasGap', blank=True, null=True)  # Field name made lowercase.
    gappct = models.FloatField(db_column='gapPct', blank=True, null=True)  # Field name made lowercase.
    hasvwap = models.IntegerField(db_column='hasVWAP', blank=True, null=True)  # Field name made lowercase.
    hasrsi = models.IntegerField(db_column='hasRSI', blank=True, null=True)  # Field name made lowercase.
    hasunusualvolume = models.IntegerField(db_column='hasUnusualVolume', blank=True, null=True)  # Field name made lowercase.
    volumechangepct = models.FloatField(blank=True, null=True)
    sma20compare = models.FloatField(db_column='Sma20compare', blank=True, null=True)  # Field name made lowercase.
    sma50compare = models.FloatField(db_column='Sma50Compare', blank=True, null=True)  # Field name made lowercase.
    sma20sma50diff = models.FloatField(db_column='Sma20Sma50Diff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScreenerView'


class Securitysummary(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    rsi14 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    number_52wkhigh = models.DecimalField(db_column='52wkhigh', max_digits=10, decimal_places=3, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_52wklow = models.DecimalField(db_column='52wklow', max_digits=10, decimal_places=3, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    averagevol3months = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'securitysummary'


class Sellqueue(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    volstr = models.CharField(max_length=45, blank=True, null=True)
    counterfullid = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellqueue'


class Shareholderdatasummary(models.Model):
    reportyear = models.IntegerField(blank=True, null=True)
    reportdate = models.DateField(blank=True, null=True)
    done = models.IntegerField(blank=True, null=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shareholderdatasummary'


class Shareholderstable(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    holderid = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=455, blank=True, null=True)
    numshare = models.BigIntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    fullcsvpath = models.CharField(max_length=45, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shareholderstable'


class Shareholdingsummary(models.Model):
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    outstandingshares = models.BigIntegerField(blank=True, null=True)
    top30shares = models.BigIntegerField(blank=True, null=True)
    floatpercentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    floatshares = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shareholdingsummary'


class Staticbox(models.Model):
    fromdate = models.DateTimeField(blank=True, null=True)
    todate = models.DateTimeField(blank=True, null=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    lowestlow = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    highesthigh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staticbox'


class Staticboxbreakout(models.Model):
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    breakoutcompare = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staticboxbreakout'


class Table29A(models.Model):
    announceid = models.BigIntegerField(primary_key=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    companyno = models.CharField(max_length=45, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    dateinterestacquired = models.DateTimeField(blank=True, null=True)
    numsecurities = models.IntegerField(blank=True, null=True)
    circumstances = models.CharField(max_length=999, blank=True, null=True)
    natureofinterest = models.CharField(max_length=255, blank=True, null=True)
    directunits = models.IntegerField(blank=True, null=True)
    directpercent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    indirectunits = models.IntegerField(blank=True, null=True)
    indirectpercent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dateofnotice = models.DateTimeField(blank=True, null=True)
    datenoticereceived = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table29a'


class Table29B(models.Model):
    announceid = models.IntegerField(primary_key=True)
    fullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='fullid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    companyno = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=555, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    circumstances = models.CharField(max_length=555, blank=True, null=True)
    natureofinterest = models.CharField(max_length=255, blank=True, null=True)
    directunits = models.IntegerField(blank=True, null=True)
    directpercent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    indirectunits = models.IntegerField(blank=True, null=True)
    indirectpercent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    securitiesafterchange = models.BigIntegerField(blank=True, null=True)
    dateofnotice = models.DateTimeField(blank=True, null=True)
    dateannounced = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table29b'


class Topgainers(models.Model):
    pricediff = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    beforeprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    currentprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topgainers'


class Topgainerspct(models.Model):
    percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    beforeprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    currentprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topgainerspct'


class Toplosers(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    pricediff = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    beforeprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    currentprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toplosers'


class Toploserspct(models.Model):
    percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    beforeprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    currentprice = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toploserspct'


class Trackerholderstable(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    holderid = models.IntegerField(blank=True, null=True)
    detailname = models.CharField(max_length=455, blank=True, null=True)
    shares = models.BigIntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    nominees = models.CharField(max_length=165, blank=True, null=True)
    remarks = models.CharField(max_length=165, blank=True, null=True)
    displayname = models.CharField(max_length=455, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trackerholderstable'


class Tradingdays(models.Model):
    tradingdate = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tradingdays'
        unique_together = (('country', 'tradingdate'),)


class Unusualvolume(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    pastaveragevolume = models.IntegerField(blank=True, null=True)
    ratio = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    currentdayvolume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unusualvolume'


class Updateddatelist(models.Model):
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'updateddatelist'


class Vwap10(models.Model):
    vwap10 = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vwap10'


class Warrantinfo(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    underlying = models.ForeignKey(Msiawarrantsmapping, models.DO_NOTHING, db_column='underlying', blank=True, null=True)
    deltapct = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    deltaperwarrantpct = models.FloatField(blank=True, null=True)
    issuer = models.CharField(max_length=255, blank=True, null=True)
    sensitivity = models.CharField(max_length=45, blank=True, null=True)
    exerciseprice = models.FloatField(blank=True, null=True)
    premiumpct = models.FloatField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    impliedvolatilitypct = models.FloatField(blank=True, null=True)
    thetapct = models.FloatField(blank=True, null=True)
    intrinsicvalueperwarrant = models.CharField(max_length=45, blank=True, null=True)
    exerciseratio = models.FloatField(blank=True, null=True)
    moneyness = models.CharField(max_length=45, blank=True, null=True)
    effectivegearing = models.FloatField(blank=True, null=True)
    breakevenpriceatexpiry = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warrantinfo'

class Arimaforecast(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    forecastdate = models.DateTimeField(db_column='ForecastDate', blank=True, null=True)  # Field name made lowercase.
    p = models.IntegerField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    q = models.IntegerField(db_column='Q', blank=True, null=True)  # Field name made lowercase.
    lower80 = models.FloatField(db_column='Lower80', blank=True, null=True)  # Field name made lowercase.
    upper80 = models.FloatField(db_column='Upper80', blank=True, null=True)  # Field name made lowercase.
    lower95 = models.FloatField(db_column='Lower95', blank=True, null=True)  # Field name made lowercase.
    upper95 = models.FloatField(db_column='Upper95', blank=True, null=True)  # Field name made lowercase.
    pointforecast = models.FloatField(db_column='PointForecast', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArimaForecast'
        unique_together = (('counterfullid', 'tradedate', 'forecastdate'),)

class Arimaforecastview(models.Model):
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    forecastdate = models.DateTimeField(db_column='ForecastDate', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.CharField(max_length=55, blank=True, null=True)
    sector = models.CharField(db_column='Sector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=55, blank=True, null=True)  # Field name made lowercase.
    pointforecast = models.FloatField(db_column='PointForecast', blank=True, null=True)  # Field name made lowercase.
    forecaststate = models.IntegerField(db_column='ForecastState', blank=True, null=True)  # Field name made lowercase.
    lower80 = models.FloatField(db_column='Lower80', blank=True, null=True)  # Field name made lowercase.
    upper80 = models.FloatField(db_column='Upper80', blank=True, null=True)  # Field name made lowercase.
    lower95 = models.FloatField(db_column='Lower95', blank=True, null=True)  # Field name made lowercase.
    upper95 = models.FloatField(db_column='Upper95', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArimaForecastView'

class Arimaforecastaccuracy(models.Model):
    closeaccuracy80 = models.IntegerField(db_column='CloseAccuracy80', blank=True, null=True)  # Field name made lowercase.
    highaccuracy80 = models.IntegerField(db_column='HighAccuracy80', blank=True, null=True)  # Field name made lowercase.
    lowaccuracy80 = models.IntegerField(db_column='LowAccuracy80', blank=True, null=True)  # Field name made lowercase.
    closeaccuracy95 = models.IntegerField(db_column='CloseAccuracy95', blank=True, null=True)  # Field name made lowercase.
    highaccuracy95 = models.IntegerField(db_column='HighAccuracy95', blank=True, null=True)  # Field name made lowercase.
    lowaccuracy95 = models.IntegerField(db_column='LowAccuracy95', blank=True, null=True)  # Field name made lowercase.
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArimaForecastAccuracy'
        unique_together = (('tradedate', 'counterfullid'),)

class Activecounters(models.Model):
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActiveCounters'
        unique_together = (('tradedate', 'counterfullid'),)


class Warrantprogresstable(models.Model):
    counterfullid = models.ForeignKey(Counters, models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    done = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warrantprogresstable'


class Candlestickspattern(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    bearishabandonedbaby = models.IntegerField(db_column='BearishAbandonedBaby', blank=True, null=True)  # Field name made lowercase.
    bearishengulfingpattern = models.IntegerField(db_column='BearishEngulfingPattern', blank=True, null=True)  # Field name made lowercase.
    bearishharami = models.IntegerField(db_column='BearishHarami', blank=True, null=True)  # Field name made lowercase.
    bearishlongday = models.IntegerField(db_column='BearishLongDay', blank=True, null=True)  # Field name made lowercase.
    bearishshortday = models.IntegerField(db_column='BearishShortDay', blank=True, null=True)  # Field name made lowercase.
    bullishabandonedbaby = models.IntegerField(db_column='BullishAbandonedBaby', blank=True, null=True)  # Field name made lowercase.
    bullishengulfingpattern = models.IntegerField(db_column='BullishEngulfingPattern', blank=True, null=True)  # Field name made lowercase.
    bullishharami = models.IntegerField(db_column='BullishHarami', blank=True, null=True)  # Field name made lowercase.
    bullishlongday = models.IntegerField(db_column='BullishLongDay', blank=True, null=True)  # Field name made lowercase.
    bullishshortday = models.IntegerField(db_column='BullishShortDay', blank=True, null=True)  # Field name made lowercase.
    darkcloudcover = models.IntegerField(db_column='DarkCloudCover', blank=True, null=True)  # Field name made lowercase.
    doji = models.IntegerField(db_column='Doji', blank=True, null=True)  # Field name made lowercase.
    downtrend = models.IntegerField(db_column='DownTrend', blank=True, null=True)  # Field name made lowercase.
    downsidetasukigap = models.IntegerField(db_column='DownsideTasukiGap', blank=True, null=True)  # Field name made lowercase.
    dragonifydoji = models.IntegerField(db_column='DragonifyDoji', blank=True, null=True)  # Field name made lowercase.
    eveningdojistar = models.IntegerField(db_column='EveningDojiStar', blank=True, null=True)  # Field name made lowercase.
    eveningstar = models.IntegerField(db_column='EveningStar', blank=True, null=True)  # Field name made lowercase.
    fallingthreemethods = models.IntegerField(db_column='FallingThreeMethods', blank=True, null=True)  # Field name made lowercase.
    gravestonedoji = models.IntegerField(db_column='GravestoneDoji', blank=True, null=True)  # Field name made lowercase.
    longday = models.IntegerField(db_column='LongDay', blank=True, null=True)  # Field name made lowercase.
    longlowershadow = models.IntegerField(db_column='LongLowerShadow', blank=True, null=True)  # Field name made lowercase.
    longuppershadow = models.IntegerField(db_column='LongUpperShadow', blank=True, null=True)  # Field name made lowercase.
    morningdojistar = models.IntegerField(db_column='MorningDojiStar', blank=True, null=True)  # Field name made lowercase.
    morningstar = models.IntegerField(db_column='MorningStar', blank=True, null=True)  # Field name made lowercase.
    risingthreemethods = models.IntegerField(db_column='RisingThreeMethods', blank=True, null=True)  # Field name made lowercase.
    shortday = models.IntegerField(db_column='ShortDay', blank=True, null=True)  # Field name made lowercase.
    uptrend = models.IntegerField(db_column='UpTrend', blank=True, null=True)  # Field name made lowercase.
    upsidetasukigap = models.IntegerField(db_column='UpsideTasukiGap', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CandleSticksPattern'
        unique_together = (('counterfullid', 'tradedate'),)


class Bullishbearish(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    isbullish = models.IntegerField(db_column='IsBullish', blank=True, null=True)  # Field name made lowercase.
    isbearish = models.IntegerField(db_column='IsBearish', blank=True, null=True)  # Field name made lowercase.
    isaccumdistbullish = models.IntegerField(db_column='IsAccumDistBullish', blank=True, null=True)  # Field name made lowercase.
    isaccumdistbearish = models.IntegerField(db_column='IsAccumDistBearish', blank=True, null=True)  # Field name made lowercase.
    isobvbullish = models.IntegerField(db_column='IsObvBullish', blank=True, null=True)  # Field name made lowercase.
    isobvbearish = models.IntegerField(db_column='IsObvBearish', blank=True, null=True)  # Field name made lowercase.
    issmabullish = models.IntegerField(db_column='IsSMABullish', blank=True, null=True)  # Field name made lowercase.
    issmabearish = models.IntegerField(db_column='IsSMABearish', blank=True, null=True)  # Field name made lowercase.
    issmaoscbullish = models.IntegerField(db_column='IsSmaOscBullish', blank=True, null=True)  # Field name made lowercase.
    issmaoscbearish = models.IntegerField(db_column='IsSmaOscBearish', blank=True, null=True)  # Field name made lowercase.
    isemabullish = models.IntegerField(db_column='IsEMABullish', blank=True, null=True)  # Field name made lowercase.
    isemabearish = models.IntegerField(db_column='IsEMABearish', blank=True, null=True)  # Field name made lowercase.
    isemaoscbullish = models.IntegerField(db_column='IsEmaOscBullish', blank=True, null=True)  # Field name made lowercase.
    isemaoscbearish = models.IntegerField(db_column='IsEmaOscBearish', blank=True, null=True)  # Field name made lowercase.
    ismacdbullishcross = models.IntegerField(db_column='IsMACDBullishCross', blank=True, null=True)  # Field name made lowercase.
    ismacdbearishcross = models.IntegerField(db_column='IsMACDBearishCross', blank=True, null=True)  # Field name made lowercase.
    isfaststooscbullish = models.IntegerField(db_column='IsFastStoOscBullish', blank=True, null=True)  # Field name made lowercase.
    isfaststooscbearish = models.IntegerField(db_column='IsFastStoOscBearish', blank=True, null=True)  # Field name made lowercase.
    isfullstooscbullish = models.IntegerField(db_column='IsFullStoOscBullish', blank=True, null=True)  # Field name made lowercase.
    isfullstooscbearish = models.IntegerField(db_column='IsFullStoOscBearish', blank=True, null=True)  # Field name made lowercase.
    isslowstooscbullish = models.IntegerField(db_column='IsSlowStoOscBullish', blank=True, null=True)  # Field name made lowercase.
    isslowstooscbearish = models.IntegerField(db_column='IsSlowStoOscBearish', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BullishBearish'
        unique_together = (('counterfullid', 'tradedate'),)


class Bullishbearishsummary(models.Model):
    counterfullid = models.ForeignKey('Counters', models.DO_NOTHING, db_column='counterfullid', blank=True, null=True)
    tradedate = models.DateTimeField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    bullishcount = models.IntegerField(db_column='BullishCount', blank=True, null=True)  # Field name made lowercase.
    bearishcount = models.IntegerField(db_column='BearishCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BullishBearishSummary'
        unique_together = (('counterfullid', 'tradedate'),)
