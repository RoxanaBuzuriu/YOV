import re

# List of (regular expression, replacement) pairs for abbreviations in catalan:
abbreviations_ca = [
    (re.compile("\\b%s\\b" % x[0]), x[1])
    for x in [
        # Abbreviations without finishing dot
        ("&", "i"),
        ("@", "arrova"),
        ("A", "ampere"),
        ("B", "byte"),
        ("C", "carrer"),
        ("CCAA", "comunitat autònoma"),
        ("CIF", "codi d'identificació fiscal"),
        ("CP", "codi postal"),
        ("DEP", "descansi en pau"),
        ("DGT", "direcció general de transit"),
        ("DNI", "document nacional d'identitat"),
        ("DO", "denominació d'origen"),
        ("E", "est"),
        ("EUR", "euro"),
        ("Hz", "hertz"),
        ("JJOO", "jocs olímpics"),
        ("L", "litre"),
        ("M", "mega"),
        ("MB", "megabyte"),
        ("MB/s", "megabyte per segon"),
        ("MBps", "megabyte per segon"),
        ("MHz", "megahertz"),
        ("MW", "megawatt"),
        ("MWh", "megawatt hora"),
        ("Mb", "megabit"),
        ("Mb/s", "megabit per segon"),
        ("Mbps", "megabit per segon"),
        ("M€", "milió d'euros"),
        ("N", "nord"),
        ("NE", "nord-est"),
        ("NO", "nord-oest"),
        ("O", "oest"),
        ("PTA", "pesseta"),
        ("RRHH", "recursos humans"),
        ("SA", "societat anònima"),
        ("SE", "sud-est"),
        ("SL", "societat limitada"),
        ("SO", "sud-oest"),
        ("SP", "servei públic"),
        ("TV", "televisió"),
        ("V", "volt"),
        ("VO", "versió original"),
        ("VOS", "versió original subtitulada"),
        ("Wh", "watt hora"),
        ("aC", "abans de Crist"),
        ("am", "abans del migdia"),
        ("b", "bit"),
        ("c/", "carrer"),
        ("cal", "caloria"),
        ("cc", "centímetre cúbic"),
        ("cl", "centilitre"),
        ("cm", "centímetre"),
        ("dC", "després de Crist"),
        ("dc", "dimecres"),
        ("dg", "diumenge"),
        ("dj", "dijous"),
        ("dl", "decilitre"),
        ("dm", "decímetre"),
        ("ds", "dissabte"),
        ("dt", "dimarts"),
        ("dv", "divendres"),
        ("g", "gram"),
        ("h", "hora"),
        ("ha", "hectàrea"),
        ("kB", "kilobyte"),
        ("kV", "kilovolt"),
        ("kW", "kilowatt"),
        ("kWh", "kilowatt hora"),
        ("kb", "kilobit"),
        ("kg", "quilogram"),
        ("km", "kilòmetre"),
        ("km/h", "kilòmetre per hora"),
        ("m", "metre"),
        ("m/s", "metres per segon"),
        ("mg", "mil·ligram"),
        ("min", "minut"),
        ("mm", "mil·límetre"),
        ("pm", "després del migdia"),
        ("rpm", "revolucions per minut"),
        ("rps", "revolucions per segon"),
        ("s", "segon"),
        ("s/n", "sense número"),
        ("t", "tona"),
        ("§", "epígraf"),
        ("¶", "paràgraf"),
        ("º", "grau"),
        ("ºC", "grau Celsius"),
        ("ºF", "grau Fahrenheit"),
        ("ºR", "grau Rankine"),
        ("€", "euro"),

        # Acronyms
        ("ACB", "a ce be"),
        ("ADN", "a de ena"),
        ("AM", "a ema"),
        ("AMPA", "ampa"),
        ("ARN", "a erra ena"),
        ("ATP", "a te pe"),
        ("AVE", "ave"),
        ("BOE", "boe"),
        ("CD", "ce de"),
        ("CEIP", "ceip"),
        ("CNI", "ce ena i"),
        ("CPU", "ce pe u"),
        ("CUP", "cup"),
        ("CV", "ce ve"),
        ("DNI", "de ena i"),
        ("DVD", "de ve de"),
        ("ERC", "e erra ce"),
        ("ESO", "eso"),
        ("EUA", "Estats units d'America"),
        ("FBI", "efa be i"),
        ("FGC", "efa ge ce"),
        ("FM", "efa ema"),
        ("FP", "efa pe"),
        ("HD", "hac de"),
        ("HTML", "hac te ema ela"),
        ("HTTP", "hac te te pe"),
        ("IBI", "ibi"),
        ("IBM", "i be ema"),
        ("IEEE" "i e cub"),
        ("IES", "i es"),
        ("IP", "i pe"),
        ("IPC", "i pe ce"),
        ("IRPF", "i erra pe efa"),
        ("ISBN", "i essa be ena"),
        ("IVA", "iva"),
        ("LG", "ela ge"),
        ("LGTB", "ela ge te be"),
        ("NBA", "ena be a"),
        ("ONG", "o ena ge"),
        ("ONU", "onu"),
        ("OTAN", "otan"),
        ("PIME", "pime"),
        ("PLC", "pe ela ce"),
        ("PP", "pe pe"),
        ("PPC", "pe pe ce"),
        ("PSC", "pe essa ce"),
        ("PSG", "pe esa ge"),
        ("PSOE", "pesoe"),
        ("R+D", "erra més de"),
        ("RAM", "ram"),
        ("SA", "esa a"),
        ("SL", "essa ela"),
        ("TDA", "te de a"),
        ("TDAH", "te de a hac"),
        ("TMB", "te ema be"),
        ("TV", "Televisió"),
        ("UA", "u a"),
        ("UAB", "u a be"),
        ("UB", "u be"),
        ("UCD", "u ce de"),
        ("UCI", "uci"),
        ("UdG", "u de ge"),
        ("UdL", "u de ela"),
        ("UEFA", "uefa"),
        ("UMH", "u ema hac"),
        ("UNED", "uned"),
        ("UOC", "uoc"),        
        ("UPC", "u pe ce"),
        ("UPF", "u pe efa"),
        ("UPV", "u pe ve"),
        ("URL", "u erra ela"),
        ("UV", "u ve"),
        ("UVI", "uvi"),
        ("www", "ve doble"),
        
    ]
] + [
    (re.compile("\\b%s\\." % x[0]), x[1])
    for x in [
        # Abbreviations finishing with dot
        ("Dr", "doctor"),
        ("Dra", "doctora"),
        ("Sr", "senyor"),
        ("Sra", "senyora"),
        ("St", "sant"),
        ("Sta", "santa"),
        ("abr", "abril"),
        ("abrev", "abreviatura"),
        ("ago", "agost"),
        ("ant", "anterior"),
        ("apmt", "apartament"),
        ("aprox", "aproximadament"),
        ("apt", "apartat"),
        ("arq", "arquitecte"),
        ("art", "article"),
        ("atm", "atmosfera"),
        ("aux", "auxiliar"),
        ("av", "avinguda"),
        ("batx", "batxillerat"),
        ("bda", "baixada"),
        ("bl", "bloc"),
        ("c", "carrer"),
        ("cap", "capítol"),
        ("cast", "castellà"),
        ("cat", "català"),
        ("cia", "companyia"),
        ("col", "columna"),
        ("com", "comarca"),
        ("corp", "corporació"),
        ("cró", "carreró"),
        ("ct", "cèntim"),
        ("ctra", "carretera"),
        ("cènt", "cèntim"),
        ("dept", "departament"),
        ("des", "desembre"),
        ("dir", "direcció"),
        ("doc", "document"),
        ("dte", "descompte"),
        ("ed", "edició"),
        ("esc", "escala"),
        ("esp", "espanyol"),
        ("esq", "esquerre/rra"),
        ("etc", "etcètera"),
        ("ex", "exemple"),
        ("febr", "febrer"),
        ("fig", "figura"),
        ("fra", "factura"),
        ("gen", "gener"),
        ("inst", "institut"),
        ("ltda", "limitada"),
        ("màx", "màxim"),
        ("mín", "mínim"),
#        ("n. de l'e.", "nota de l'editor"),
#        ("n. de la t.", "nota de la traductora"),
#        ("n. de les ed.", "nota de les editores"),
#        ("n. de les t.", "nota de les traductores"),
#        ("n. del t.", "nota del traductor"),
#        ("n. dels ed.", "nota dels editors"),
#        ("n. dels t.", "nota dels traductors"),
        ("neg", "negatiu"),
        ("nov", "novembre"),
        ("núm", "número"),
        ("oct", "octubre"),
        ("parc", "parcel·la"),
        ("part", "particular"),
        ("pg", "passeig"),
        ("pl", "plaça"),
        ("pobl", "població"),
        ("pol", "polígon"),
        ("pos", "positiu"),
        ("ppal", "principal"),
        ("prev", "previ"),
        ("prof", "professor"),
        ("prog", "programa"),
        ("prov", "província"),
        ("pta", "pesseta"),
        ("ptes", "pessetes"),
        ("ptge", "passatge"),
        ("pàg", "pàgina"),
        ("rbla", "rambla"),
        ("ref", "referència"),
        ("reg", "regió"),
        ("s", "segle"),
        ("seg", "següent"),
        ("set", "setembre"),
        ("sign", "signatura"),
        ("sup", "superior"),
        ("supl", "suplement"),
        ("símb", "símbol"),
        ("tel", "telèfon"),
        ("trv", "travessia"),
        ("u", "unitat"),
        ("urb", "urbanització"),
        ("vol", "volum"),
        ("vs", "versus"),
        ("àt", "àtic"),
        ("íd", "ídem")
    ]
]
