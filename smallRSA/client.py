import gmpy2
from Crypto.Util.number import long_to_bytes

n= 131351460044200870397043709090757073761162762710937783517733229107904226870966872745226745597696586548174302909582621103277183989288690050168361125818537361050872346229066622594101064234388603274755138176619643103165293449739140148080737896335730451554731864570044670441823882004762340700839041015684123014453
e= 3
ct= 37530210357019911587955465192505553789667514311991143009308327842954099996986270301158530956679000756233105064992637131321365373293025939760146736501010384417433205180191397212404098036796136641805753972981010485392857194839921309525986679386609460462267249420186981

pt = gmpy2.iroot(ct, e)[0] # root
print(long_to_bytes(pt).decode())