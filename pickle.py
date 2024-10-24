import pickle

profile_file = open( "profile.pickle", "wb" )
profile = { "이름" : "박명수", "나이" : 51, "취미" : ["수학", "프로그래밍"] }

print(profile)
pickle.dump( profile, profile_file )

profile_file.close()

profile_file = open( "profile.pickle", "rb" )
profileR = pickle.load(profile_file  )

print( profile )
profile_file.close()

with open( "SCORE.TXT", "r", encoding="utf-8" ) as profile_file:
    print( profile_file.read() )



for     