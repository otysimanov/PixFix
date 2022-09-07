import hmac
import hashlib

apikey    = "00f2d3d1fcd18ed113f32c7e1c4c6fcd"
merchant_code = "DS13144"
merchant_ref  = "INV55567"
amount        = 1500000

signStr = "{}{}{}".format(merchant_code, merchant_ref, amount)
signature = hmac.new(bytes(apikey,'latin-1'), bytes(signStr,'latin-1'), hashlib.sha256).hexdigest()


print(signature)

# result
# 9f167eba844d1fcb369404e2bda53702e2f78f7aa12e91da6715414e65b8c86a
