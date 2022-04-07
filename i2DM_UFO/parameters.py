# This file was automatically created by FeynRules 2.3.34
# Mathematica version: 12.1.1 for Linux x86 (64-bit) (June 19, 2020)
# Date: Thu 7 Apr 2022 09:18:17



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.488,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.188,
               texname = '\\text{MZ}',
               lhablock = 'GAUGEMASS',
               lhacode = [ 1 ])

epsilon = Parameter(name = 'epsilon',
                    nature = 'external',
                    type = 'real',
                    value = 0.01,
                    texname = '\\epsilon',
                    lhablock = 'HIDDEN',
                    lhacode = [ 1 ])

ttheta = Parameter(name = 'ttheta',
                   nature = 'external',
                   type = 'real',
                   value = 0.00001,
                   texname = '\\text{ttheta}',
                   lhablock = 'HIDDEN',
                   lhacode = [ 2 ])

aDM1 = Parameter(name = 'aDM1',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{aDM1}',
                 lhablock = 'HIDDEN',
                 lhacode = [ 3 ])

MHS = Parameter(name = 'MHS',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{MHS}',
                lhablock = 'HIDDEN',
                lhacode = [ 4 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'HIGGS',
               lhacode = [ 1 ])

swsq = Parameter(name = 'swsq',
                 nature = 'external',
                 type = 'real',
                 value = 0.225,
                 texname = '\\text{swsq}',
                 lhablock = 'SMINPUTS',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 2 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663900000000002,
               texname = '\\text{Gf}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 4 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.42,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 174.3,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

ME = Parameter(name = 'ME',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{ME}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.106,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0022,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 174.3,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.0047,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.096,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MD1 = Parameter(name = 'MD1',
                nature = 'external',
                type = 'real',
                value = 50,
                texname = '\\text{MD1}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MD2 = Parameter(name = 'MD2',
                nature = 'external',
                type = 'real',
                value = 100,
                texname = '\\text{MD2}',
                lhablock = 'MASS',
                lhacode = [ 58 ])

MAp = Parameter(name = 'MAp',
                nature = 'external',
                type = 'real',
                value = 150,
                texname = '\\text{MAp}',
                lhablock = 'MASS',
                lhacode = [ 1023 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WD1 = Parameter(name = 'WD1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WD1}',
                lhablock = 'DECAY',
                lhacode = [ 52 ])

WD2 = Parameter(name = 'WD2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WD2}',
                lhablock = 'DECAY',
                lhacode = [ 58 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.44140351,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WAp = Parameter(name = 'WAp',
                nature = 'external',
                type = 'real',
                value = 0.0008252,
                texname = '\\text{WAp}',
                lhablock = 'DECAY',
                lhacode = [ 1023 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.04759951,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00282299,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WHS = Parameter(name = 'WHS',
                nature = 'external',
                type = 'real',
                value = 5.23795,
                texname = '\\text{WHS}',
                lhablock = 'DECAY',
                lhacode = [ 35 ])

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - swsq)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(swsq)',
               texname = 's_w')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

aD = Parameter(name = 'aD',
               nature = 'internal',
               type = 'real',
               value = '1/aDM1',
               texname = '\\text{aD}')

SignAux = Parameter(name = 'SignAux',
                    nature = 'internal',
                    type = 'real',
                    value = '(-MAp + MZ)/cmath.sqrt((-MAp + MZ)**2)',
                    texname = '\\text{SignAux}')

SignScalar = Parameter(name = 'SignScalar',
                       nature = 'internal',
                       type = 'real',
                       value = '(MH - MHS)/cmath.sqrt((MH - MHS)**2)',
                       texname = '\\text{SignScalar}')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '1/(2**0.25*cmath.sqrt(Gf))',
              texname = 'v')

ctheta = Parameter(name = 'ctheta',
                   nature = 'internal',
                   type = 'real',
                   value = '1/cmath.sqrt(1 + ttheta**2)',
                   texname = 'c_{\\theta }')

stheta = Parameter(name = 'stheta',
                   nature = 'internal',
                   type = 'real',
                   value = 'ttheta/cmath.sqrt(1 + ttheta**2)',
                   texname = 's_{\\theta }')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

chi = Parameter(name = 'chi',
                nature = 'internal',
                type = 'real',
                value = 'epsilon/cw',
                texname = '\\chi')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

gD = Parameter(name = 'gD',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aD)*cmath.sqrt(cmath.pi)',
               texname = 'g_D')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(MH**2 + MHS**2 + SignScalar*cmath.sqrt((MH**2 - MHS**2)**2))/(4.*v**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

eta = Parameter(name = 'eta',
                nature = 'internal',
                type = 'real',
                value = 'chi/cmath.sqrt(1 - chi**2)',
                texname = '\\eta')

muSM2 = Parameter(name = 'muSM2',
                  nature = 'internal',
                  type = 'real',
                  value = 'lam*v**2',
                  texname = '\\text{muSM2}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

DZaux = Parameter(name = 'DZaux',
                  nature = 'internal',
                  type = 'real',
                  value = 'SignAux*cmath.sqrt(MAp**4 + MZ**4 - 2*MAp**2*MZ**2*(1 + 2*eta**2*sw**2))',
                  texname = '\\text{DZaux}')

MZ0 = Parameter(name = 'MZ0',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt((MAp**2 + MZ**2 + SignAux*cmath.sqrt((MAp**2 - MZ**2)**2 - 4*eta**2*MAp**2*MZ**2*sw**2))/(2 + 2*eta**2*sw**2))',
                texname = '\\text{MZ0}')

DZ = Parameter(name = 'DZ',
               nature = 'internal',
               type = 'real',
               value = '(MAp**4 - DZaux*MZ**2 + MZ**4 + MAp**2*(-DZaux - 2*eta**2*MZ**2*sw**2))/(2.*MAp**2*MZ**2)',
               texname = '\\text{DZ}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cw*MZ0',
               texname = 'M_W')

MX = Parameter(name = 'MX',
               nature = 'internal',
               type = 'real',
               value = 'MZ0*cmath.sqrt(DZ)',
               texname = '\\text{MX}')

taAux = Parameter(name = 'taAux',
                  nature = 'internal',
                  type = 'real',
                  value = '-1 + DZ + eta**2*sw**2',
                  texname = '\\text{taAux}')

ta = Parameter(name = 'ta',
               nature = 'internal',
               type = 'real',
               value = '-(taAux + SignAux*cmath.sqrt(4*eta**2*sw**2 + taAux**2))/(2.*eta*sw)',
               texname = 't_{\\alpha }')

xi = Parameter(name = 'xi',
               nature = 'internal',
               type = 'real',
               value = '(MX*cmath.sqrt(1 - chi**2))/gD',
               texname = '\\xi')

ca = Parameter(name = 'ca',
               nature = 'internal',
               type = 'real',
               value = '1/cmath.sqrt(1 + ta**2)',
               texname = 'c_{\\alpha }')

lamD = Parameter(name = 'lamD',
                 nature = 'internal',
                 type = 'real',
                 value = '-((ttheta*abs(MD1 - MD2)*cmath.sqrt(2))/((1 + ttheta**2)*xi))',
                 texname = '\\text{lamD}')

sa = Parameter(name = 'sa',
               nature = 'internal',
               type = 'real',
               value = 'ta/cmath.sqrt(1 + ta**2)',
               texname = 's_{\\alpha }')

rho = Parameter(name = 'rho',
                nature = 'internal',
                type = 'real',
                value = '(MH**2 + MHS**2 - SignScalar*cmath.sqrt((MH**2 - MHS**2)**2))/(4.*xi**2)',
                texname = '\\rho')

DMgauge = Parameter(name = 'DMgauge',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt((MD1 - MD2)**2 - 2*lamD**2*xi**2)',
                    texname = '\\text{DMgauge}')

muH2 = Parameter(name = 'muH2',
                 nature = 'internal',
                 type = 'real',
                 value = 'rho*xi**2',
                 texname = '\\text{muH2}')

MD0 = Parameter(name = 'MD0',
                nature = 'internal',
                type = 'real',
                value = '(-DMgauge + MD1 + MD2)/2.',
                texname = '\\text{MD0}')

MDD = Parameter(name = 'MDD',
                nature = 'internal',
                type = 'real',
                value = '(DMgauge + MD1 + MD2)/2.',
                texname = '\\text{MDD}')

DM = Parameter(name = 'DM',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt((-MD0 + MDD)**2 + 2*lamD**2*xi**2)',
               texname = '\\text{DM}')

