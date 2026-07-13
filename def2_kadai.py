def postTaxPrice(price):
    ans = price * 1.08
    return int(ans)

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")
