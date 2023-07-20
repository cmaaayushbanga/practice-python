import pyttsx3

def pronounce_names(name_list):
    engine = pyttsx3.init()

    for name in name_list:
        shoutout = f"Shoutout to {name}"
        engine.say(shoutout)
        print(shoutout)

    engine.runAndWait()

if __name__ == "__main__":
    l = ["Nikhil", "Nishant Kumar", "Aayush Banga"]
    pronounce_names(l)

# # For Mac
# from os import system
# names = ["StupidProgramm1","AayushGarg15", "Yuniek", "NiteshUpadhyay2", "RAMESHKUMAR69", "AshishKushwaha4", "AshokBhatt", "MILLANDREME", "ValorantAccoun4", "Sanjeevthakur8", "vivekRaogaddema", "NilutpalBaruah", "Priyanshu48", "KenZi2", "RahulGoyal14", "KartikeySurbhi", "AnirbanPati", "RohanPudasaini", "TechBlogs", "joelthomas1103", "dhairyapawaia", "PrithviSingh15", "GoogolChad", "Moinhusen", "mahi98989897", "Blitzfan1", "umang001", "AvijitManna1", "Mr-NeonNeon", "MaryamTatheer", "NishantJaiswal2", "AnonymousBuddy1", "MaryamTatheer", "GyanKumar1", "StarVipin", "vivekRaogaddema", "RaviSharma34", "AhsanTariq3", "gagankj", "ProgrammerShray", "AvijitDey5", "Anshuman097", "AnchalGupta9", "StupidProgramm1", "HimanshuKumar96", "hnxpriyanshu", "MaxM50", "piyushgoyall", "DEMANDHERE", "KrishnaAnand2", "SurajVishwaka10", "NominathKuwar", "firozeeIII", "jawad9899", "ArunavaAdhikari", "Quazi-Misbah-Raza", "HistoricMind", "Rajbir98", "AkshayNivate", "vivekRaogaddema", "maanitgill", "krushnsinh", "universelhome", "OPGAMEROPGAMERm", "universelhome", "learningtocodewithabdullah", "Abdullah426351", "SagarPathak3", "SAMARTH-VERMA", "PrithvirajPati3", "SAURABHTRIPATH6", "SumanRajak", "Swayam2004", "Joydip2002", "PulkitPareek", "RatnakarGautam221b", "tassawerzaidi", "GRyHacker", "uatta8088", "Athcode", "PrasoonShrivast", "piyushgoyall", "Saptak291", "PratyakshDhankh", "ZayanAhmad2", "Ali-RazaRaza9", "TridevJha", "KrrishHalder", "HeroProgrammin1", "Sanjeev-Kumar78", "AryanKushwaha2", "GalluBhai", "AB265", "AayushGarg15", "StupidProgramm1", "dheerajkumar68", "ArpitJaiswal2", "Fighters006", "AviPandit", "mrz004", "AviPandit", "MihirSingh4", "Nks-hkhk", "msCoder5", "SURAJGUSAIN1", "DivyanandPandey", "AhmadShuja", "JaydeepSindhav", "Champ7239", "piyushgoyall", "Joydip2002", "MukulVerma8745", "V-Durgeshwar-Ra", "SaacheKapoor", "41-GauravGaurav", "VeersinghZanka1", "LegendVibhu", "YashAgr", "vivekRaogaddema", "Priyanshu-kundu", "iamarghamallick", "samad90", "iamarghamallick", "MukulVerma8745", "MaxM50", "ItZgooseBoy", "piyushgoyall", "pavanteja14", "sologamerq1", "YugamTiwana", "piyushgoyall", "ShubhamSaini12", "AvishJain24", "ItZgooseBoy", "Iswastikmishra", "srisridmulti", "AvishJain24", "MFaizan3", "anukoolchauhan", "codeWithPrawar", "ArshitRupani", "Muhammad-Anas11"]
# for name in names:
#   system(f'say Shoutout to {name}')