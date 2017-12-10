#currency.py
#Feiyang Xu(Voler007)
#December 1,2017
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""
def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency+'&to=EUR&amt=1')
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr[-11:-4] != "invalid"

        

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    if iscurrency(currency_from)==False or iscurrency(currency_to)==False:
        return "Your currency code is invalid!"
    else:
        from urllib.request import urlopen
        doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode('ascii')
        jstr=jstr[:-34]+" }"
        d=eval(jstr)
        alist=d['to'].split()
        a=float(alist[0])
        return a


"""Module for test

This module provides several test functions to test the module above."""
def test_iscurrency():
    """test iscurrency(currency)"""
    assert(True == iscurrency("USD"))
    assert(True == iscurrency("KHR"))
    assert(True == iscurrency("CRC"))
    assert(False == iscurrency("ACA"))
    assert(False == iscurrency("KUK"))

    
def test_exchange():
    """test exchange(currency_from, currency_to, amount_from)"""
    assert(2.0952375 == exchange("USD","EUR",2.5))
    assert(1042.8948102411 == exchange("QAR","XOF",7))
    assert(38931.325765306 == exchange("SGD","LKR",345))
    assert(1508.4960330019 == exchange("BZD","GMD",66))
    assert('Your currency code is invalid!' == exchange("CAD","EUZ",25))



def testAll():
    """test all cases"""
    test_iscurrency()
    test_exchange()
    print("All tests passed")


testAll()
