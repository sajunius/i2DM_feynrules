# This file was automatically created by FeynRules 2.3.34
# Mathematica version: 12.1.1 for Linux x86 (64-bit) (June 19, 2020)
# Date: Thu 7 Apr 2022 09:18:17


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.hs, P.hs, P.hs, P.hs ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_12})

V_2 = Vertex(name = 'V_2',
             particles = [ P.hs, P.hs, P.hs ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_53})

V_3 = Vertex(name = 'V_3',
             particles = [ P.h, P.h, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_13})

V_4 = Vertex(name = 'V_4',
             particles = [ P.h, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_59})

V_5 = Vertex(name = 'V_5',
             particles = [ P.Ap, P.Ap, P.hs, P.hs ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_52})

V_6 = Vertex(name = 'V_6',
             particles = [ P.Ap, P.Ap, P.hs ],
             color = [ '1' ],
             lorentz = [ L.VVS1 ],
             couplings = {(0,0):C.GC_57})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Ap, P.Ap, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_8})

V_8 = Vertex(name = 'V_8',
             particles = [ P.Ap, P.Ap, P.h ],
             color = [ '1' ],
             lorentz = [ L.VVS1 ],
             couplings = {(0,0):C.GC_58})

V_9 = Vertex(name = 'V_9',
             particles = [ P.ghG, P.ghG__tilde__, P.G ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_4})

V_10 = Vertex(name = 'V_10',
              particles = [ P.G, P.G, P.G ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_4})

V_11 = Vertex(name = 'V_11',
              particles = [ P.G, P.G, P.G, P.G ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_6,(0,0):C.GC_6,(2,2):C.GC_6})

V_12 = Vertex(name = 'V_12',
              particles = [ P.P__tilde__Chi1__tilde__, P.P__tilde__Chi1, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_22})

V_13 = Vertex(name = 'V_13',
              particles = [ P.P__tilde__Chi2__tilde__, P.P__tilde__Chi1, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_20})

V_14 = Vertex(name = 'V_14',
              particles = [ P.P__tilde__Chi1__tilde__, P.P__tilde__Chi2, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_20})

V_15 = Vertex(name = 'V_15',
              particles = [ P.P__tilde__Chi2__tilde__, P.P__tilde__Chi2, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_7})

V_16 = Vertex(name = 'V_16',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_17 = Vertex(name = 'V_17',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_18 = Vertex(name = 'V_18',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_19 = Vertex(name = 'V_19',
              particles = [ P.u__tilde__, P.u, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_20 = Vertex(name = 'V_20',
              particles = [ P.c__tilde__, P.c, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_21 = Vertex(name = 'V_21',
              particles = [ P.t__tilde__, P.t, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_22 = Vertex(name = 'V_22',
              particles = [ P.A, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_31})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Ap, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_16})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__plus__, P.hs, P.hs ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_24})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.hs ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_54})

V_26 = Vertex(name = 'V_26',
              particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_34})

V_27 = Vertex(name = 'V_27',
              particles = [ P.A, P.Ap, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_33})

V_28 = Vertex(name = 'V_28',
              particles = [ P.Ap, P.Ap, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_19})

V_29 = Vertex(name = 'V_29',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_9})

V_30 = Vertex(name = 'V_30',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_10})

V_31 = Vertex(name = 'V_31',
              particles = [ P.b__tilde__, P.b, P.hs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_62})

V_32 = Vertex(name = 'V_32',
              particles = [ P.tt__plus__, P.tt__minus__, P.hs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_65})

V_33 = Vertex(name = 'V_33',
              particles = [ P.c__tilde__, P.c, P.hs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_63})

V_34 = Vertex(name = 'V_34',
              particles = [ P.t__tilde__, P.t, P.hs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_64})

V_35 = Vertex(name = 'V_35',
              particles = [ P.Ap, P.Z, P.hs, P.hs ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_51})

V_36 = Vertex(name = 'V_36',
              particles = [ P.Ap, P.Z, P.hs ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_56})

V_37 = Vertex(name = 'V_37',
              particles = [ P.Ap, P.Z, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_15})

V_38 = Vertex(name = 'V_38',
              particles = [ P.Ap, P.Z, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_60})

V_39 = Vertex(name = 'V_39',
              particles = [ P.P__tilde__Chi1__tilde__, P.P__tilde__Chi1, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_23})

V_40 = Vertex(name = 'V_40',
              particles = [ P.P__tilde__Chi2__tilde__, P.P__tilde__Chi1, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_21})

V_41 = Vertex(name = 'V_41',
              particles = [ P.P__tilde__Chi1__tilde__, P.P__tilde__Chi2, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_21})

V_42 = Vertex(name = 'V_42',
              particles = [ P.P__tilde__Chi2__tilde__, P.P__tilde__Chi2, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_14})

V_43 = Vertex(name = 'V_43',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_32})

V_44 = Vertex(name = 'V_44',
              particles = [ P.Ap, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_17})

V_45 = Vertex(name = 'V_45',
              particles = [ P.Z, P.Z, P.hs, P.hs ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_50})

V_46 = Vertex(name = 'V_46',
              particles = [ P.Z, P.Z, P.hs ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_55})

V_47 = Vertex(name = 'V_47',
              particles = [ P.Z, P.Z, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18})

V_48 = Vertex(name = 'V_48',
              particles = [ P.Z, P.Z, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_61})

V_49 = Vertex(name = 'V_49',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_11})

V_50 = Vertex(name = 'V_50',
              particles = [ P.d__tilde__, P.d, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_51 = Vertex(name = 'V_51',
              particles = [ P.s__tilde__, P.s, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_52 = Vertex(name = 'V_52',
              particles = [ P.b__tilde__, P.b, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_53 = Vertex(name = 'V_53',
              particles = [ P.d__tilde__, P.d, P.Ap ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_45})

V_54 = Vertex(name = 'V_54',
              particles = [ P.s__tilde__, P.s, P.Ap ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_45})

V_55 = Vertex(name = 'V_55',
              particles = [ P.b__tilde__, P.b, P.Ap ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_45})

V_56 = Vertex(name = 'V_56',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_36,(0,1):C.GC_38})

V_57 = Vertex(name = 'V_57',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_36,(0,1):C.GC_38})

V_58 = Vertex(name = 'V_58',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_36,(0,1):C.GC_38})

V_59 = Vertex(name = 'V_59',
              particles = [ P.e__plus__, P.e__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_60 = Vertex(name = 'V_60',
              particles = [ P.m__plus__, P.m__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_61 = Vertex(name = 'V_61',
              particles = [ P.tt__plus__, P.tt__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_62 = Vertex(name = 'V_62',
              particles = [ P.e__plus__, P.e__minus__, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_49})

V_63 = Vertex(name = 'V_63',
              particles = [ P.m__plus__, P.m__minus__, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_49})

V_64 = Vertex(name = 'V_64',
              particles = [ P.tt__plus__, P.tt__minus__, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_49})

V_65 = Vertex(name = 'V_65',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_42})

V_66 = Vertex(name = 'V_66',
              particles = [ P.m__plus__, P.m__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_42})

V_67 = Vertex(name = 'V_67',
              particles = [ P.tt__plus__, P.tt__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_42})

V_68 = Vertex(name = 'V_68',
              particles = [ P.u__tilde__, P.u, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_69 = Vertex(name = 'V_69',
              particles = [ P.c__tilde__, P.c, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_70 = Vertex(name = 'V_70',
              particles = [ P.t__tilde__, P.t, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_71 = Vertex(name = 'V_71',
              particles = [ P.u__tilde__, P.u, P.Ap ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_48})

V_72 = Vertex(name = 'V_72',
              particles = [ P.c__tilde__, P.c, P.Ap ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_48})

V_73 = Vertex(name = 'V_73',
              particles = [ P.t__tilde__, P.t, P.Ap ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_48})

V_74 = Vertex(name = 'V_74',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_41})

V_75 = Vertex(name = 'V_75',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_41})

V_76 = Vertex(name = 'V_76',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,1):C.GC_35,(0,0):C.GC_30})

V_77 = Vertex(name = 'V_77',
              particles = [ P.ve__tilde__, P.ve, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_46})

V_78 = Vertex(name = 'V_78',
              particles = [ P.vm__tilde__, P.vm, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_46})

V_79 = Vertex(name = 'V_79',
              particles = [ P.vt__tilde__, P.vt, P.Ap ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_46})

V_80 = Vertex(name = 'V_80',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_40})

V_81 = Vertex(name = 'V_81',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_40})

V_82 = Vertex(name = 'V_82',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_40})

V_83 = Vertex(name = 'V_83',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_84 = Vertex(name = 'V_84',
              particles = [ P.m__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_85 = Vertex(name = 'V_85',
              particles = [ P.tt__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_86 = Vertex(name = 'V_86',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_26})

V_87 = Vertex(name = 'V_87',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_27})

V_88 = Vertex(name = 'V_88',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_28})

V_89 = Vertex(name = 'V_89',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_90 = Vertex(name = 'V_90',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_92 = Vertex(name = 'V_92',
              particles = [ P.vm__tilde__, P.m__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_93 = Vertex(name = 'V_93',
              particles = [ P.vt__tilde__, P.tt__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

V_94 = Vertex(name = 'V_94',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_66})

V_95 = Vertex(name = 'V_95',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_68})

V_96 = Vertex(name = 'V_96',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_67})

V_97 = Vertex(name = 'V_97',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_69})

V_98 = Vertex(name = 'V_98',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_25})

