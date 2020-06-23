text = "X-DSPAM-Confidence: 0.8475"
dotfind = text.find(".")
ftext = float(text[dotfind-1:])
print(ftext)
