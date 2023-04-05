#
# This is a script that has been used on
# the website "Mr. WorldWide" for transliteration  
# and tabel generation. This script can be used
# to transliterate Avestan words. You will find
# a few words below all asigned to the "txt" 
# variable. Just make sure that the "txt" var
# is set to the word you want to transliterate,
# then simply run the script.
# 
# The two first vars below are abereviations of
# Swedish words. 
# vok = Vokaler, "Vowels"
# kons = Konsonanter, "Consonants"
#

vok = """\
𐬀, a, /a/
𐬁, ā, /a:/
𐬂, å, /ɑ/
𐬃, ā̊, /ɑ:/
𐬄, ą, /ã/
𐬅, ą̇, /ã:/
𐬆, ə, /ə/
𐬇, ə̄, /ə:/
𐬈, e, /e/
𐬉, ē, /e:/
𐬊, o, /o/
𐬋, ō, /o:/
𐬌, i, /i/
𐬍, ī, /i:/
𐬎, u, /u/
𐬏, ū, /u:/"""
kons = """\
𐬐, k, /k/
𐬑, x, /x/
𐬒, x́, /x/
𐬓, xᵛ, /xʷ/
𐬔, g, /g/
𐬕, ġ, /g/
𐬖, γ, /ɣ/
𐬗, c, /tʃ/
𐬘, j, /dʒ/
𐬙, t, /t/
𐬚, ϑ, /θ/
𐬛, d, /d/
𐬜, δ, /ð/
𐬝, t̰, /t/
𐬞, p, /p/
𐬟, f, /ɸ/
𐬠, b, /b/
𐬡, β, /β/
𐬢, ŋ, /ŋ/
𐬣, ŋ́, /ŋ/
𐬤, ŋᵛ, /ŋʷ/
𐬥, n, /n/
𐬦, ń, /ɲ/
𐬧, ṇ, /n/
𐬨, m, /m/
𐬩, m̨, /m̥/
𐬪, ẏ, /j/
𐬫, y, /j/
𐬬, v, /w/
𐬭, r, /r/
𐬮, l, /l/
𐬯, s, /s/
𐬰, z, /z/
𐬱, š, /ʃ/
𐬲, ž, /ʒ/
𐬳, š́, /ʃ/
𐬴, ṣ̌, /ʃ/
𐬵, h, /h/"""
table_row = """\
<tr>
	<td class="ave">{char}</td>
	<td>{trans}</td>
	<td>{ipa}</td>
</tr>
"""
txt = "𐬎𐬞𐬀𐬯𐬙𐬀𐬎𐬎𐬀𐬐𐬀𐬉𐬥𐬀"
txt = "𐬰𐬀𐬭𐬀𐬚𐬎𐬱𐬙𐬭𐬀"
txt = "𐬁𐬙𐬀𐬭"
txt = "𐬀𐬴𐬀"
txt = "𐬛𐬭𐬎𐬘"
txt = "𐬫𐬀𐬰𐬀𐬙𐬀"
txt = "𐬨𐬀𐬰𐬛𐬁 𐬀𐬵𐬎𐬭𐬀"
"""for row in kons.split("\n"):
	r = row.split(", ")
	print(table_row.format(char=r[0], trans=r[1], ipa=r[2]))"""
for char in list(txt):
	found = False
	if char == " " or char == "\n" or char == "\t":
		print(char, end="")
		continue
	for row in kons.split("\n"):
		r = row.split(", ")
		if r[0] == char:
			found = True
			print(r[1], end="")
			break
	if not found:
		for row in vok.split("\n"):
			r = row.split(", ")
			if r[0] == char:
				found = True
				print(r[1], end="")
				break
	if not found:
		print("unknown character " + char)
print()