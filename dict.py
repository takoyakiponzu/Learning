freetime = True
AM = True
PM = True

yuuki = [freetime, AM, PM]


yuuki = {
    "freetime": True,
    "AM": True,
    "PM": True,
    "goHome": '帰ります',
    "not goHome": '帰りません',
    "sleep": '寝ます',
}
if yuuki["freetime"] and yuuki["AM"]:
    print(yuuki["goHome"])
elif yuuki["freetime"] and yuuki["PM"]:
    print(yuuki["not goHome"])
else:
    print(yuuki["sleep"])

    #配列を使ってゆうきが暇で午前中なら帰ります
#ゆうきが暇で午後ならかえりません
#午前中でもなく午後でもないなら寝ます