"""
 * This is a script for generating IPA urls.
 * Can be used as import or as program.
"""
import os
ipa = {
	"ð": "https://en.wikipedia.org/wiki/Voiced_dental_fricative",
	"ɲ̟": "https://en.wikipedia.org/wiki/Voiced_palatal_nasal#Voiced_alveolo-palatal_nasal",
	"s̪": "https://en.wikipedia.org/wiki/Voiceless_alveolar_fricative#Voiceless_apico-alveolar_sibilant",
	"kʼ": "https://en.wikipedia.org/wiki/Velar_ejective_stop",
	"pʼ": "https://en.wikipedia.org/wiki/Bilabial_ejective_stop",
	"tʼ": "https://en.wikipedia.org/wiki/Dental_and_alveolar_ejective_stops",
	"qʼ": "https://en.wikipedia.org/wiki/Uvular_ejective_stop",
	"t͡sʼ": "https://en.wikipedia.org/wiki/Alveolar_ejective_affricate",
	"t͡ʃʼ": "https://en.wikipedia.org/wiki/Palato-alveolar_ejective_affricate",
	"d͡z": "https://en.wikipedia.org/wiki/Voiced_alveolar_affricate#Voiced_alveolar_sibilant_affricate",
	"d͡ʑ": "https://en.wikipedia.org/wiki/Voiced_alveolo-palatal_affricate",
	"v": "https://en.wikipedia.org/wiki/Voiced_labiodental_fricative",
	"d": "https://en.wikipedia.org/wiki/Voiced_dental_and_alveolar_plosives",
	"z": "https://en.wikipedia.org/wiki/Voiced_alveolar_fricative#Voiced_alveolar_sibilant",
	"ʐ": "https://en.wikipedia.org/wiki/Voiced_retroflex_fricative",
	"ʂ": "https://en.wikipedia.org/wiki/Voiceless_retroflex_fricative",
	"p": "https://en.wikipedia.org/wiki/Voiceless_bilabial_plosive",
	"m": "https://en.wikipedia.org/wiki/Voiced_bilabial_nasal",
	"n̥": "https://en.wikipedia.org/wiki/Voiceless_alveolar_nasal",
	"f": "https://en.wikipedia.org/wiki/Voiceless_labiodental_fricative",
	"t": "https://en.wikipedia.org/wiki/Voiceless_dental_and_alveolar_plosives",
	"n": "https://en.wikipedia.org/wiki/Voiced_dental,_alveolar_and_postalveolar_nasals",
	"l": "https://en.wikipedia.org/wiki/Voiced_dental,_alveolar_and_postalveolar_lateral_approximants#Voiced_alveolar_lateral_approximant",
	"ɬ": "https://en.wikipedia.org/wiki/Voiceless_dental_and_alveolar_lateral_fricatives",
	"ɬʼ": "https://en.wikipedia.org/wiki/Alveolar_lateral_ejective_fricative",
	"t͡ɬʼ": "https://en.wikipedia.org/wiki/Alveolar_lateral_ejective_affricate",
    "t͡ɬ": "https://en.wikipedia.org/wiki/Voiceless_alveolar_lateral_affricate",
	"ɭ": "https://en.wikipedia.org/wiki/Voiced_retroflex_lateral_approximant",
	"ɫ": "https://en.wikipedia.org/wiki/Voiced_dental,_alveolar_and_postalveolar_lateral_approximants#Velarized_alveolar_lateral_approximant",
	"k": "https://en.wikipedia.org/wiki/Voiceless_velar_plosive",
	"x": "https://en.wikipedia.org/wiki/Voiceless_velar_fricative",
	"χ": "https://en.wikipedia.org/wiki/Voiceless_uvular_fricative",
	"h": "https://en.wikipedia.org/wiki/Voiceless_glottal_fricative",
	"s": "https://en.wikipedia.org/wiki/Voiceless_alveolar_fricative#Voiceless_alveolar_sibilants",
	"ʑ": "https://en.wikipedia.org/wiki/Voiced_alveolo-palatal_fricative",
	"w": "https://en.wikipedia.org/wiki/Voiced_labial–velar_approximant",
	"ɥ": "https://en.wikipedia.org/wiki/Voiced_labial–palatal_approximant",
	"j": "https://en.wikipedia.org/wiki/Voiced_palatal_approximant",
	"b": "https://en.wikipedia.org/wiki/Voiced_bilabial_plosive",
	"i": "https://en.wikipedia.org/wiki/Close_front_unrounded_vowel",
	"y": "https://en.wikipedia.org/wiki/Close_front_rounded_vowel",
	"ʏ̫": "https://en.wikipedia.org/wiki/Near-close_near-front_rounded_vowel#Near-close_front_protruded_vowel",
	"ɨ": "https://en.wikipedia.org/wiki/Close_central_unrounded_vowel",
	"ʉ": "https://en.wikipedia.org/wiki/Close_central_rounded_vowel",
	"ɯ": "https://en.wikipedia.org/wiki/Close_back_unrounded_vowel",
	"ɰ": "https://en.wikipedia.org/wiki/Voiced_velar_approximant",
	"u": "https://en.wikipedia.org/wiki/Close_back_rounded_vowel",
	"ɪ": "https://en.wikipedia.org/wiki/Near-close_near-front_unrounded_vowel",
	"ʏ": "https://en.wikipedia.org/wiki/Near-close_near-front_rounded_vowel",
	"ʊ": "https://en.wikipedia.org/wiki/Near-close_near-back_rounded_vowel",
	"e": "https://en.wikipedia.org/wiki/Close-mid_front_unrounded_vowel",
	"ø": "https://en.wikipedia.org/wiki/Close-mid_front_rounded_vowel",
	"ɘ": "https://en.wikipedia.org/wiki/Close-mid_central_unrounded_vowel",
	"ɵ": "https://en.wikipedia.org/wiki/Close-mid_central_rounded_vowel",
	"ɤ": "https://en.wikipedia.org/wiki/Close-mid_back_unrounded_vowel",
	"o": "https://en.wikipedia.org/wiki/Close-mid_back_rounded_vowel",
	"ʊ͍": "https://en.wikipedia.org/wiki/Near-close_near-back_rounded_vowel#Near-close_back_compressed_vowel",
	"e̞": "https://en.wikipedia.org/wiki/Mid_front_unrounded_vowel",
	"ø̞": "https://en.wikipedia.org/wiki/Mid_front_rounded_vowel",
	"œ̝": "https://en.wikipedia.org/wiki/Mid_front_rounded_vowel",
	"ɟ": "https://en.wikipedia.org/wiki/Voiced_palatal_plosive",
	"r̝": "https://en.wikipedia.org/wiki/Voiced_dental,_alveolar_and_postalveolar_trills#Voiced_alveolar_fricative_trill",
	"ɾ": "https://en.wikipedia.org/wiki/Voiced_dental_and_alveolar_taps_and_flaps#Voiced_alveolar_tap_and_flap",
	"ɽ": "https://en.wikipedia.org/wiki/Voiced_retroflex_flap",
	"ɺ̣": "https://en.wikipedia.org/wiki/Voiced_retroflex_lateral_flap",
	"ɺ̠": "https://en.wikipedia.org/wiki/Voiced_retroflex_lateral_flap",
	"ə": "https://en.wikipedia.org/wiki/Mid_central_vowel",
	"ɤ̞": "https://en.wikipedia.org/wiki/Mid_back_unrounded_vowel",
	"o̞": "https://en.wikipedia.org/wiki/Mid_back_rounded_vowel",
	"ɛ": "https://en.wikipedia.org/wiki/Open-mid_front_unrounded_vowel",
	"œ": "https://en.wikipedia.org/wiki/Open-mid_front_rounded_vowel",
	"ɜ": "https://en.wikipedia.org/wiki/Open-mid_central_unrounded_vowel",
	"ɞ": "https://en.wikipedia.org/wiki/Open-mid_central_rounded_vowel",
	"ʌ": "https://en.wikipedia.org/wiki/Open-mid_back_unrounded_vowel",
	"ɔ": "https://en.wikipedia.org/wiki/Open-mid_back_rounded_vowel",
	"æ": "https://en.wikipedia.org/wiki/Near-open_front_unrounded_vowel",
	"ɐ": "https://en.wikipedia.org/wiki/Near-open_central_vowel",
	"a": "https://en.wikipedia.org/wiki/Open_front_unrounded_vowel",
	"ɶ": "https://en.wikipedia.org/wiki/Open_front_rounded_vowel",
	"ä": "https://en.wikipedia.org/wiki/Open_central_unrounded_vowel",
	"m̥": "https://en.wikipedia.org/wiki/Voiceless_bilabial_nasal",
	"ɑ": "https://en.wikipedia.org/wiki/Open_back_unrounded_vowel",
	"ɒ": "https://en.wikipedia.org/wiki/Open_back_rounded_vowel",
	"θ": "https://en.wikipedia.org/wiki/Voiceless_dental_fricative",
	"r": "https://en.wikipedia.org/wiki/Voiced_dental,_alveolar_and_postalveolar_trills#Voiced_alveolar_trill",
	"r̥": "https://en.wikipedia.org/wiki/Voiceless_alveolar_trill",
	"ɹ": "https://en.wikipedia.org/wiki/Voiced_alveolar_and_postalveolar_approximants",
    "ɻ": "https://en.wikipedia.org/wiki/Voiced_retroflex_approximant",
	"ʀ": "https://en.wikipedia.org/wiki/Voiced_uvular_trill",
	"ʁ": "https://en.wikipedia.org/wiki/Voiced_uvular_fricative",
	"ɡ": "https://en.wikipedia.org/wiki/Voiced_velar_plosive",
	"ʃ": "https://en.wikipedia.org/wiki/Voiceless_postalveolar_fricative#Voiceless_palato-alveolar_fricative",
	"q": "https://en.wikipedia.org/wiki/Voiceless_uvular_plosive",
	"ɢ": "https://en.wikipedia.org/wiki/Voiced_uvular_plosive",
	"ɣ": "https://en.wikipedia.org/wiki/Voiced_velar_fricative",
	"ʕ": "https://en.wikipedia.org/wiki/Voiced_pharyngeal_fricative",
	"ʝ": "https://en.wikipedia.org/wiki/Voiced_palatal_fricative",
	"β": "https://en.wikipedia.org/wiki/Voiced_bilabial_fricative",
	"c": "https://en.wikipedia.org/wiki/Voiceless_palatal_plosive",
	"ɲ": "https://en.wikipedia.org/wiki/Voiced_palatal_nasal",
	"ç": "https://en.wikipedia.org/wiki/Voiceless_palatal_fricative",
	"ç": "https://en.wikipedia.org/wiki/Voiceless_palatal_fricative",
	"ŋ": "https://en.wikipedia.org/wiki/Voiced_velar_nasal",
	"ʔ": "https://en.wikipedia.org/wiki/Glottal_stop",
	"t͡s": "https://en.wikipedia.org/wiki/Voiceless_alveolar_affricate#Voiceless_alveolar_sibilant_affricate",
	"d͡ʒ": "https://en.wikipedia.org/wiki/Voiced_postalveolar_affricate",
	"t͡ʃ": "https://en.wikipedia.org/wiki/Voiceless_postalveolar_affricate",
	"t͡ɕ": "https://en.wikipedia.org/wiki/Voiceless_alveolo-palatal_affricate",
	"ʒ": "https://en.wikipedia.org/wiki/Voiced_postalveolar_fricative#Voiced_palato-alveolar_fricative",
	"ɦ": "https://en.wikipedia.org/wiki/Voiced_glottal_fricative",
	"ħ": "https://en.wikipedia.org/wiki/Voiceless_pharyngeal_fricative",
	"ʜ": "https://en.wikipedia.org/wiki/Voiceless_epiglottal_trill",
	"ʢ": "https://en.wikipedia.org/wiki/Voiced_epiglottal_trill",
	"ɔ̝": "https://en.wikipedia.org/wiki/Mid_back_rounded_vowel",
	"ɸ": "https://en.wikipedia.org/wiki/Voiceless_bilabial_fricative",
	"ɕ": "https://en.wikipedia.org/wiki/Voiceless_alveolo-palatal_fricative",
	"ɫ": "https://en.wikipedia.org/wiki/Voiced_dental,_alveolar_and_postalveolar_lateral_approximants#Velarized_alveolar_lateral_approximant",
	"ꞎ": "https://en.wikipedia.org/wiki/Voiceless_retroflex_lateral_fricative",
	"ʎ": "https://en.wikipedia.org/wiki/Voiced_palatal_lateral_approximant",
	"ʋ": "https://en.wikipedia.org/wiki/Voiced_labiodental_approximant",
	"ˤ": "https://en.wikipedia.org/wiki/Pharyngealization",
	"ʲ": "https://en.wikipedia.org/wiki/Palatalization_(phonetics)",
	"ʰ": "https://en.wikipedia.org/wiki/Aspirated_consonant",
	"ˠ": "https://en.wiktionary.org/wiki/ˠ",
	"ʷ": "https://en.wikipedia.org/wiki/Labialization"
}
template='<a class="ipa" href="{url}" title="{name}">{char}</a>'
def urlToName(url):
		if "#" in url:
			return url.split("#")[1].replace("_", " ")
		elif "/wiki/" in url:
			return url.split("/wiki/")[1].replace("_", " ")
		else:
			return "input error"
def ipaToHtml(i, t=template):
	if i == "/":
		return ""
	u = ipa[i.replace("ː", "").replace(".", "")]
	return t.format(url=u, name=urlToName(u), char=i)
def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
def getIPA(inp):
	one_list = ["n̥", "t͡s", "d͡ʒ", "t͡ʃ", "d͡z", "t͡ɕ", "r̥", "t͡ʃʼ", "t͡ɬʼ","t͡ɬ", "d͡ʑ", "ʏ̫", "ʊ͍", "ɺ̣", "ɺ̠"]
	rv = ""
	if inp == "stop" or inp == "exit":
		exit()
	elif inp.strip() == "":
		return rv
	elif inp == "clexit" or inp == "cexit":
		clearScreen()
		exit()
	elif inp == "cls" or inp == "clear":
		clearScreen()
	else:
		inp = inp.replace("g", "ɡ").replace("γ", "ɣ")
		if len(inp) < 2 or inp in one_list :
			rv += f"[{ipaToHtml(inp)}]"
		elif len(inp) == 0:
			return rv
		else:
			inp = inp.replace("/, /", ",").replace(", ", ",").replace("/ or /", ",")
			items = []
			for char in list(inp):
				if char == "ː" or char == "." or char == "̥" or char == "̞" or char == "̝" or char == "ʼ":
					items[len(items)-1] = items[len(items)-1]+char
				else:
					items.append(char)
			rv += "["
			i = 0
			keepList = "ˈ~˧˥˨˩˦˥"
			while i < len(items):
				if i == len(items)-1:
					rv += ipaToHtml(items[i])
				elif items[i] == ",":
					rv += ", "
				elif items[i] in keepList:
					rv += items[i]
				else:
					rv += ipaToHtml(items[i])
				i+=1
			rv += "]"
	return rv
if __name__ == "__main__":
	while True:
		inp = str(input("Enter IPA:"))
		print(getIPA(inp))
