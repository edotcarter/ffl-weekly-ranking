#A python script to check and print out the weekly position tiers from borischen.io

#import requests module
import requests 

#store results of get in QB object
QB = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_QB.txt')

print("QB Tiers")
print(QB.text)
print("*****")
print(" ")

#store results of get in WR object
WR = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_WR.txt')

print("WR Tiers")
print(WR.text)
print("*****")
print(" ")

#store results of get in RB object
RB = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_RB.txt')

print("RB Tiers")
print(RB.text)
print("*****")
print(" ")

#store results of get in TE object
TE = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_TE.txt')

print("TE Tiers")
print(TE.text)
print("*****")
print(" ")

#store results in flex object
flex = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_FLX.txt')

print("FLEX Tiers")
print(flex.text)
print("*****")
print(" ")

#store results in DST object
DST = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_DST.txt')

print("DST Tiers")
print(DST.text)
print("*****")
print(" ")

#store results in K object
K = requests.get('https://s3-us-west-1.amazonaws.com/fftiers/out/text_K.txt')

print("K Tiers")
print(K.text)
print("*****")
print(" ")