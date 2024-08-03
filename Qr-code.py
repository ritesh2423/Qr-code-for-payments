import qrcode

#taking upi id as Stirng
UPI_ID = input("Enter upi id")

# format of upi link
#upi : //pay?pa=UPI_ID&pn=NAME&am=AMMOUNT&cu=CURRENCY&tn=MESSAGE
#here pa=recipient upi-id pn= recipient name am=ammount  cu= form of currency tn= message before payment sended with transaction

#defining url payment on the basis of upi id and the payment app

paytm_url = f'upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234'
phonepe_url = f'upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234'
credupi_url = f'upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234'

#createing qr codes for each payment apps
paytm_qr=qrcode.make(paytm_url)
phonepe_qr=qrcode.make(phonepe_url)
googlepay_qr=qrcode.make(googlepay_url)
credupi_qr=qrcode.make(credupi_url)

#save the qr in storage (Optional)
paytm_qr.save('paytm.png')
phonepe_qr.save('phonepay.png')
googlepay_qr.save('googlepay.png')
credupi_qr.save('credupi.png')

#showing qr code with pillow
paytm_qr.show()
phonepe_qr.show()
googlepay_qr.show()
credupi_qr.show()