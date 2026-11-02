"""
Die Bedeutung des Plus-Zeichens in Python
"""
#(str) ist string,sring bedeutet Zeichenketten in einfachen oder doppelten Anführungszeichen, z. B. „Hallo“, ‚Python‘, „123“, ‚5.0‘, „4711“  
#    und (int) ist Integer,Integer sind ganze Zahlen 
print("Hallo" + "Welt")
# Im terminal steht jetzt: "HalloWelt". Also ohne Leerzeichen zwischen den beiden Wörtern. 
print("Hallo" + " Welt")
# Im terminal steht jetzt: "Hallo Welt"". Also mit Leerzeichen zwischen den beiden Wörtern. 
print(15 + 20)
# im terminal steht jetzt: 35. Also die Summe der beiden Zahlen.
print("123" + "321")
# im terminal steht jetzt:123321. das heißt wenn man es in " " setzt steht die zahl so da
print(123 + "321")
#      |  |      |_______ String
# Integer rechenoperator
# beides zusammen geht nicht also nicht ein mit " " und eins ohne im terminal steht:unsupported operand type(s) for +: 'int' and 'str'
print("123" + "vorbei")
# im terminal wird jetzt "123Vorbei" angezeigt also zahl mit bustaben ohne lerzeichen
#print(123 + "vorbei")
#geht wieder nicht da wieder etwas mit""und ohne ""steht
#print("vorbei" + 123)
#ist das selbe nur umgedreht