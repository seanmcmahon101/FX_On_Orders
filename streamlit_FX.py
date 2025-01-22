import streamlit as st
import pandas as pd
import io

CUST_TO_CURR = {
    "00LPPB"	:	"GBP2"	,
    "2MP"	:	"EUR"	,
    "ABALLT"	:	"EUR"	,
    "ABER"	:	"EUR"	,
    "ABG"	:	"EUR"	,
    "ABGUD"	:	"EUR"	,
    "ABTEC"	:	"EUR"	,
    "ACCAV"	:	"GBP"	,
    "ADRIAN"	:	"EUR"	,
    "AFG"	:	"EUR"	,
    "AFIKU"	:	"USD"	,
    "AGCOBE"	:	"EUR"	,
    "AGCODE"	:	"EUR"	,
    "AGCODK"	:	"EUR"	,
    "AGCOFIN"	:	"EUR"	,
    "AGCOFR"	:	"EUR"	,
    "AGCOHO"	:	"EUR"	,
    "AGCONL"	:	"EUR"	,
    "AGCOSA"	:	"EUR"	,
    "AGRITA"	:	"EUR"	,
    "AGRO"	:	"EUR"	,
    "AKCAN"	:	"GBP"	,
    "ALAMO"	:	"GBP"	,
    "ALKO"	:	"EUR"	,
    "ALTAN"	:	"EUR"	,
    "ALTER"	:	"EUR"	,
    "ALTIA"	:	"EUR"	,
    "AMCA"	:	"EUR"	,
    "AMISCO"	:	"EUR"	,
    "AMKOD"	:	"EUR"	,
    "AMMANN"	:	"EUR"	,
    "AMMANS"	:	"EUR"	,
    "ANULT"	:	"EUR"	,
    "ARANN"	:	"EUR"	,
    "ARCOS"	:	"EUR"	,
    "ARELLE"	:	"EUR"	,
    "ARGO"	:	"EUR"	,
    "ARGOCZ"	:	"EUR"	,
    "ARGOIT"	:	"EUR"	,
    "ARGOUK"	:	"GBP"	,
    "ARON"	:	"EUR"	,
    "ARTEMIS"	:	"GBP"	,
    "ASHRAD"	:	"EUR"	,
    "ATCITA"	:	"EUR"	,
    "ATHENS"	:	"EUR"	,
    "ATLAS"	:	"EUR"	,
    "ATLASAM"	:	"EUR"	,
    "ATLASB"	:	"EUR"	,
    "ATLASBLG"	:	"GBP"	,
    "ATLASDE"	:	"EUR"	,
    "ATLASIN2"	:	"GBP"	,
    "ATLASIND"	:	"GBP"	,
    "ATLASIT"	:	"EUR"	,
    "ATLASMAS"	:	"EUR"	,
    "ATLASUR"	:	"EUR"	,
    "ATMG"	:	"EUR"	,
    "AVTEC"	:	"GBP"	,
    "AYHAN"	:	"GBP"	,
    "BACHOF"	:	"EUR"	,
    "BAR"	:	"GBP"	,
    "BATEM"	:	"GBP"	,
    "BCELTD"	:	"USD"	,
    "BCSEU"	:	"EUR"	,
    "BELL"	:	"GBP"	,
    "BELLGH"	:	"EUR"	,
    "BELLUK"	:	"GBP"	,
    "BENOT"	:	"EUR"	,
    "BENTLY"	:	"GBP"	,
    "BEREND"	:	"EUR"	,
    "BERFIN"	:	"EUR"	,
    "BERFRA"	:	"EUR"	,
    "BERGMAN"	:	"GBP"	,
    "BERNST"	:	"GBP"	,
    "BERTHO"	:	"EUR"	,
    "BGP"	:	"GBP"	,
    "BIBUS"	:	"GBP"	,
    "BIBUS1"	:	"EUR"	,
    "BIBUSAT"	:	"EUR"	,
    "BIBUSSK"	:	"EUR"	,
    "BINSA"	:	"EUR"	,
    "BMG"	:	"EUR"	,
    "BOBCAD"	:	"USD"	,
    "BOBCAT"	:	"EUR"	,
    "BOBCZ"	:	"EUR"	,
    "BOBFR"	:	"EUR"	,
    "BOMAG"	:	"EUR"	,
    "BONDIO"	:	"EUR"	,
    "BONO"	:	"EUR"	,
    "BOSCHCH"	:	"EUR"	,
    "BOSCHH"	:	"EUR"	,
    "BOSCHP"	:	"EUR"	,
    "BOSCHS"	:	"EUR"	,
    "BOSOIL"	:	"EUR"	,
    "BOSOLE"	:	"EUR"	,
    "BRAKO"	:	"GBP"	,
    "BREVFR"	:	"EUR"	,
    "BREXAU"	:	"EUR"	,
    "BREXFR"	:	"EUR"	,
    "BREXIT"	:	"EUR"	,
    "BREXNL"	:	"EUR"	,
    "BREXSA"	:	"EUR"	,
    "BRIEDA"	:	"EUR"	,
    "BRUEN"	:	"EUR"	,
    "BT"	:	"EUR"	,
    "BTHYDRA"	:	"EUR"	,
    "BTSPARE"	:	"EUR"	,
    "BUCHER"	:	"EUR"	,
    "BUCHGBP"	:	"GBP"	,
    "BURN"	:	"EUR2"	,
    "BURN1"	:	"EUR"	,
    "BURNAUTO"	:	"EUR2"	,
    "BURNEU"	:	"EUR"	,
    "CAB"	:	"EUR"	,
    "CAE25"	:	"EUR"	,
    "CAE25G"	:	"GBP"	,
    "CAE35"	:	"EUR"	,
    "CAE35G"	:	"GBP"	,
    "CAE37"	:	"EUR"	,
    "CAE37G"	:	"GBP"	,
    "CAEKY"	:	"EUR"	,
    "CAEKYG"	:	"GBP"	,
    "CAEYQ"	:	"EUR"	,
    "CAEYQG"	:	"GBP"	,
    "CALF"	:	"EUR"	,
    "CAPMAN"	:	"GBP"	,
    "CAPRONI"	:	"EUR"	,
    "CARGOR"	:	"EUR"	,
    "CARIND"	:	"GBP"	,
    "CARKOR"	:	"EUR"	,
    "CARL"	:	"GBP"	,
    "CARLBF"	:	"GBP"	,
    "CARLS"	:	"EUR"	,
    "CARPOL"	:	"EUR"	,
    "CARRIN"	:	"EUR"	,
    "CARROK"	:	"EUR"	,
    "CARROM"	:	"GBP"	,
    "CARROV"	:	"EUR"	,
    "CARSPA"	:	"EUR"	,
    "CARSPAPT"	:	"EUR"	,
    "CASAP"	:	"EUR"	,
    "CAT25"	:	"GBP"	,
    "CAT35"	:	"GBP"	,
    "CAT37"	:	"GBP"	,
    "CATARR"	:	"EUR"	,
    "CATBR"	:	"GBP"	,
    "CATBRC"	:	"GBP"	,
    "CATBRZ"	:	"EUR"	,
    "CATDKBT"	:	"GBP"	,
    "CATDOR"	:	"GBP"	,
    "CATGOS"	:	"EUR"	,
    "CATINC"	:	"GBP"	,
    "CATINCCZ"	:	"GBP"	,
    "CATINCTL"	:	"GBP"	,
    "CATIND"	:	"GBP"	,
    "CATIND2"	:	"GBP"	,
    "CATIT"	:	"GBP"	,
    "CATITG"	:	"GBP"	,
    "CATJAP"	:	"GBP"	,
    "CATKY"	:	"GBP"	,
    "CATLAR"	:	"GBP"	,
    "CATML"	:	"GBP"	,
    "CATML2"	:	"GBP"	,
    "CATPET"	:	"GBP"	,
    "CATREG"	:	"GBP"	,
    "CATREU"	:	"EUR"	,
    "CATREU1"	:	"GBP"	,
    "CATSAR"	:	"GBP"	,
    "CATSEU"	:	"EUR"	,
    "CATUK"	:	"GBP"	,
    "CATUK1"	:	"GBP"	,
    "CATUK2"	:	"GBP"	,
    "CAUK25"	:	"GBP"	,
    "CAUKYQ"	:	"GBP"	,
    "CCENG"	:	"EUR"	,
    "CDENG"	:	"GBP"	,
    "CEDI"	:	"EUR"	,
    "CEDIT"	:	"EUR"	,
    "CESAB"	:	"EUR"	,
    "CHAFER"	:	"GBP"	,
    "CHARVATCZ"	:	"EUR"	,
    "CIFA"	:	"EUR"	,
    "CIFAMIX"	:	"EUR"	,
    "CIMM"	:	"EUR"	,
    "CLAASSE"	:	"EUR"	,
    "CLAASSU"	:	"EUR"	,
    "CLARK"	:	"GBP"	,
    "CNHAUS"	:	"EUR"	,
    "CNHBE1"	:	"EUR"	,
    "CNHBI"	:	"GBP"	,
    "CNHBI1"	:	"EUR"	,
    "CNHCX"	:	"EUR"	,
    "CNHFR"	:	"EUR"	,
    "CNHHEI"	:	"EUR"	,
    "CNHIND"	:	"GBP"	,
    "CNHIT"	:	"USD"	,
    "CNHKT1"	:	"EUR"	,
    "CNHKUTNO"	:	"EUR"	,
    "CNHLE"	:	"EUR"	,
    "CNHLE1"	:	"EUR"	,
    "CNHLE2"	:	"USD"	,
    "CNHMJ1"	:	"EUR"	,
    "CNHMM3"	:	"EUR"	,
    "CNHMOD"	:	"EUR"	,
    "CNHPL"	:	"EUR"	,
    "CNHSAN"	:	"EUR"	,
    "CNHSE"	:	"GBP"	,
    "CNHSE1"	:	"USD"	,
    "CNHSE2"	:	"EUR"	,
    "CNHSPE"	:	"EUR"	,
    "CNHSPH"	:	"EUR"	,
    "CNHUK"	:	"GBP"	,
    "CNHZD"	:	"EUR"	,
    "COBI"	:	"EUR"	,
    "COEX"	:	"EUR"	,
    "COMBIN"	:	"USD"	,
    "COMER"	:	"EUR"	,
    "COMHYD"	:	"EUR"	,
    "COMPAC"	:	"USD"	,
    "CONTEC"	:	"EUR"	,
    "COSNAV"	:	"EUR"	,
    "CROWNM"	:	"EUR"	,
    "CROWNR"	:	"EUR"	,
    "CUKURO"	:	"EUR"	,
    "CYMAX"	:	"EUR"	,
    "CZETEC"	:	"EUR"	,
    "DAIRYM"	:	"GBP"	,
    "DANAEU"	:	"EUR"	,
    "DANAGB"	:	"GBP"	,
    "DANAHE"	:	"EUR"	,
    "DANAHS"	:	"GBP"	,
    "DANAHU"	:	"EUR"	,
    "DANAIT"	:	"GBP"	,
    "DANAME"	:	"EUR"	,
    "DANAREX"	:	"EUR"	,
    "DANFDK"	:	"EUR"	,
    "DANFEU"	:	"EUR"	,
    "DANI"	:	"EUR"	,
    "DANINL"	:	"EUR"	,
    "DANTAL"	:	"GBP"	,
    "DANTAL1"	:	"GBP"	,
    "DANTGUM"	:	"GBP"	,
    "DANTGUR"	:	"GBP"	,
    "DAVID"	:	"EUR"	,
    "DCATGO"	:	"USD"	,
    "DCDK"	:	"EUR"	,
    "DCFI"	:	"EUR"	,
    "DCNO"	:	"EUR"	,
    "DCNT"	:	"EUR"	,
    "DCREDI"	:	"USD"	,
    "DEAMAG"	:	"EUR"	,
    "DELTA"	:	"EUR"	,
    "DEMAG"	:	"EUR"	,
    "DEMAR"	:	"EUR"	,
    "DENEAG"	:	"GBP"	,
    "DENISO"	:	"EUR"	,
    "DEUTZ"	:	"EUR"	,
    "DEUTZD"	:	"EUR"	,
    "DHOLL"	:	"EUR"	,
    "DHUNAFT"	:	"EUR"	,
    "DICSA"	:	"EUR"	,
    "DINOIL"	:	"EUR"	,
    "DJCBTR"	:	"USD"	,
    "DOLAN"	:	"EUR"	,
    "DOOINF"	:	"EUR"	,
    "DOOSAN"	:	"EUR"	,
    "DOOVEH"	:	"EUR"	,
    "DOYLE"	:	"GBP"	,
    "DOYLE1"	:	"USD"	,
    "DOYLSH"	:	"GBP"	,
    "DRIVESYS"	:	"GBP"	,
    "DRIVESYST"	:	"GBP"	,
    "DSERVO"	:	"USD"	,
    "DUPLO"	:	"EUR"	,
    "DURWEN"	:	"EUR"	,
    "DYNASET"	:	"EUR"	,
    "DYNCHI"	:	"EUR"	,
    "DYNCHIN"	:	"EUR"	,
    "DYNGER"	:	"EUR"	,
    "EASTATT"	:	"GBP"	,
    "ECKER"	:	"EUR"	,
    "EDBERG"	:	"EUR"	,
    "EEF"	:	"GBP"	,
    "EIOTEK"	:	"EUR"	,
    "EJCBTR"	:	"EUR"	,
    "EKOMAT"	:	"EUR"	,
    "ELASIS"	:	"EUR"	,
    "ELET80"	:	"EUR"	,
    "ELM"	:	"EUR"	,
    "EMER"	:	"EUR"	,
    "ENARCO"	:	"EUR"	,
    "ENTEK"	:	"EUR"	,
    "ENVIRO"	:	"GBP"	,
    "EPSILON"	:	"EUR"	,
    "EQUIB"	:	"EUR"	,
    "ERIKSSW"	:	"EUR"	,
    "ESCORTS"	:	"GBP"	,
    "ESHYDA"	:	"EUR"	,
    "EUCRED"	:	"EUR"	,
    "EUROFL"	:	"EUR"	,
    "EXCENT"	:	"EUR"	,
    "EXPRES"	:	"GBP"	,
    "FAE"	:	"EUR"	,
    "FARMTR"	:	"EUR"	,
    "FARRARI"	:	"EUR"	,
    "FDINT"	:	"EUR"	,
    "FERMEC"	:	"GBP"	,
    "FERRI"	:	"EUR"	,
    "FINNVE"	:	"EUR"	,
    "FIZSPA"	:	"EUR"	,
    "FLPOHO"	:	"USD"	,
    "FLUID"	:	"EUR"	,
    "FLUIDR"	:	"EUR"	,
    "FLUIMP"	:	"EUR"	,
    "FLUITECNIK"	:	"EUR"	,
    "FLULOG"	:	"GBP"	,
    "FLUSYS"	:	"EUR"	,
    "FLYBRID"	:	"GBP"	,
    "FMV"	:	"EUR"	,
    "FORD"	:	"EUR"	,
    "FORNIT"	:	"EUR"	,
    "FORS"	:	"EUR"	,
    "FPH"	:	"EUR"	,
    "FRANKO"	:	"EUR"	,
    "FRANZO"	:	"EUR"	,
    "FRASTE"	:	"EUR"	,
    "FRIDLE"	:	"EUR"	,
    "FTE"	:	"EUR"	,
    "GADVAND"	:	"EUR"	,
    "GAM NV"	:	"EUR"	,
    "GAMBINI"	:	"EUR"	,
    "GATES"	:	"GBP"	,
    "GBCRED"	:	"GBP"	,
    "GEESINK"	:	"EUR"	,
    "GEMSA"	:	"EUR"	,
    "GENIE"	:	"GBP"	,
    "GERGULF"	:	"EUR"	,
    "GHPLV"	:	"EUR"	,
    "GIANT"	:	"EUR"	,
    "GIDROS"	:	"EUR"	,
    "GIESEN"	:	"GBP"	,
    "GIMA"	:	"EUR"	,
    "GKN"	:	"EUR"	,
    "GKNDK"	:	"EUR"	,
    "GKNSWE"	:	"EUR"	,
    "GMSWE"	:	"GBP"	,
    "GRASPA"	:	"EUR"	,
    "GRAYSON"	:	"GBP"	,
    "GRAZIA"	:	"EUR"	,
    "GRENOB"	:	"EUR"	,
    "GRIMME"	:	"EUR"	,
    "GTALOM"	:	"EUR"	,
    "HABERK"	:	"EUR"	,
    "HAINAG"	:	"EUR"	,
    "HAINZL"	:	"EUR"	,
    "HALDDE"	:	"EUR"	,
    "HALDSE"	:	"EUR"	,
    "HALDUK"	:	"GBP"	,
    "HAMECH"	:	"GBP"	,
    "HAMM"	:	"EUR"	,
    "HANGZHOU"	:	"USD"	,
    "HARAIN"	:	"EUR"	,
    "HARPER"	:	"GBP"	,
    "HAYTER"	:	"GBP"	,
    "HBS"	:	"EUR"	,
    "HCS"	:	"EUR"	,
    "HCTEC"	:	"GBP"	,
    "HDI"	:	"USD"	,
    "HDM"	:	"EUR"	,
    "HDSES"	:	"EUR"	,
    "HDSFR"	:	"EUR"	,
    "HEDEF"	:	"EUR"	,
    "HEIL"	:	"GBP"	,
    "HEMA"	:	"EUR"	,
    "HF CHINA"	:	"GBP"	,
    "HFCHINA"	:	"GBP"	,
    "HFCUSD"	:	"USD"	,
    "HFINC"	:	"USD"	,
    "HFKOREA"	:	"USD"	,
    "HIDORF"	:	"EUR"	,
    "HIDPL"	:	"EUR"	,
    "HIDRO2"	:	"EUR"	,
    "HIDROM"	:	"EUR"	,
    "HIDROO"	:	"EUR"	,
    "HIDSLOV"	:	"EUR"	,
    "HINE"	:	"EUR"	,
    "HINER"	:	"EUR"	,
    "HINO"	:	"GBP"	,
    "HIPOW"	:	"EUR"	,
    "HIPOW1"	:	"GBP"	,
    "HIPOWB"	:	"GBP"	,
    "HIPOWB2"	:	"GBP2"	,
    "HIPOWCD2"	:	"GBP2"	,
    "HISCAB"	:	"EUR"	,
    "HMH"	:	"GBP"	,
    "HMIND"	:	"GBP"	,
    "HOBAU"	:	"GBP"	,
    "HOERB"	:	"EUR"	,
    "HOERMANN"	:	"EUR"	,
    "HOMBURG"	:	"EUR"	,
    "HORSCH"	:	"EUR"	,
    "HORSCHAS"	:	"EUR"	,
    "HPA"	:	"EUR"	,
    "HPIEU"	:	"EUR"	,
    "HSK"	:	"EUR"	,
    "HUSCO"	:	"GBP"	,
    "HUSIND"	:	"GBP"	,
    "HUSQVA"	:	"EUR"	,
    "HYDBRZ"	:	"USD"	,
    "HYDCZ"	:	"EUR"	,
    "HYDEQ"	:	"EUR"	,
    "HYDING"	:	"EUR"	,
    "HYDLIK"	:	"EUR"	,
    "HYDMAN"	:	"EUR"	,
    "HYDMOB"	:	"EUR"	,
    "HYDNIT"	:	"EUR"	,
    "HYDRAC"	:	"EUR"	,
    "HYDRAP"	:	"EUR"	,
    "HYDRAUL"	:	"EUR"	,
    "HYDREAM"	:	"EUR"	,
    "HYDREG"	:	"EUR"	,
    "HYDREL"	:	"EUR"	,
    "HYDREM"	:	"EUR"	,
    "HYDREMD"	:	"EUR"	,
    "HYDREW"	:	"EUR"	,
    "HYDROFAST"	:	"USD"	,
    "HYDROK"	:	"EUR"	,
    "HYDROM"	:	"EUR"	,
    "HYDRON"	:	"EUR"	,
    "HYDROP"	:	"EUR"	,
    "HYDROS"	:	"EUR"	,
    "HYDROV"	:	"EUR"	,
    "HYDROVER"	:	"EUR"	,
    "HYDSK"	:	"EUR"	,
    "HYDSPA"	:	"EUR"	,
    "HYDSPE"	:	"USD"	,
    "HYDTECH"	:	"USD"	,
    "HYDWAR"	:	"USD"	,
    "HYDX"	:	"EUR"	,
    "HYFLO"	:	"GBP"	,
    "HYFLO2"	:	"GBP2"	,
    "HYFLOEU"	:	"EUR"	,
    "HYNORD"	:	"EUR"	,
    "HYPOOL"	:	"EUR"	,
    "HYTECSA"	:	"EUR"	,
    "HYVA"	:	"EUR"	,
    "HYVAINTER"	:	"EUR"	,
    "HYVAUK"	:	"GBP"	,
    "IBL"	:	"EUR"	,
    "IBST"	:	"EUR"	,
    "IDROVR"	:	"EUR"	,
    "IDSYSTEM"	:	"EUR"	,
    "IFAS"	:	"EUR"	,
    "IMI"	:	"EUR"	,
    "INGEN"	:	"EUR"	,
    "INTEG"	:	"GBP"	,
    "INTER"	:	"EUR"	,
    "INTMAN"	:	"GBP"	,
    "IQS"	:	"EUR"	,
    "IRMER"	:	"EUR"	,
    "ISISFL"	:	"GBP"	,
    "ITBELL"	:	"EUR"	,
    "ITTECH"	:	"EUR"	,
    "IVENTEC"	:	"EUR"	,
    "JCBACC"	:	"GBP"	,
    "JCBATT"	:	"GBP"	,
    "JCBBHL"	:	"EUR2"	,
    "JCBBHP"	:	"GBP"	,
    "JCBCEU"	:	"EUR2"	,
    "JCBCOM"	:	"GBP"	,
    "JCBE2"	:	"EUR2"	,
    "JCBEAR"	:	"GBP"	,
    "JCBEX2"	:	"USD"	,
    "JCBEXC"	:	"USD"	,
    "JCBEXE"	:	"EUR"	,
    "JCBGBU"	:	"GBP"	,
    "JCBGD"	:	"EUR2"	,
    "JCBHBU"	:	"EUR2"	,
    "JCBHP"	:	"GBP"	,
    "JCBHVY"	:	"EUR2"	,
    "JCBINC"	:	"USD"	,
    "JCBIND"	:	"GBP"	,
    "JCBIPTD"	:	"GBP"	,
    "JCBJAI"	:	"GBP"	,
    "JCBLAN"	:	"EUR2"	,
    "JCBLOA"	:	"GBP"	,
    "JCBLOE"	:	"EUR2"	,
    "JCBLP"	:	"GBP"	,
    "JCBMIL"	:	"GBP"	,
    "JCBMIN"	:	"GBP"	,
    "JCBPAC"	:	"EUR2"	,
    "JCBPUN"	:	"GBP"	,
    "JCBRD"	:	"GBP"	,
    "JCBREA"	:	"EUR2"	,
    "JCBRES"	:	"GBP"	,
    "JCBSER"	:	"EUR2"	,
    "JCBTGB"	:	"GBP"	,
    "JCBTRE"	:	"EUR2"	,
    "JCBVIB"	:	"EUR"	,
    "JD BRU"	:	"EUR"	,
    "JDASH"	:	"GBP"	,
    "JDASH1"	:	"GBP"	,
    "JDASHOK"	:	"INR"	,
    "JDBH"	:	"EUR"	,
    "JDBRU"	:	"EUR"	,
    "JDFR"	:	"EUR"	,
    "JDIND"	:	"EUR"	,
    "JDIND2"	:	"GBP"	,
    "JDKAIS"	:	"EUR"	,
    "JDMANN"	:	"EUR"	,
    "JDNL"	:	"EUR"	,
    "JDNL2"	:	"EUR"	,
    "JDSP"	:	"EUR"	,
    "JDZWEI"	:	"EUR"	,
    "JIHOST"	:	"EUR"	,
    "JLGBE"	:	"EUR"	,
    "JLGBRUN"	:	"GBP"	,
    "JLGEP"	:	"EUR"	,
    "JLGEPGB"	:	"GBP"	,
    "JLGGBP"	:	"GBP"	,
    "JLGSCO"	:	"EUR"	,
    "JOHNS"	:	"GBP"	,
    "JUNGH"	:	"EUR"	,
    "JUNGH2"	:	"EUR"	,
    "JUNGHSP"	:	"EUR"	,
    "KAELBLE"	:	"EUR"	,
    "KELLANDS"	:	"GBP"	,
    "KEMPER"	:	"EUR"	,
    "KLADIV"	:	"EUR"	,
    "KMF"	:	"EUR"	,
    "KNORR"	:	"GBP"	,
    "KOGMBH"	:	"EUR"	,
    "KOLBERG"	:	"EUR"	,
    "KOMATS"	:	"EUR"	,
    "KOMBEL"	:	"EUR"	,
    "KOMIND"	:	"GBP"	,
    "KOMINSP"	:	"GBP"	,
    "KOMIPR"	:	"GBP"	,
    "KOMUK"	:	"EUR"	,
    "KOMUKE"	:	"EUR2"	,
    "KONIA"	:	"EUR"	,
    "KOPPEN"	:	"EUR"	,
    "KORMAN"	:	"EUR"	,
    "KRAMAD"	:	"EUR"	,
    "KRAMER"	:	"EUR"	,
    "KRONE"	:	"EUR"	,
    "KTB"	:	"GBP"	,
    "KUBOTA"	:	"EUR"	,
    "KUBOTAJP"	:	"EUR"	,
    "KUHN"	:	"EUR"	,
    "KUHNFR"	:	"EUR"	,
    "KUK"	:	"EUR"	,
    "KUKE"	:	"EUR2"	,
    "KVERN"	:	"EUR"	,
    "LAVERD"	:	"EUR"	,
    "LAXA"	:	"EUR"	,
    "LEEBOY"	:	"GBP"	,
    "LEOPOL"	:	"EUR"	,
    "LETIA"	:	"GBP"	,
    "LIEB"	:	"EUR"	,
    "LIEBC"	:	"EUR"	,
    "LIEBCH"	:	"EUR"	,
    "LIEBCH2"	:	"EUR"	,
    "LIEBD"	:	"EUR"	,
    "LIEBFR"	:	"EUR"	,
    "LIEBFRA"	:	"EUR"	,
    "LIEBGE"	:	"GBP"	,
    "LIEBGE1"	:	"EUR"	,
    "LIEBT"	:	"EUR"	,
    "LIEBTE"	:	"EUR"	,
    "LINDE"	:	"GBP"	,
    "LINDECZ"	:	"EUR"	,
    "LINDGMBH"	:	"EUR"	,
    "LOCATE"	:	"EUR"	,
    "LOCATEL"	:	"EUR"	,
    "LOG"	:	"EUR"	,
    "LOGAB"	:	"EUR"	,
    "LOHMAN"	:	"EUR"	,
    "LOHR"	:	"EUR"	,
    "LOHRSE"	:	"EUR"	,
    "LOKO"	:	"EUR"	,
    "LSMTRON"	:	"USD"	,
    "LUNDBERG"	:	"EUR"	,
    "LUNDE"	:	"EUR"	,
    "LYAHYD"	:	"EUR"	,
    "MAAS"	:	"EUR"	,
    "MAGNA"	:	"EUR"	,
    "MAGNI"	:	"EUR"	,
    "MAHIND"	:	"GBP"	,
    "MANBE"	:	"EUR"	,
    "MANBF"	:	"EUR"	,
    "MANCLPR"	:	"EUR"	,
    "MANITLY"	:	"EUR"	,
    "MANTEU"	:	"EUR"	,
    "MANTIT"	:	"EUR"	,
    "MANWOC"	:	"EUR"	,
    "MANWOCG"	:	"EUR"	,
    "MARINI"	:	"EUR"	,
    "MARVEL"	:	"EUR"	,
    "MARZOC"	:	"EUR"	,
    "MASKIN"	:	"EUR"	,
    "MASTEC"	:	"EUR"	,
    "MASTVAG"	:	"EUR"	,
    "MAURER"	:	"EUR"	,
    "MAZZOTTI"	:	"EUR"	,
    "MBH"	:	"EUR"	,
    "MCCLO"	:	"GBP"	,
    "MCCONN"	:	"GBP"	,
    "MCCORM"	:	"EUR"	,
    "MCFE"	:	"EUR"	,
    "MCHALE"	:	"EUR"	,
    "MCHALE2"	:	"EUR"	,
    "MCHALEGB"	:	"GBP"	,
    "MECAL"	:	"EUR"	,
    "MECALAC"	:	"EUR"	,
    "MECALGBG"	:	"EUR"	,
    "MEDIAS"	:	"GBP"	,
    "MERLO"	:	"EUR"	,
    "METAU"	:	"EUR"	,
    "METFACH"	:	"EUR"	,
    "METSO"	:	"EUR"	,
    "MEZOG"	:	"EUR"	,
    "MICOEU"	:	"GBP"	,
    "MICROHYD"	:	"EUR"	,
    "MILLER"	:	"GBP"	,
    "MINIG"	:	"EUR"	,
    "MONOSEM"	:	"EUR"	,
    "MOTION"	:	"EUR"	,
    "MOTIONC"	:	"USD"	,
    "MOTOR"	:	"EUR"	,
    "MOVECO"	:	"EUR"	,
    "MPO"	:	"EUR"	,
    "MTCELTD"	:	"GBP"	,
    "MULTI"	:	"EUR"	,
    "MYKRO"	:	"GBP"	,
    "NACCO"	:	"EUR"	,
    "NAUDER"	:	"EUR"	,
    "NESTEP"	:	"EUR"	,
    "NEUECO"	:	"EUR"	,
    "NEUSON"	:	"EUR"	,
    "NEUSONSP"	:	"EUR"	,
    "NEWHOL"	:	"EUR"	,
    "NEXEN"	:	"GBP"	,
    "NHMEX"	:	"USD"	,
    "NHMEX1"	:	"GBP"	,
    "NHMEXA"	:	"USD"	,
    "NHOLFR"	:	"EUR"	,
    "NHPOLE"	:	"EUR"	,
    "NHZED"	:	"EUR"	,
    "NIFTY"	:	"GBP"	,
    "NILFIS"	:	"EUR"	,
    "NIMCO"	:	"EUR"	,
    "NINGBO"	:	"USD"	,
    "NMH"	:	"GBP"	,
    "NMH1"	:	"GBP"	,
    "NMHNL"	:	"GBP"	,
    "NMHUSA"	:	"GBP"	,
    "NORD"	:	"EUR"	,
    "NORDFLUID"	:	"EUR"	,
    "NORDHY"	:	"EUR"	,
    "NORTH"	:	"GBP"	,
    "NPI"	:	"GBP"	,
    "NYMEK"	:	"EUR"	,
    "OCGF"	:	"EUR"	,
    "OGNI"	:	"EUR"	,
    "OILPATH"	:	"USD"	,
    "OILPRO"	:	"GBP"	,
    "OILTEC"	:	"EUR"	,
    "OK"	:	"EUR"	,
    "OKHAT"	:	"EUR"	,
    "OLEO"	:	"EUR"	,
    "OLEOBI"	:	"EUR"	,
    "OLEODI"	:	"EUR"	,
    "OMFB"	:	"EUR"	,
    "OMRSPA"	:	"EUR"	,
    "OPTPRO"	:	"EUR"	,
    "ORAFLU"	:	"EUR"	,
    "OSCA"	:	"EUR"	,
    "OTELEC"	:	"EUR"	,
    "OTTO"	:	"GBP"	,
    "PALAZZ"	:	"EUR"	,
    "PANNI"	:	"EUR"	,
    "PANTEN"	:	"USD"	,
    "PARKCZ"	:	"EUR"	,
    "PARKDE"	:	"EUR"	,
    "PARKFI"	:	"EUR"	,
    "PARKFR"	:	"EUR"	,
    "PARKSE"	:	"EUR"	,
    "PARKTROL"	:	"EUR"	,
    "PARMA"	:	"EUR"	,
    "PAUS"	:	"EUR"	,
    "PAZZAG"	:	"EUR"	,
    "PBMACH"	:	"EUR"	,
    "PEDRO"	:	"EUR"	,
    "PERFEC"	:	"EUR"	,
    "PERKIN"	:	"EUR2"	,
    "PERKPE"	:	"GBP"	,
    "PERKST"	:	"GBP"	,
    "PHC LTD"	:	"EUR"	,
    "PHFLTD"	:	"GBP"	,
    "PINGCN"	:	"EUR"	,
    "PINGLC"	:	"EUR"	,
    "PINGLH"	:	"EUR"	,
    "PINGRM"	:	"EUR"	,
    "PINGRS"	:	"EUR"	,
    "PINGSP"	:	"EUR"	,
    "PINGUE"	:	"EUR"	,
    "PINOSA"	:	"EUR"	,
    "PIUSI"	:	"EUR"	,
    "PLOEGER"	:	"EUR"	,
    "PMCATT"	:	"EUR"	,
    "PMCCYL"	:	"EUR"	,
    "PMCDRIV"	:	"EUR"	,
    "PMCIND"	:	"EUR"	,
    "PMCPOL"	:	"EUR"	,
    "PMCRU"	:	"EUR"	,
    "PMCTEC"	:	"EUR"	,
    "PMI"	:	"EUR"	,
    "POCLA"	:	"GBP"	,
    "POCLAIT"	:	"EUR"	,
    "POCLAN"	:	"EUR"	,
    "POLAR"	:	"EUR"	,
    "PONAR"	:	"EUR"	,
    "PONSSE"	:	"EUR"	,
    "POTTIN"	:	"EUR"	,
    "POWER"	:	"EUR"	,
    "POWERTOWERS"	:	"GBP"	,
    "PRONAR"	:	"EUR"	,
    "PSG"	:	"EUR"	,
    "PSYST"	:	"EUR"	,
    "PTDHOE"	:	"EUR"	,
    "RAASM"	:	"EUR"	,
    "RABA"	:	"EUR"	,
    "RAMP"	:	"EUR"	,
    "RANDSA"	:	"EUR"	,
    "RANSOM"	:	"GBP"	,
    "RASCO"	:	"EUR"	,
    "RASTO"	:	"EUR"	,
    "RAVO"	:	"EUR"	,
    "RBNURN"	:	"GBP"	,
    "RBSCHW"	:	"EUR"	,
    "RECMAN"	:	"GBP"	,
    "RECYC"	:	"GBP"	,
    "REESINK"	:	"EUR"	,
    "RENAUL"	:	"EUR"	,
    "RENCIT"	:	"EUR"	,
    "RENGMBH"	:	"EUR"	,
    "REXBEL"	:	"EUR"	,
    "REXBRU"	:	"EUR"	,
    "REXRO"	:	"EUR"	,
    "RICARD"	:	"GBP"	,
    "RIMAST"	:	"EUR"	,
    "ROMAX"	:	"GBP"	,
    "RONZIO"	:	"EUR"	,
    "ROQUET"	:	"EUR"	,
    "ROQUETRO"	:	"EUR"	,
    "RUPPEL"	:	"EUR"	,
    "RYTTER"	:	"EUR"	,
    "SACE"	:	"EUR"	,
    "SAFIM"	:	"EUR"	,
    "SAHGEV"	:	"EUR"	,
    "SALAMI"	:	"EUR"	,
    "SALES"	:	"GBP"	,
    "SALTA"	:	"EUR"	,
    "SALUSPL"	:	"EUR"	,
    "SAMASZ"	:	"EUR"	,
    "SAME"	:	"EUR"	,
    "SANDVIK"	:	"EUR"	,
    "SANDVIKFR"	:	"EUR"	,
    "SANDVIKSP"	:	"EUR"	,
    "SANKO"	:	"EUR"	,
    "SANTHYD"	:	"USD"	,
    "SANY"	:	"EUR"	,
    "SAUERU"	:	"GBP"	,
    "SAVERY"	:	"GBP"	,
    "SAVERY2"	:	"GBP2"	,
    "SAVWEB"	:	"GBP"	,
    "SCHAEU"	:	"EUR"	,
    "SCHCRA"	:	"EUR"	,
    "SCHGER"	:	"EUR"	,
    "SCHLAN"	:	"EUR"	,
    "SCHNUPP"	:	"EUR"	,
    "SCHROT"	:	"EUR"	,
    "SCHSEU"	:	"EUR"	,
    "SCHWE"	:	"EUR"	,
    "SCIMA"	:	"EUR"	,
    "SDSLOV"	:	"EUR"	,
    "SEAL"	:	"EUR"	,
    "SEKURA"	:	"EUR"	,
    "SENNEBO"	:	"EUR"	,
    "SEPSON"	:	"EUR"	,
    "SERTA"	:	"EUR"	,
    "SERTABU"	:	"EUR"	,
    "SERVIM"	:	"EUR"	,
    "SERVO"	:	"GBP"	,
    "SERVO2"	:	"GBP2"	,
    "SERVOE"	:	"EUR"	,
    "SHPAC"	:	"USD"	,
    "SIAC"	:	"EUR"	,
    "SIGMAF"	:	"EUR"	,
    "SIMEX"	:	"EUR"	,
    "SINJIN"	:	"USD"	,
    "SKYJAC"	:	"GBP"	,
    "SLEIPN"	:	"EUR"	,
    "SMITS"	:	"EUR"	,
    "SMURF"	:	"GBP"	,
    "SNAPSS"	:	"EUR"	,
    "SNHSE1"	:	"GBP"	,
    "SOFR"	:	"EUR"	,
    "SOIL"	:	"EUR"	,
    "SORMIK"	:	"EUR"	,
    "SPX"	:	"EUR"	,
    "ST"	:	"EUR"	,
    "STACKE"	:	"EUR"	,
    "STER"	:	"GBP"	,
    "STERTIL"	:	"EUR"	,
    "STEYRE"	:	"EUR"	,
    "STIGWAHL"	:	"EUR"	,
    "STILFR"	:	"EUR"	,
    "STILL"	:	"EUR"	,
    "STILLH"	:	"EUR"	,
    "STILLHL"	:	"EUR"	,
    "STREP"	:	"EUR"	,
    "SUCCESS"	:	"USD"	,
    "SUMMIT"	:	"GBP"	,
    "SUNHYD"	:	"GBP"	,
    "SVAB"	:	"EUR"	,
    "SVENSK"	:	"EUR"	,
    "TAFE"	:	"GBP"	,
    "TANF"	:	"GBP"	,
    "TECFLUID"	:	"EUR"	,
    "TEKNOP"	:	"EUR"	,
    "TEKOR"	:	"EUR"	,
    "TELES"	:	"GBP"	,
    "TELLEF"	:	"EUR"	,
    "TENANT"	:	"EUR"	,
    "TENFAL"	:	"GBP"	,
    "TENGBP"	:	"GBP"	,
    "TERBERG"	:	"EUR"	,
    "TEREQU"	:	"GBP"	,
    "TEREXGB"	:	"GBP"	,
    "TEREXRO"	:	"EUR"	,
    "TERLIN"	:	"EUR"	,
    "TERROT"	:	"GBP"	,
    "TERXGLO"	:	"EUR"	,
    "TERXIND"	:	"GBP"	,
    "TERXIT"	:	"EUR"	,
    "TERXITGL"	:	"EUR"	,
    "TEST"	:	"EUR"	,
    "TEST1"	:	"GBP"	,
    "TEST2"	:	"GBP"	,
    "TESTLISA"	:	"GBP"	,
    "THIEVIN"	:	"EUR"	,
    "THURI"	:	"EUR"	,
    "TIANJIN"	:	"USD"	,
    "TIKAS"	:	"EUR"	,
    "TIKASHYD"	:	"EUR"	,
    "TILL"	:	"EUR"	,
    "TOKYO"	:	"USD"	,
    "TOMMYJ"	:	"EUR"	,
    "TORO"	:	"GBP"	,
    "TRANS"	:	"EUR"	,
    "TREBU"	:	"EUR"	,
    "TUBE"	:	"EUR"	,
    "TURNER"	:	"GBP"	,
    "TURNIND"	:	"GBP"	,
    "TVHNV"	:	"EUR"	,
    "TWIN"	:	"EUR"	,
    "TWINEU"	:	"EUR"	,
    "TWINIT"	:	"EUR"	,
    "UABEMS"	:	"EUR"	,
    "UNIDRO"	:	"EUR"	,
    "URBAN"	:	"EUR"	,
    "URSUS"	:	"EUR"	,
    "URSUSL"	:	"EUR"	,
    "UTILSV"	:	"EUR"	,
    "UZEL"	:	"EUR"	,
    "VADER"	:	"EUR"	,
    "VALE"	:	"GBP"	,
    "VALTRA"	:	"EUR"	,
    "VALVOLE"	:	"EUR"	,
    "VECA"	:	"EUR"	,
    "VELAVA"	:	"EUR"	,
    "VENETO"	:	"EUR"	,
    "VISTA"	:	"EUR"	,
    "VO938"	:	"EUR"	,
    "VOL191"	:	"EUR"	,
    "VOL300"	:	"EUR"	,
    "VOL890"	:	"EUR"	,
    "VOL901"	:	"EUR"	,
    "VOL903"	:	"EUR"	,
    "VOL905"	:	"EUR"	,
    "VOL924"	:	"EUR"	,
    "VOL938"	:	"GBP"	,
    "VOL956"	:	"EUR"	,
    "VOLIND"	:	"GBP"	,
    "VOLKOR"	:	"EUR"	,
    "VOLPEN"	:	"EUR"	,
    "VOLTAS"	:	"GBP"	,
    "VOLVAR"	:	"EUR"	,
    "VOLVBR"	:	"EUR"	,
    "VOLVBR2"	:	"EUR"	,
    "VOLVEU"	:	"EUR"	,
    "VOLVFR"	:	"EUR"	,
    "VOLVMX"	:	"EUR"	,
    "VOLVNL"	:	"EUR"	,
    "VOLVO4"	:	"EUR"	,
    "VOLVPO"	:	"EUR"	,
    "VOLVPT"	:	"EUR"	,
    "VOLVSE"	:	"EUR"	,
    "VORAN"	:	"EUR"	,
    "VYDRAULICS"	:	"EUR"	,
    "WABCO"	:	"EUR"	,
    "WALV"	:	"EUR"	,
    "WEBER"	:	"EUR"	,
    "WEIDEM"	:	"EUR"	,
    "WEMA"	:	"EUR"	,
    "WESSEL"	:	"EUR"	,
    "WESTPORT"	:	"EUR"	,
    "WESTPORT IT"	:	"EUR"	,
    "WEYHAU"	:	"EUR"	,
    "WIRTGEN"	:	"EUR"	,
    "WOLFEU"	:	"EUR"	,
    "YELLOW"	:	"GBP"	,
    "YOSHI"	:	"USD"	,
    "YTOFRA"	:	"EUR"	,
    "YUKEN"	:	"EUR"	,
    "ZEHS"	:	"EUR"	,
    "ZEPP"	:	"EUR"	,
    "ZEPRO"	:	"EUR"	,
    "ZETRA"	:	"EUR"	,
    "ZFARCO"	:	"GBP"	,
    "ZFAREU"	:	"EUR"	,
    "ZFFR"	:	"EUR"	,
    "ZFFRIE"	:	"EUR"	,
    "ZFMAR"	:	"EUR"	,
    "ZFPASS"	:"EUR"	,
    "ZFPDEU"	:"EUR"	,
    "ZFSCH"	:	"EUR"	,
    "ZFSER"	:	"EUR"	,
    }

# Define acceptable ExRate limits per currency
EXRATE_LIMITS = {
    "EUR": {"type": "exact", "value": 1.15},
    "EUR2": {"type": "range", "min": 1.1, "max": 2.0}, # Assuming EUR2 is meant to be EUR and using EUR2 as per your formula
    "USD": {"type": "exact", "value": 1.25},
    "GBP": {"type": "range", "min": 1.20, "max": 1.30}, # Example GBP range - adjust as needed, add to your formula if needed
    "GBP2": {"type": "range", "min": "1.20", "max": 1.30}, # Example GBP2 range - adjust as needed, add to your formula if needed
}


def process_data(uploaded_file):
    try:
        # Read Excel and remove header rows
        df = pd.read_excel(uploaded_file, skiprows=7)
        if df.empty:
            return None, "File appears empty after removing header rows"

        # Debug: Show raw data
        st.write("Raw data first 5 rows:")
        st.write(df.head())

        # Clean column names - convert all to string and strip whitespace
        df.columns = df.columns.astype(str).str.strip()

        # Debug: Show column names after cleaning
        st.write("Column names after cleaning:")
        st.write(df.columns.tolist())

        # Remove unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Remove blank rows (where 'Ln' is empty)
        if 'Ln' in df.columns:
            df = df[df['Ln'].notna()]
        else:
            available_cols = ", ".join(df.columns.tolist())
            st.error(f"Column 'Ln' not found. Available columns: {available_cols}")
            return None, "Column 'Ln' not found in the data"

        # Clean currency data with error handling
        if 'ExRate' in df.columns:
            df['ExRate'] = df['ExRate'].astype(str).str.strip()
            df['ExRate'] = pd.to_numeric(df['ExRate'].str.replace('/', ''), errors='coerce')
            invalid_rates = df[df['ExRate'].isna()] # Identify rows where ExRate is NaN (not converted)

            if not invalid_rates.empty:
                df.loc[invalid_rates.index, 'ExRate'] = "No exchange rate pulled from report" # Replace NaN with text

        else:
            st.error("Column 'ExRate' not found in the data")
            return None, "Column 'ExRate' not found in the data"

        # Check for 'Customer ID' column (instead of 'Customer')
        if 'Customer ID' not in df.columns:
            st.error("Column 'Customer ID' not found in the data. Please ensure your file has a 'Customer ID' column.")
            return None, "Column 'Customer ID' not found"

        # Create 'Currency Code' column based on 'Customer ID'
        df['Currency Code'] = df['Customer ID'].map(CUST_TO_CURR)

        # Debug: Show Currency Code column after creation
        st.write("Currency Code column after creation:")
        st.write(df[['Customer ID', 'Currency Code']].head())


        # Add Anomaly column and check for currency mismatch and ExRate anomalies
        df['Anomaly'] = ''
        for index, row in df.iterrows():
            customer_id = row['Customer ID'] # Use 'Customer ID'
            expected_currency = row['Currency Code'] # Now 'Currency Code' is created column
            actual_currency = row['Currency Code'] # Actual and Expected are the same in this logic, can adjust if needed later
            ex_rate = row['ExRate']

            if expected_currency is not None and str(actual_currency).strip() != str(expected_currency).strip(): # Still comparing against itself for now, adjust logic if needed for different 'actual' source
                df.loc[index, 'Anomaly'] += 'Currency Mismatch; ' # Flag currency mismatch - logic might need review

            # ExRate Anomaly Check
            if not pd.isna(ex_rate) and expected_currency in EXRATE_LIMITS and not isinstance(ex_rate, str): # Check for NaN ExRate, if currency has defined limits, and ensure ex_rate is not a string "No exchange rate..."
                limits = EXRATE_LIMITS[expected_currency]
                if limits["type"] == "exact":
                    if not abs(ex_rate - limits["value"]) < 1e-6: # Using tolerance for float comparison
                        df.loc[index, 'Anomaly'] += f'ExRate Anomaly (Expected {limits["value"]}); '
                elif limits["type"] == "range":
                    if not (limits["min"] <= ex_rate <= limits["max"]):
                        df.loc[index, 'Anomaly'] += f'ExRate Anomaly (Expected between {limits["min"]} and {limits["max"]}); '
            elif not pd.isna(ex_rate) and expected_currency is not None and expected_currency not in EXRATE_LIMITS and not isinstance(ex_rate, str): # Added check to avoid anomaly flag for "No exchange rate..." text
                 df.loc[index, 'Anomaly'] += f'No ExRate limits defined for {expected_currency}; ' # Flag if no limits are defined for currency


        # Remove trailing semicolon and space from Anomaly if not empty
        df['Anomaly'] = df['Anomaly'].str.rstrip('; ')

        return df, None

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None, str(e)


# Streamlit UI
st.title("FX Order Processing System")

st.markdown("[Click here to access Report](http://hffsuk02/Reports/report/ReportsUK/Customer/CoCustOrdRD2)")

st.markdown("""

Processing Instructions:
Upload the CoCustOrdRD2 Excel report

App will automatically:

Remove header rows

Clean data format

Identify exchange rate anomalies

Flag currency mismatches based on customer dictionary

Replaces unconvertible ExRates with "No exchange rate pulled from report"

Exports to Excel with two sheets: 'Processed Data' (all rows) and 'Anomalies' (only rows with anomalies)

Download processed file with anomaly flags

""")

uploaded_file = st.file_uploader("Upload CoCustOrdRD2 Report", type=["xlsx"])

if uploaded_file:
    processed_df, error = process_data(uploaded_file)

    if error:
        st.error(error)
    else:
        st.success("File processed successfully!")
        st.dataframe(processed_df)

        # --- Export functionality with two sheets ---
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            processed_df.to_excel(writer, sheet_name='Processed Data', index=False) # Sheet 1: All data

            # Filter for anomaly rows
            anomaly_df = processed_df[processed_df['Anomaly'] != '']
            anomaly_df.to_excel(writer, sheet_name='Anomalies', index=False) # Sheet 2: Anomaly rows

        st.download_button(
            label="Download Processed File",
            data=output.getvalue(),
            file_name="processed_orders.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

st.markdown("""

SM

""")
