from enum import Enum
from lightstreamer.client import Subscription

class PishroApiWebUrl(Enum):
    GET_ACCOUNTING_REMAIN = '/Web/V1/Accounting/Remain'
    GET_CLIENT_SIDE_ALERT = '/Web/V1/Symbol/GetClientSideAlert'
    GET_OPEN_ORDER = '/Web/V1/Order/GetOpenOrder/OpenOrder'
    GET_CUSTOMER_TODAY_ORDERS = '/Web/V1/Order/GetTodayOrders/Customer/GetCustomerTodayOrders'
    GET_CUSTOMER_TRADES = '/Web/V1/Order/GetCustomerTrades/Customer/GetCustomerTrades'
    GET_ORDER_LIST = '/Web/V1/Order/GetOrderList/Customer/GetOrderList'

    DELETE_ORDER = '/Web/V1/Order/Delete'
    UPDATE_ORDER = '/Web/V1/Order/PUT'
    SEND_MULTIPLE_ORDERS = '/Web/V1/Order/SendMultipleOrders'

    GET_DAILY_CUSTOMER_STOCK_PORTFOLIO = '/Web/V1/DailyPortfolio/Get/DailyPortfolio'

    GET_WATCH_LIST_ROW = '/Web/V1/WatchListRow/Get'
    ADD_ISIN_TO_WATCH_LIST_CATEGORY = '/Web/V1/WatchListRow/Post'

    GET_SYMBOL = '/Web/V1/Symbol/GetSymbol'
    GET_SYMBOL_V2 = '/Web/V2/Symbol/GetSymbol'

    DELETE_ISIN_FROM_WATCH_LIST_ROW = '/Web/V1/WatchListRow/Delete'
    GET_CUSTOMER_ACCOUNT = '/Web/V1/Accounting/GetCustomerAccount'
    GET_WATCH_LIST_CATEGORY = '/Web/V1/WatchListCategory/Get'
    CREATE_WATCH_LIST_CATEGORY = '/Web/V1/WatchListCategory/POST'
    DELETE_WATCH_LIST_CATEGORY = '/Web/V1/WatchListCategory/Delete'
    UPDATE_WATCH_LIST_CATEGORY = '/Web/V1/WatchListCategory/Put'

    GET_REMAIN_ASSET = '/Web/V1/DailyPortfolio/GetRemainAsset/GetRemainAsset'
    GET_CUSTOMER_OPTION_POSITION_COUNT = '/Web/V2/Customer/GetCustomerOptionPositionCount'
    GET_CUSTOMER_FUTURE_POSITION_COUNT = '/Web/V1/TseFuture/GetCustomerFuturePositionCount'
    GET_FAIR_PRICE_PARAMETERS = '/Web/V1/Conf/FairPriceParameters'
    GET_REALTIME_PORTFOLIO = '/Web/V1/RealtimePortfolio/Get/RealtimePortfolio'
    GET_CUSTOMER_CHANGED_BROKERS = '/Web/V1/RealtimePortfolio/GetCustomerChangedBrokers'

    CONFIRM_CUSTOMER_CHANGED_BROKER = '/Web/V1/RealtimePortfolio/ConfirmCustomerChangedBroker'
    IGNORE_CUSTOMER_CHANGED_BROKER = '/Web/V1/RealtimePortfolio/IgnoreCustomerChangedBroker'
    GET_ACTIVE_AGREEMENT_LIST = '/Web/V1/Agreement/GetActiveAgreementList'
    ACCEPT_AGREEMENT = '/Web/V1/Agreement/AcceptAgreement'
    CHANGE_AGREEMENT_STATE = '/Web/V1/Agreement/ChangeAgreementState'
    CHECK_AGREEMENT = '/Web/V1/Agreement/CheckAgreement'
    GET_AGREEMENT = '/Web/V1/Agreement/GetAgreement'
    DELETE_REALTIME_PORTFOLIO_ROW = '/Web/V1/RealtimePortfolio/Delete'
    DELETE_REALTIME_PORTFOLIO_ROWS = '/Web/V1/RealtimePortfolio/DeleteRows'
    DELETE_REALTIME_PORTFOLIO_MULTIPLE_DETAIL_RECORDS = '/Web/V1/RealtimePortfolio/DeleteMultipleDetailRecords'
    CREATE_REALTIME_PORTFOLIO_ROW = '/Web/V1/RealtimePortfolio/Post/RealtimePortfolio'
    GET_MESSAGES = '/Web/V1/Message/Get/Messages'
    PUT_MESSAGES_BATCH_LIST = '/Web/V1/Message/PutBatchList/Messages/BatchList'
    GET_CSD_PORTFOLIO_LIST = '/Web/V1/DailyPortfolio/GetCSDPortfolioList'
    GET_SUPERVISOR_MESSAGE_FOR_HEADER = '/Web/V1/Message/GetSupervisorMessageForHeader'
    GET_SUPERVISOR_MESSAGE = '/Web/V1/Message/GetSupervisorMessage'
    ACCOUNT_TRANSACTION = '/Web/V1/AccountTransaction/Post/AccountTransaction'
    SEND_ORDER = '/Web/V1/Order/Post'
    ORDER_DETAIL = '/Web/V1/Order/GetOrderDetails/Detail'
    UPDATE_MULTIPLE_ORDERS = '/Web/V1/Order/UpdateMultipleOrders'
    GET_CUSTOMER_OFFLINE_ORDERS_HISTORY = '/Web/V1/OfflineOrders/GetCustomerOfflineOrdersHistory'
    GET_CUSTOMER_OFFLINE_ORDERS = '/Web/V1/OfflineOrders/GetCustomerOfflineOrders'
    ADD_OFFLINE_ORDER = '/Web/V1/OfflineOrders/AddOfflineOrder'
    DELETE_OFFLINE_ORDER = '/Web/V1/OfflineOrders/DeleteOfflineOrder'
    GET_IPO_SYMBOLS = '/Web/V1/Symbol/GetIpoSymbols/IpoSymbols'
    IS_EXIST_IPO_SYMBOLS = '/Web/V1/Symbol/IsExistIpoSymbols'
    GET_CUSTOMER_OPTION_CONTRACT_SETTLEMENT_REQUEST = '/Web/V1/Customer/GetCustomerOptionContractSettlementRequest'

    GET_CUSTOMER_OPTION_CONTRACT_SETTLEMENT_REQUEST_V2 = '/Web/V2/Customer/GetCustomerOptionContractSettlementRequest'
    GET_CUSTOMER_SUMMARY_SETTLEMENT_REQUESTS_HISTORY = '/Web/V1/Customer/GetCustomerSummarySettlementRequestsHistory'
    EXCEL_MY_ORDERS = '/Web/V1/Order/ExportToExcel'
    SAVE_SETTLEMENT_REQUEST = '/Web/V1/Customer/SaveSettlementRequest'

    GET_SYMBOLS_NOTES = '/Web/V1/SymbolNote/GetSymbolsNotes'
    ADD_SYMBOL_NOTE = '/Web/V1/SymbolNote/AddSymbolNote'
    DELETE_SYMBOL_NOTE = '/Web/V1/SymbolNote/DeleteSymbolNote'
    EDIT_SYMBOL_NOTE = '/Web/V1/SymbolNote/EditSymbolNote'

    UPDATE_SYMBOL_NOTES = '/Web/V1/WatchListRow/UpdateSymbolNotes'
    GET_SYMBOL_NOTES = '/Web/V1/WatchListRow/GetSymbolNotes'
    GET_PAYMENT_OPTIONS = '/Web/V1/MoneyPayment/GetPaymentOptions'
    GET_CUSTOMER_BANK_ACCOUNTS = '/Web/V1/MoneyPayment/GetCustomerBankAccounts'
    SAVE_USER_SETTINGS_BY_SETTING_NAME_NEW = '/Web/V1/Customer/SaveUserSettingsBySettingNameNew'
    GET_USER_SETTINGS_BY_SETTING_NAME = '/Web/V1/Customer/GetUserSettingsBySettingName'

    REALTIME_PORTFOLIO_DETAIL = '/Web/V1/RealtimePortfolio/Detail'
    GET_SYMBOL_BOND_AMOUNT = '/Web/V1/Order/GetSymbolBondAmount'
    GET_MONEY_RECEIPT_LIST = '/Web/V1/MoneyReceipt/GetMoneyReceiptList'
    GET_MONEY_PAYMENT_LIST = '/Web/V1/MoneyPayment/GetMoneyPaymentListSilver'
    GET_CUSTOMER_OPTION_SETTLMENT_REPORTS = '/Web/V1/Customer/GetCustomerOptionSettlmentReports'

    TSE_FUTURE_GET_CUSTOMER_CONTRACT_SETTLEMENT_REQUEST = '/Web/V1/TseFuture/GetCustomerContractSettlementRequest'
    TSE_FUTURE_SAVE_SETTLEMENT_REQUEST = '/Web/V2/TseFuture/SaveSettlementRequest'
    TSE_FUTURE_GET_CUSTOMER_FUTURE_SETTLMENT_REPORTS = '/Web/V1/TseFuture/GetCustomerFutureSettlmentReports'
    TSE_FUTURE_GET_CUSTOMER_SUMMARY_SETTLEMENT_REQUESTS_HISTORY = '/Web/V1/TseFuture/GetCustomerSummarySettlementRequestsHistory'
    TSE_FUTURE_PROFIT_LOSS_HISTORY = '/Web/V1/TseFuture/ProfitLossHistory'

    DELETE_MONEY_RECEIPT = '/Web/V1/MoneyReceipt/Delete/MoneyReceipt'
    DELETE_MONEY_PAYMENT_REQUEST = '/Web/V1/MoneyPayment/DeleteMoneyPaymentRequest'
    GET_WATCHLISTS_BY_SYMBOL = '/Web/V1/WatchListRow/GetWatchlistsBySymbol'
    GET_GATEWAY_PROVIDERS = '/Web/V1/MoneyTransfer/GetGatewayProviders'
    GET_TADDIR_GATEWAY_PROVIDERS = '/Web/V2/TadbirPay/GetGatewayProviders'
    GET_PARENT_INFO = '/Web/V2/TadbirPay/GetParentInfo'
    BEGIN_REQUEST = '/Web/V1/MoneyTransfer/BeginRequest'
    CREATE_DEPOSIT = '/Web/V2/TadbirPay/CreateDeposit'
    GET_SUPERVISOR_MESSAGE_ARCHIVE = '/Web/V1/Message/GetSupervisorMessageArchive'
    SEND_MONEY_PAYMENT_REQUEST = '/Web/V1/MoneyPayment/SendMoneyPaymentRequest'
    GET_CHANGE_BROKER_REQUESTS = '/Web/V1/SymbolChangeBroker/GetChangeBrokerRequests'
    SEND_CHANGE_BROKER_REQUEST = '/Web/V1/SymbolChangeBroker/SendChangeBrokerRequest'
    SAVE_MONEY_RECEIPT = '/Web/V1/MoneyReceipt/Post/MoneyReceipt'
    DELETE_CHANGE_BROKER_REQUEST = '/Web/V1/SymbolChangeBroker/DeleteChangeBrokerRequest'

    GET_BASKET_ORDERS = '/Web/V1/BasketOrder/GetBasketOrders'
    GET_BASKET_ORDER_ROWS = '/Web/V1/BasketOrder/GetBasketOrderRows'

    GET_ACTIVE_OTP_TOKEN = '/Web/V1/Otp/GetActiveOTPToken'
    ACTIVE_OTP = '/Web/V1/Otp/ActiveOTP'
    DEACTIVE_OTP = '/Web/V1/Otp/DeActiveOTP'


class OrderStatus(Enum):
    partiallyexecutionandexpired = "قسمتی از سفارش انجام و منقضی شد"
    partiallyexecution = "قسمتی از سفارش انجام شد"
    partiallyexcutionandexpired = "قسمتی از سفارش انجام و منقضی شد"
    partiallyexcution = "بخشی از سفارش انجام شد"
    orderexecuted = "سفارش اجرا شد"
    onmodifyboard = "ثبت در سیستم معاملات(ویرایش شده)"
    onmodify = "درحال ویرایش"
    oncancelerror = "خطا! حذف سفارش انجام نشد"
    onboard = "ثبت در سیستم معاملات"
    modify = "ویرایش"
    inomsqueue = "ارسال به کارگزاری"
    freeze = "سفارش شما ثبت شد.در انتظار پایان دوره پذیره نویسی "
    expired = "سفارش منقضی شد"
    error = "خطا"
    done = "سفارش بصورت کامل انجام شد"
    delete = "حذف "
    cancel = "سفارش از سیستم حذف شد"

class OrderSides(Enum):
    BUY = "خرید"
    SELL = "فروش"
