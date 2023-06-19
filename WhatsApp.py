import pywhatkit

phone_num = '+34677290474'
message = 'Prueba desde Python'
hour = 21
minute = 15

try:
    pywhatkit.sendwhatmsg(phone_num, message, hour, minute)
    print(f'Message sent to {phone_num} successfully!')
except Exception as e:
    print(f'Error: {str(e)}')