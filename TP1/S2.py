total_seconds = 9875
hour = total_seconds // 3600
a = total_seconds % 3600
min = a //60
s = a % 60
print("9875 seconds = ", hour,"h", min,"min" ,s,"s")
print("check: ",hour*3600 + min*60 + s == total_seconds )