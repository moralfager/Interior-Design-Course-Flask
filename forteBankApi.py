import requests
import xml.etree.ElementTree as ET
import os


def getPurchaseURL(price, unique_id, name, surname, email, token):
    # ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://ecomtst.fortebank.com/Exec'
    headers = {'Content-Type': 'application/xml'}
    forte_login = os.environ.get('forte_login')
    forte_password = os.environ.get('forte_password')
    auth = (forte_login, forte_password)
    xml_string = f'''
    <TKKPG>
        <Request>
            <Operation>CreateOrder</Operation>
            <Language>RU</Language>
            <Order>
                <OrderType>Purchase</OrderType>
                <Merchant>MERHFOR_TEST</Merchant>
                <Amount>{price}</Amount>
                <Currency>398</Currency>
                <Description>xxxxxxxx</Description>
                <ApproveURL>http://localhost:5000/buy/checkPayment/{unique_id}</ApproveURL>
                <CancelURL>http://localhost:5000/buy/checkPayment/{unique_id}</CancelURL>
                <DeclineURL>http://localhost:5000/buy/checkPayment/{unique_id}</DeclineURL>
                <AddParams>
                    <FA-DATA>Phone=22211444</FA-DATA>
                    <OrderExpirationPeriod>30</OrderExpirationPeriod>
                </AddParams>
            </Order>
        </Request>
    </TKKPG>
    '''
    # Отправляем запрос к API

    response = requests.post(url, headers=headers, auth=auth, data=xml_string)
    responseXML = response.content.decode('utf-8')
    response = ET.fromstring(responseXML)

    session_id = response.find('.//SessionID').text
    order_id = response.find('.//OrderID').text
    url = response.find('.//URL').text

    # Print the results
    print(f"Session ID: {session_id}")
    print(f"Order ID: {order_id}")
    print(f"URL: {url}")
    print(f"YOUR URL IS: {url}/?OrderID={order_id}&SessionID={session_id}")
    # return f"{url}/?OrderID={order_id}&SessionID={session_id}"
    data = [unique_id, order_id, session_id, f"{url}?OrderID={order_id}&SessionID={session_id}", name, surname, email, token]
    return data




def checkStatusForte(OrderID, SessionID):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://ecomtst.fortebank.com/Exec'
    headers = {'Content-Type': 'application/xml'}
    forte_login = os.environ.get('forte_login')
    forte_password = os.environ.get('forte_password')
    auth = (forte_login, forte_password)
    checkStatusForteXML = f'''
        <TKKPG>
            <Request>
                <Operation>GetOrderStatus</Operation>
                <Language>RU</Language>
                <Order>
                    <Merchant>MERHFOR_TEST</Merchant>
                    <OrderID>{OrderID}</OrderID>
                </Order>
                <SessionID>{SessionID}</SessionID>
            </Request>
        </TKKPG>
    '''
    response = requests.post(url, headers=headers, auth=auth, data=checkStatusForteXML)
    responseXML = response.content.decode('utf-8')
    response = ET.fromstring(responseXML)
    OrderStatus = response.find('.//OrderStatus').text
    return OrderStatus

