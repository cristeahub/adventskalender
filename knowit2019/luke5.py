s = "tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol"
print(s)

l = len(s)-1

for i in range(0, l//2, 3):
    sl = list(s)
    tmp1, tmp2, tmp3 = sl[i], sl[i+1], sl[i+2]
    sl[i], sl[i+1], sl[i+2] = sl[l-i-2], sl[l-i-1], sl[l-i]
    sl[l-i-2], sl[l-i-1], sl[l-i] = tmp1, tmp2, tmp3
    s = ''.join(sl)

for i in range(0, l, 2):
    sl = list(s)
    tmp1 = sl[i]
    sl[i] = sl[i+1]
    sl[i+1] = tmp1
    s = ''.join(sl)

print(s[len(s)//2:] + s[:len(s)//2])
