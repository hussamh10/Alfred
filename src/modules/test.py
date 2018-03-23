from gcal import Calendar as cal

c = cal()
ans = c.getAnswer('next event', '')
print(ans)
